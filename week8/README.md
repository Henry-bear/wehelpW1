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
OOCSS（物件導向 CSS）是一種將 CSS 組織成可重用組件的命名方式。它的核心思想是分離結構（Structure）與外觀（Skin），這樣可以減少重複代碼並提高可維護性。

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
SMACSS 是一種將 CSS 分類為不同類別的架構，幫助我們組織 CSS，使其更容易擴展和維護。
* 主要類別：
    1. Base（基礎樣式）：設定標籤的基本樣式，例如 body、h1、a 等。
    2. Layout（佈局樣式）：控制頁面區塊的佈局，例如 header、footer、sidebar。
    3. Module（模組樣式）：可重用的 UI 元件，如按鈕、卡片、導航欄等。
    4. State（狀態樣式）：描述元素的狀態，例如 .is-active、.is-hidden。
    5. Theme（主題樣式）（可選）：用於定義不同的主題樣式，如 .theme-dark、.theme-light。
* BEM（區塊-元素-修飾符，Block-Element-Modifier）
2. Tell us which naming guideline is your favorite, and give an example to demonstrate the main concept of that guideline. 
For example, you can demo how to apply the OOCSS naming guideline to the CSS code in our week 1 tasks.



# Topic 3
**Fetch and CORS**

* Using built-in JavaScript fetch function, we can send HTTP requests to the back-end and get HTTP responses without refreshing or redirecting the page. Cross Origin Resource Sharing (CORS) concept plays a critical role if we want to send a request to a different domain with the fetch function.

Follow learning steps below to prepare your report:

1. What is CORS?

2. Can we use the fetch function in our localhost page, to send a request to https://www.google.com/ and get a response?

3. Can we use the fetch function in our localhost page, to send a request to https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json and get a response? Compared to the previous case, what’s the difference?

4. How to share APIs we developed to other domains, just like what we experienced in
step 3. Could you give us an example?

___

# Task 4
**Connection Pool**

* The standard procedure to work with databases is: connect, execute SQL statements, and finally close the connection. Connection Pool is a programming technique to make the connection between back-end system and database more stable, and increase overall throughput.

Follow learning steps below to prepare your report:

1. What is Connection Pool? Why do we want to use Connection Pool?

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



