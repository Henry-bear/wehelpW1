# Task 1
# 串接、擷取公開資料
import urllib.request as request
import json
import csv
src1="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
src2="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2"
# 抓取 景點資料
with request.urlopen(src1) as spotResponse:
    spotData=json.load(spotResponse) 
spotList=spotData["data"]["results"]
# print(spotList)

# 抓取 捷運站資料
with request.urlopen(src2) as mrtResponse:
    mrtData=json.load(mrtResponse)
mrtList=mrtData["data"]
# print(mrtList)
# 建立 district 篩選函式 (address)
allDistrict=["中正區", "萬華區", "中山區", "大同區", "大安區", "松山區", "信義區", "士林區", "文山區", "北投區", "內湖區", "南港區"]
def extract_district(address):
    for district in allDistrict:
        if district in address:
            return district
    return "Unknown"
# 建立一個 SERIAL_NO 到 District 的對應
serial_no_to_district = {mrt["SERIAL_NO"]: extract_district(mrt["address"]) for mrt in mrtList}

# SpotTitle,District,Longitude,Latitude,ImageURL
with open("spot.csv", "w",encoding="utf-8") as file:
    writer = csv.writer(file)
    
    for spot in spotList:
        # SpotTitle
        spot_title = spot["stitle"]

        # District
        serial_no = spot["SERIAL_NO"]
        district = serial_no_to_district.get(serial_no)

        # Longitude, Latitude
        longitude = spot["longitude"]
        latitude = spot["latitude"]

        #ImageURL
        urls = spot["filelist"].split("https://")
        urls = ["https://" + url for url in urls if url]
        first_image_url = urls[0] if urls else ""

        # 寫進 CSV 檔
        writer.writerow([spot_title, district, longitude, latitude, first_image_url])

# StationName,AttractionTitle1,AttractionTitle2,AttractionTitle3,...
# 建立一個 SERIAL_NO 到 MRT 的對應
serial_no_to_mrt = {mrt["SERIAL_NO"]: mrt["MRT"] for mrt in mrtList}
# 建立一個 MRT 到景點標題的對應
mrt_to_spots = {}

for spot in spotList:
    serial_no = spot["SERIAL_NO"]
    spot_title = spot["stitle"]
    mrt_station = serial_no_to_mrt.get(serial_no, None)
    if mrt_station:
        if mrt_station not in mrt_to_spots:
            mrt_to_spots[mrt_station] = []
        mrt_to_spots[mrt_station].append(spot_title)

# 寫入 mrt.csv
with open("mrt.csv", "w", encoding="utf-8") as file:
    writer = csv.writer(file)
    for mrt_station, spots in mrt_to_spots.items():
        row = [mrt_station] + spots
        writer.writerow(row)

# ===========================================分隔線====================================================

# Task 2
# Parse web page data and save to files by Python
import urllib.request as req
import bs4
# 抓取網頁內容
def fetch_page_content(url):
    request = req.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    return data
# 抓取文章內文時間
def parse_article_date(url):
    data = fetch_page_content(url)
    root = bs4.BeautifulSoup(data, "html.parser")
    meta_values = root.find_all("span", class_="article-meta-value")
    if meta_values:
        date = meta_values[3].get_text()  # 假設時間是第四個元素
    else:
        date = ""
    return date

def get_data(url):
    data = fetch_page_content(url)
    root = bs4.BeautifulSoup(data, "html.parser")
    titles = root.find_all("div", class_="title")
    like_counts = root.find_all("div", class_="nrec")
    articles = []

    for title, like_count in zip(titles, like_counts):
        # 文章標題
        if title.a is not None:
            title_text = title.a.string
            # 按讚
            span = like_count.find("span")
            if span:
                number = span.text
            else:
                number = "0"
            # 取得文章超連結
            page_url = "https://www.ptt.cc" + title.a["href"]
            article_date = parse_article_date(page_url)
            articles.append([title_text, number, article_date])
    # 取得下一頁（另一頁）超連結
    next_page_url = root.find("a", string="‹ 上頁")
    if next_page_url:
        next_page_url = "https://www.ptt.cc" + next_page_url["href"]
    else:
        next_page_url = None

    return articles, next_page_url

# 主程序: 抓取多個頁面的標題
page_url = "https://www.ptt.cc/bbs/Lottery/index.html"
count = 0
all_articles = []

while count < 3:
    articles, page_url = get_data(page_url)
    all_articles.extend(articles)
    if page_url is None:
        break
    count += 1

# 寫入 article.csv
with open("article.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    for article in all_articles:
        writer.writerow(article)

print("檔案寫入完成")