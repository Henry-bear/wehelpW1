from fastapi import FastAPI, Form, Request, Depends, HTTPException, Query, Body
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
from starlette.requests import Request as StarletteRequest
from sqlalchemy import create_engine, Column, Integer, String, BIGINT, DateTime, func, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
from sqlalchemy.exc import SQLAlchemyError
import pymysql
from typing import Optional
from pydantic import BaseModel, Field


app = FastAPI()

# ------------------------------- Task 1 ~ 4 ------------------------------------------
# 設定模板文件路徑
templates = Jinja2Templates(directory="templates")

# 加入SessionMiddleware
app.add_middleware(SessionMiddleware, secret_key="your-secret-key")

# SQLAlchemy 設定
# 資料庫的連接資訊
DATABASE_URL = "mysql+pymysql://root:12345678@localhost/website"
# 建立資料庫引擎，負責連接資料庫
engine = create_engine(DATABASE_URL)
# 建立資料庫會話，與資料庫互動
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# 建立一個基礎類別
Base = declarative_base()

# 使用者模型
# member Table
class Member(Base):
    __tablename__ = "member"
    id = Column(BIGINT, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    username = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    follower_count = Column(Integer, nullable=False, default=0)
    time = Column(DateTime, nullable=False, default=func.now())
    # 與 Message 資料表建立關聯
    messages = relationship("Message", back_populates="member")
# message Table
class Message(Base):
    __tablename__ = "message"
    id = Column(BIGINT, primary_key=True, index=True, autoincrement=True)
    member_id = Column(BIGINT, ForeignKey('member.id'), nullable=False)
    content = Column(String(255), nullable=False)
    like_count = Column(Integer, nullable=False, default=0)
    time = Column(DateTime, nullable=False, default=func.now())
    # 與 Member 資料表建立關聯(代表訊息屬於該會員)
    member = relationship("Member", back_populates="messages")

# 建立資料表
Base.metadata.create_all(bind=engine)

# 從請求取得對話的依賴函數
def get_session(request: StarletteRequest):
    return request.session

# 取得資料庫對話的依賴函數
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 定義 Pydantic 模型
class UpdateNameRequest(BaseModel):
    name: str = Field(..., example="新的使用者姓名")

# 首頁 index (GET)
@app.get("/")
def index_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
# 處理註冊表單 (POST)
@app.post("/signup")
def signup(
    request:Request, 
    name: str = Form(...), 
    username: str = Form(...), 
    password: str = Form(...), 
    session: dict=Depends(get_session), 
    db: Session = Depends(get_db)
):
    # 檢查帳號是否已經存在 
    # query(Member)  等同  SELECT * FROM member
    # filter() 等同 SELECT * FROM member WHERE username = '某個帳號';
    # first() 執行查詢，並回傳第一筆找到的資料
    existing_user = db.query(Member).filter(Member.username == username).first()
    # 假設 username 存在，導向錯誤頁面 error，顯示帳號已存在的訊息
    if existing_user:
        return templates.TemplateResponse("error.html", {"request": request, "message": "帳號已經存在，請使用其他帳號註冊"})
    new_user = Member(name=name, username=username, password=password)
    # 新增帳號，例外處理
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)  # 刷新
    except Exception as e:
        # 發生錯誤時復原變更
        db.rollback()
        raise HTTPException(status_code=500, detail="Internal Server Error")
    session["SIGNED-IN"] = True
    session["USERNAME"] = username
    session["NAME"] = name
    # 註冊成功，導向首頁 index
    return RedirectResponse(url="/", status_code=303)
# 驗證登入 (POST)
@app.post("/signin")
def signin(
    request: Request, 
    username: str = Form(...), 
    password: str = Form(...), 
    session: dict=Depends(get_session), 
    db: Session = Depends(get_db)
):
    user = db.query(Member).filter(Member.username == username).first()
    if user and user.password == password:
        session["SIGNED-IN"] = True
        session["USERNAME"] = username
        session["NAME"] = user.name
        session["ID"] = user.id
        # 帳號密碼正確，導向到會員頁面 /member
        return RedirectResponse(url="/member", status_code=303)
    # 如果帳號或密碼錯誤，導向到錯誤頁面 /error
    else:
        return RedirectResponse(url="/error?message=帳號、或密碼輸入錯誤", status_code=303)
# 驗證登出 (GET)
@app.get("/signout")
def signout(
    request: Request, 
    session: dict = Depends(get_session)
):
    session["SIGNED-IN"] = False
    session.pop("USERNAME", None)
    session.pop("NAME", None)
    session.pop("ID", None)
    # 成功登出，導向至首頁 index
    return RedirectResponse(url="/", status_code=303)
# 會員頁面 (GET)
@app.get("/member")
def member_page(
    request: Request, 
    session: dict = Depends(get_session), 
    db: Session = Depends(get_db)
):
    # 如果判斷尚未登入，重定導向至 首頁 index
    if not session.get("SIGNED-IN"):
        return RedirectResponse(url="/", status_code=303)
    #  Message table 的 所有內容
    messages = db.query(Message).all()
    # 判斷登入成功，導向至 /member
    return templates.TemplateResponse("member.html", {"request": request, "name": session.get("NAME"), "message": "，歡迎登入系統", "messages": messages, "user_id": session.get("ID")})

# ------------------------------- Task 5 ~ 6 ------------------------------------------
# 建立訊息 (POST)
@app.post("/createMessage")
def create_message(
    request: Request, 
    content: str = Form(...), 
    session: dict = Depends(get_session), 
    db: Session = Depends(get_db)
):
    if not session.get("SIGNED-IN"):
        return RedirectResponse(url="/", status_code=303)
    member_id = session.get("ID")
    new_message = Message(content=content, member_id=member_id)
    # 新增訊息，例外處理
    try:
        db.add(new_message)
        db.commit()
        db.refresh(new_message) # 刷新
    except Exception as e:
        # 發生錯誤時復原變更
        db.rollback()
        raise HTTPException(status_code=500, detail="Internal Server Error")
    return RedirectResponse(url="/member", status_code=303)

# 刪除訊息內容 (POST)
@app.post("/deleteMessage")
def delete_message_content(
    request: Request, 
    message_id: int = Form(...), 
    session: dict = Depends(get_session), 
    db: Session = Depends(get_db)
):
    if not session.get("SIGNED-IN"):
        return RedirectResponse(url="/", status_code=303)
    member_id = session.get("ID")
    message = db.query(Message).filter(Message.id == message_id, Message.member_id == member_id).first()
    if not message:
        raise HTTPException(status_code=404, detail="Message not found or not authorized")
    # 刪除訊息，例外處理
    try:
        db.delete(message)
        db.commit()
    except Exception as e:
        # 發生錯誤時復原變更
        db.rollback()
        raise HTTPException(status_code=500, detail="Internal Server Error")
    return RedirectResponse(url="/member", status_code=303)

# 錯誤頁面 (GET)
@app.get("/error")
def error_page(request: Request, message: str):
    return templates.TemplateResponse("error.html", {"request": request, "message": message})

# =================================== Week7 =====================================================
# ================================= Task 1~3 ====================================================

# 會員查詢 API (GET)
@app.get("/api/member")
def get_member(
    username: Optional[str] = Query(None), # 從查詢參數取得要查詢的會員名稱
    session: dict = Depends(get_session), 
    db: Session = Depends(get_db)
):
    if not session.get("SIGNED-IN"): # 阻止使用者直接連線 /api/member ，如果未登入則顯示錯誤 401
        return JSONResponse(content={"error": "Unauthorized"}, status_code=401)
    # 查詢會員帳號 (username)，例外處理
    try:
        if username:
            # 查詢使用者是否存在
            user = db.query(Member).filter(Member.username == username).first()
            if user:
             return JSONResponse(content={"data": {"id": user.id, "name": user.name, "username": user.username}})
        return JSONResponse(content={"data": None})
    except SQLAlchemyError as e:
        # SQL 錯誤時顯示 500
        return JSONResponse(content={"error": str(e)}, status_code=500)

# 姓名更新 API (PATCH)
@app.patch("/api/member")
def update_member_name(
    body: UpdateNameRequest, # 對應前端 JSON.stringify({ name: newName })
    session: dict = Depends(get_session), 
    db: Session = Depends(get_db)
):
    if not session.get("SIGNED-IN"): # 阻止使用者直接連線 /api/member ，如果未登入則顯示錯誤 401
        return JSONResponse(content={"error": True}, status_code=401)
    # 更新姓名(name)，例外處理
    try:
        username = session.get("USERNAME")
        new_name = body.name    # 取得新名字，對應 JSON.stringify({ name: newName })
        # 假設沒有輸入姓名，回傳錯誤
        if not new_name:
         return JSONResponse(content={"error": True}, status_code=400)
        # 查詢使用者是否存在
        user = db.query(Member).filter(Member.username == username).first()

        if user:
            user.name = new_name
            db.commit()
            session["NAME"] = new_name  # 更新 session 資訊
            return JSONResponse(content={"ok": True})                  # 前端 if (data.ok)
        return JSONResponse(content={"error": True}, status_code=400)  # 前端 if (!data.ok)
    except SQLAlchemyError as e:
        # SQL 錯誤時顯示 500
        return JSONResponse(content={"error": str(e)}, status_code=500) 

# 設定靜態文件路徑 (main.css)
app.mount("/static", StaticFiles(directory="static"), name="static")

# 使用 uvicorn 啟動伺服器
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=3000)
