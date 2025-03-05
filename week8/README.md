# Topic 1
**HTML <script> Attributes**

* There are 2 attributes, defer and async, that we can use in <script> tag to change the script loading and executing behavior.
Follow learning steps below to prepare your report:
>`在 HTML 中，<script> 標籤有兩個關鍵屬性：defer 和 async，它們會影響 JavaScript 的加載和執行方式`

1. What happens If we add a defer attribute to a <script> tag?  
>`如果我們在 <script> 標籤中加入 defer 屬性，會發生什麼？`
* 當 script 標籤帶有 defer 屬性時，瀏覽器會先下載該腳本，但等到 HTML 文檔完全解析完畢後才執行。
這樣可以確保 JavaScript 只在 DOM 樹準備好之後執行，不會影響 HTML 解析過程。

**特性：**
- 腳本會被延遲執行，直到 HTML 解析完畢後才運行。
- 多個 defer 腳本會按照它們在 HTML 中的出現順序執行（保證執行順序）。
- 只能用於外部腳本 (<script src="..." defer></script>)，不能用於內聯腳本。
適合情境：當 JavaScript 需要操作 DOM 時（例如，添加事件監聽器或修改 HTML 結構）。

```html
<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <title>Defer Example</title>
    <script src="script.js" defer></script>
</head>
<body>
    <h1>Hello, world!</h1>
</body>
</html>
```
`在這個例子中，script.js 會在 HTML 文檔解析完畢後執行，確保 h1 標籤已經載入，避免 document.querySelector('h1') 找不到元素的問題。`

2. What happens If we add an async attribute to a <script> tag?  
>`如果我們在 <script> 標籤中加入 async 屬性，會發生什麼？`
* 當 script 標籤帶有 async 屬性時，瀏覽器會異步下載該腳本，並且在下載完成後立即執行，不會等待 HTML 完全解析。這可能會導致腳本執行順序變得不確定。

**特性：**

- 腳本會與 HTML 解析同步下載，但下載完成後會立即執行（可能會暫停 HTML 解析）。
- 多個 async 腳本的執行順序無法保證，取決於哪個腳本先下載完成。
- 只能用於外部腳本 (<script src="..." async></script>)，不能用於內聯腳本。
適合情境：當 JavaScript 不依賴 DOM 結構，也不需要與其他腳本保持執行順序時（例如，載入廣告、分析工具、第三方 API）。

```html
<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <title>Async Example</title>
    <script src="analytics.js" async></script>
</head>
<body>
    <h1>Hello, world!</h1>
</body>
</html>
```
`這個例子中，analytics.js（例如 Google Analytics 之類的腳本）會在下載後立即執行，而不會等待 HTML 完全解析。`  

3. When to use these 2 attributes? Could you give us code examples to illustrate the use cases for these 2 attributes?  
>`何時使用這兩個屬性？使用場景與代碼示例`

| 屬性 | 何時使用 | 影響 |
| :---:|:---:|:---:|
| defer | 當腳本需要操作 DOM，並且與其他腳本有順序依賴時 |確保 HTML 解析完成後才執行，且保持執行順序|
| async  | 當腳本不依賴 DOM，也不需要與其他腳本保持順序時 | 下載完成後立即執行，可能影響 HTML 解析 |

### 總結
* 使用 defer：

適合需要操作 DOM 的腳本，如頁面初始化、UI 交互功能。
確保 HTML 解析完畢後執行，並保持執行順序。

* 使用 async：

適合不依賴 DOM 或執行順序的腳本，如廣告、分析工具、第三方 SDK。
下載後立即執行，順序不確定。

選擇哪個屬性取決於腳本是否依賴 DOM 和其他腳本的執行順序。
___

# Topic 2
**CSS Selector Naming**

* OOCSS, SMACSS, and BEM are 3 common naming guidelines for CSS Selector. These
guidelines help us write more readable CSS code.
>`在 CSS 開發中，為了提高可讀性、可維護性，開發者通常會遵循一些命名規範。OOCSS、SMACSS 和 BEM 是三種常見的 CSS 命名方法，幫助我們更有條理地編寫樣式。`


Follow learning steps below to prepare your report:

1. Introduce the concepts of OOCSS, SMACSS, and BEM naming guidelines.
* OOCSS（物件導向 CSS，Object-Oriented CSS）  
>`OOCSS（物件導向 CSS）是一種將 CSS 組織成可重用組件的命名方式。它的核心思想是分離結構（Structure）與外觀（Skin），這樣可以減少重複代碼並提高可維護性。`

* 主要原則：

    1. 分離結構與外觀：
        結構（Structure）：負責元素的基本佈局，例如 width、margin、padding 等。
        外觀（Skin）：負責元素的視覺風格，如 background-color、border、box-shadow 等。
    2. 使用可重用的類別：
        例如，使用 .btn 定義按鈕的結構，使用 .btn-primary、.btn-secondary 來定義不同的樣式，而不是為每個按鈕單獨寫樣式。
```css
/* 結構 (Structure) */
.btn {
    display: inline-block;
    padding: 10px 20px;
    border-radius: 5px;
    text-align: center;
}

/* 外觀 (Skin) */
.btn-primary {
    background-color: blue;
    color: white;
}

.btn-secondary {
    background-color: gray;
    color: white;
}

```

* SMACSS（可擴展與模組化 CSS，Scalable and Modular Architecture for CSS）  
>`SMACSS 是一種將 CSS 分類為不同類別的架構，幫助我們組織 CSS，使其更容易擴展和維護。`
* 主要類別：
    1. Base（基礎樣式）：設定標籤的基本樣式，例如 body、h1、a 等。
    2. Layout（佈局樣式）：控制頁面區塊的佈局，例如 header、footer、sidebar。
    3. Module（模組樣式）：可重用的 UI 元件，如按鈕、卡片、導航欄等。
    4. State（狀態樣式）：描述元素的狀態，例如 .is-active、.is-hidden。
    5. Theme（主題樣式）（可選）：用於定義不同的主題樣式，如 .theme-dark、.theme-light。
```css
/* Base 樣式 */
body {
    font-family: Arial, sans-serif;
}

/* Layout 佈局 */
.l-header {
    background-color: #333;
    color: white;
    padding: 10px;
}

/* Module 模組 */
.card {
    border: 1px solid #ddd;
    padding: 15px;
    border-radius: 5px;
}

/* State 狀態 */
.is-active {
    background-color: yellow;
}
```

* BEM（區塊-元素-修飾符，Block-Element-Modifier）  
>`BEM 是一種基於組件的命名規範，通過「區塊（Block）、元素（Element）、修飾符（Modifier）」的方式組織 CSS 代碼，使其更直觀可讀。`
* 命名規則：
    1. Block（區塊）：代表獨立的組件，如 .menu、.button。
    2. Element（元素）：區塊內的子元素，使用 __ 連接，如 .menu__item、.button__icon。
    3. Modifier（修飾符）：用於改變區塊或元素的樣式，使用 -- 連接，如 .button--large、.menu__item--active。
```css
/* Block 區塊 */
.card {
    border: 1px solid #ddd;
    padding: 15px;
    border-radius: 5px;
}

/* Element 元素 */
.card__title {
    font-size: 18px;
    font-weight: bold;
}

.card__content {
    font-size: 14px;
}

/* Modifier 修飾符 */
.card--highlight {
    background-color: yellow;
}

```

2. Tell us which naming guideline is your favorite, and give an example to demonstrate the main concept of that guideline. 
For example, you can demo how to apply the OOCSS naming guideline to the CSS code in our week 1 tasks.    
>`我最喜歡 BEM，因為它的結構清晰，而且適用於現代前端框架（如 React、Vue）。BEM 讓我們更容易理解組件的組成，並且能夠很好地管理大型專案中的 CSS。`

## 總結
| 命名方式 | 主要概念 | 適用場景 |
| :---:|:---:|:---:|
| OOCSS | 分離結構與外觀 |可重用 UI 元件，如按鈕、表單|
| SMACSS | 將 CSS 分成 Base、Layout、Module、State、Theme | 大型專案，適合多人協作 |
| BEM | Block、Element、Modifier 結構化命名 | 現代前端開發，如 React、Vue |

📌 如果專案是大型企業網站，推薦使用 SMACSS。  
📌 如果正在開發前端框架（如 React/Vue）中的組件，推薦使用 BEM。  
📌 如果希望寫出可重用的 UI 樣式，推薦使用 OOCSS。

# Topic 3
**Fetch and CORS**

* Using built-in JavaScript fetch function, we can send HTTP requests to the back-end and get HTTP responses without refreshing or redirecting the page. Cross Origin Resource Sharing (CORS) concept plays a critical role if we want to send a request to a different domain with the fetch function.  
>`使用 JavaScript 內建的 fetch 函式，我們可以向後端發送 HTTP 請求，並在不重新整理或跳轉頁面的情況下獲取 HTTP 回應。當我們希望使用 fetch 來向不同網域發送請求時，「跨來源資源共享」（Cross-Origin Resource Sharing，CORS）的概念就變得非常重要。`

Follow learning steps below to prepare your report:

1. What is CORS?   
>`CORS（跨來源資源共享）是一種網頁安全機制，允許瀏覽器向不同來源（不同網域、子網域、通訊協定或連接埠）請求資源。瀏覽器會根據伺服器的回應標頭（Access-Control-Allow-Origin）來決定是否允許請求成功。`  
>`預設情況下，為了安全性，瀏覽器會限制來自不同來源的 JavaScript 直接存取其他網域的資源。CORS 允許伺服器設定特定的允許來源，從而開放 API 供其他網域存取。`
2. Can we use the fetch function in our localhost page, to send a request to https://www.google.com/ and get a response?
>`我們可以在本機端的網頁使用 fetch 函式，向 https://www.google.com/ 發送請求並獲取回應嗎？`  
>`不行，Google 並未開放 CORS 訪問，因此當我們在本機端使用 fetch 發送請求時，瀏覽器會攔截該請求，並顯示 CORS 錯誤訊息。`
```javascript
fetch("https://www.google.com/")
  .then(response => response.text())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```  
>`瀏覽器控制台會出現 CORS policy 錯誤，因為 Google 的伺服器並未允許來自我們本機的請求。`

3. Can we use the fetch function in our localhost page, to send a request to https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json and get a response? Compared to the previous case, what’s the difference?  
>`我們可以在本機端的網頁使用 fetch 函式，向上述網址發送請求並獲取回應嗎？與前一個案例相比，有什麼不同？`  
>`可以。
該 URL 屬於 GitHub Pages，並且其伺服器設定了允許跨域存取（CORS headers），所以我們可以成功獲取 JSON 資料。`
```javascript
fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json")
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```  
>`與 Google 的情況不同，這個 API 伺服器有設定 Access-Control-Allow-Origin: *，允許來自任何網域的請求，因此我們能成功獲取回應。`
4. How to share APIs we developed to other domains, just like what we experienced in
step 3. Could you give us an example?
>`如何讓我們開發的 API 允許其他網域存取？請舉例說明。`  
>`如果我們想要讓自己開發的 API 能夠讓其他網域存取（如 GitHub Pages），我們需要在後端的 HTTP 回應標頭中加入 CORS 設定。`  
>`在 FastAPI 中可以這樣做`
```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 設定 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允許所有網域訪問（可以改為指定的網域，如 ["https://example.com"]）
    allow_credentials=True,
    allow_methods=["*"],  # 允許所有 HTTP 方法
    allow_headers=["*"],  # 允許所有標頭
)

@app.get("/data")
async def get_data():
    return {"message": "這是開放給其他網域的 API 資料"}
```
>`這樣，當其他網域的前端使用 fetch 發送請求時，就可以成功獲取資料，而不會遇到 CORS 限制。`

___

# Task 4
**Connection Pool**

* The standard procedure to work with databases is: connect, execute SQL statements, and finally close the connection. Connection Pool is a programming technique to make the connection between back-end system and database more stable, and increase overall throughput.

Follow learning steps below to prepare your report:

* 在與資料庫進行交互時，標準程序通常是：
    1. 連接資料庫（connect）
    2. 執行 SQL 語句（execute）
    3. 關閉連接（close）  
#### 然而，每次請求都建立與關閉連線會帶來額外的開銷，影響系統效能。
1. What is Connection Pool? Why do we want to use Connection Pool?  
>`是一種用來管理資料庫連線的技術，它透過維持一組可重複使用的連線來優化效能，避免頻繁建立與關閉連線的成本。`
* 使用連線池的優勢：
    1.提高效能：重複使用連線，減少建立連線的時間。  
    2.減少資源消耗：降低資料庫伺服器的負擔，減少連線管理的開銷。  
    3.增加系統穩定性：避免大量即時連線導致資料庫崩潰或資源耗盡。  
    4.提高併發能力：允許多個請求共用同一組連線，提高吞吐量。  
2. How to create a Connection Pool by the official mysql-connector-python package?

3. If we want to make database operations, we get a connection from Connection Pool, execute SQL statements, and finally return connection back to the Connection Pool.Demo your code which implements the above procedure.
___

# Task 5
**Cross-Site Scripting (XSS)**

* Cross-Site Scripting (XSS) is one of the most common attack methods. Try to study the basic concept, replicate the attack steps, and tell us how to prevent this kind of attack from the developer’s view.

Follow learning steps below to prepare your report:
1. What is XSS?

2. You are a hacker! Design and do a real XSS attack on a web system. Show us your work.

3. Based on the scenario you did in the previous step, how could it be prevented?



