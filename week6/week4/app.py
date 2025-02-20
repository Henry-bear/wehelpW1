from fastapi import FastAPI, Form, Request, Depends, Path
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
from starlette.requests import Request as StarletteRequest
from typing import Annotated

app = FastAPI()

# Task 1~3 
# 設定模板文件路徑
templates = Jinja2Templates(directory="templates")

# 加入 SessionMiddleware
app.add_middleware(SessionMiddleware, secret_key="your-secret-key")

# 從請求中獲取會話的依賴函數
def get_session(request: StarletteRequest):
    return request.session

# 首頁 index (GET)
@app.get("/")
def index_page(request: Request):
    # 導向至首頁 index
    return templates.TemplateResponse("index.html", {"request": request})

# 驗證 Verification Endpoint (POST)
@app.post("/signin")
# 從 HTTP POST 請求的表單中提取 account 及 password 欄位，資料型態為字串 ，透過依賴注入來獲取的字典資料
def signin(request: Request, account: str = Form(...), password: str = Form(...), session: dict = Depends(get_session)):
    if not account or not password:
    # 如果帳號或密碼未輸入，導向到錯誤頁面 /error
        return RedirectResponse(url="/error?message=帳號、或密碼尚未輸入", status_code=303)
    # 帳號和密碼驗證 帳密皆為 test
    if account == "test" and password == "test":
        # 設定變量，表示已登入
        session["SIGNED-IN"] = True
        return RedirectResponse(url="/member", status_code=303)
    # 如果帳號或密碼錯誤，導向到錯誤頁面 /error
    else:
        return RedirectResponse(url="/error?message=帳號、或密碼輸入錯誤", status_code=303)
    
# 成功登入頁面 Success Page (GET) 只有在登入時顯示
@app.get("/member")
def member_page(request: Request, message: str="恭喜您，成功登入系統", session: dict = Depends(get_session)):
    # 如果判斷尚未登入，重定導向至 首頁 index
    if not session.get("SIGNED-IN"):
        return RedirectResponse(url="/", status_code=303)
    # 判斷登入成功，導向至 /member
    return templates.TemplateResponse("member.html", {"request": request, "message": message})

# 登入失敗 錯誤頁面 Error Page (GET)
@app.get("/error")
def error_page(request: Request, message: str):
    # 登入失敗，導向至 /error
    return templates.TemplateResponse("error.html", {"request": request, "message": message})

# 驗證 Signout Endpoint (GET) 確認是否有成功登出
@app.get("/signout")
def signout(request: Request, session: dict = Depends(get_session)):
    # 設定變量，表示已登出
    session["SIGNED-IN"] = False
    # 成功登出，導向至首頁 index
    return RedirectResponse(url="/", status_code=303)

#---------------------------------------------------------------------

# Task 4: Path Parameter (Optional)

# 顯示計算結果，使用路徑參數來接收數值 num
@app.get("/square/{num}")
# 設定 num 為 int  且必須大於 0
def square_result_page(request: Request, num: Annotated[int, Path(..., gt=0)]):
    result = num * num
    return templates.TemplateResponse("square.html", {"request": request, "result": result})

# 設定靜態文件路徑 (main.css)
app.mount("/static", StaticFiles(directory="static"), name="static")


# 使用 uvicorn 啟動伺服器
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)