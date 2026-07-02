# -*- coding: utf-8 -*-
import os
import re
import shutil

# 定義路徑
output_singles = r"c:\Users\leots\OneDrive\Desktop\Antigravity2.20260626\YouTube學習筆記特助\output\PAPAYA 電腦教室"
output_playlist = os.path.join(output_singles, "網頁 & 架站 & 開發")

obsidian_singles = r"C:\Users\leots\OneDrive\文件\Secondbrain\YouTube學習筆記\PAPAYA 電腦教室"
obsidian_playlist = os.path.join(obsidian_singles, "網頁 & 架站 & 開發")

# 1. 建立目錄
os.makedirs(output_singles, exist_ok=True)
os.makedirs(output_playlist, exist_ok=True)
os.makedirs(obsidian_singles, exist_ok=True)
os.makedirs(obsidian_playlist, exist_ok=True)

# 2. 定義播放清單影片 (重排為最合邏輯的學習順序：HTML/CSS -> JS -> Git -> SQL -> Figma -> Google Sites -> Wix -> WordPress 01-04)
playlist_videos = [
    {
        "index": 1,
        "id": "6HHN0G2cwBM",
        "title": "成為網頁設計師的第一步！快速上手 HTML & CSS 展開你的網頁設計之旅！",
        "filename": "EP01_成為網頁設計師的第一步！快速上手 HTML & CSS 展開你的網頁設計之旅！.md",
        "content_func": lambda: """## 🧠 核心概念與技術摘要
1. **HTML & CSS 基礎網頁結構**：
   * **HTML** 提供網頁的骨架與語意結構。`head` 標籤存放網頁中繼資料（如字元編碼、搜尋引擎優化資訊等）；`body` 標籤存放網頁可見內容。
   * **CSS** 提供網頁的視覺外觀、排版與樣式。透過選擇器（Selectors）來指定 HTML 標籤並套用樣式（如顏色、寬度、字型）。
2. **語意化標籤與結構設計**：
   * 使用 `section`、`div` 等標籤將網頁內容模組化與分類。
   * 合理使用語意化標籤有利於搜尋引擎優化 (SEO)，幫助搜尋蜘蛛理解網頁層級。
3. **邊距與排版控制（Padding & Margin）**：
   * **Padding (內邊距/內襯)**：元件內容與邊框之間的距離，例如加大訊息輸入欄的內邊距以提升點擊與閱讀舒適度。
   * **Margin (外邊距)**：元件邊框與其他元件之間的外部距離。
   * **置中對齊**：使用 `text-align: center` 進行文字水平置中；使用 `margin: 0 auto` 來使區塊級容器水平置中。
4. **自適應與欄位佈局**：
   * 將寬度設成 `100%` 以適應瀏覽器視窗寬度。
   * 透過建立多個 `div`（如寬度 300 像素的卡片），結合 Flexbox/Grid 進行網頁多欄位並排佈局。
   * 表單元素美化：調整輸入框（input）、文本域（textarea）的 Placeholder 提示文字色彩、邊框與間距。

## ⏱️ 附時間戳記的段落大綱
* `[00:02]` 網頁設計基本原理，HTML 與 CSS 的分工角色。
* `[02:01]` 網頁 head 標籤的後台資訊與元數據（Metadata）設定。
* `[04:00]` body 標籤與一般文書處理概念的對應關係。
* `[06:01]` 在 VS Code 中建立專案資料夾、檔案組織與 HTML/CSS 檔案關聯。
* `[08:00]` CSS 基礎選取器語法：如何針對特定標籤套用視覺樣式。
* `[10:01]` 使用 section 標籤將網頁文章內容進行區塊化與結構分類。
* `[12:00]` 調整內邊距（Padding）與外邊距（Margin）以優化文字排版間距。
* `[14:00]` 設定寬度為 100% 的滿版自適應容器設計。
* `[16:00]` 利用 HTML5 結構標籤優化搜尋引擎 (SEO) 指引。
* `[18:01]` 文字置中對齊與區塊級元件水平置中技巧（margin: auto）。
* `[20:01]` 調配文字顏色與背景的視覺對比度，優化視覺層級。
* `[22:01]` 多欄式卡片佈局：設定多個 300 像素 div 區塊的並排。
* `[24:01]` 表單欄位提示文字（Placeholder）與邊框樣式自訂。
* `[26:00]` 互動按鈕的 CSS 懸停（Hover）狀態與漸變設定。
* `[28:01]` 留言訊息欄（Textarea）的上下內邊距加寬美化。

## 🌐 中英專有名詞對照表
* **HTML / CSS**：超文字標記語言 / 層疊樣式表
* **Metadata**：中繼資料 / 後台元數據
* **Padding / Margin**：內邊距 / 外邊距
* **Selectors**：選擇器
* **SEO (Search Engine Optimization)**：搜尋引擎優化
* **Placeholder**：佔位提示文字
* **Hover State**：懸停狀態

## 🏃‍♂️ 行動指南
* 在本地建立一個 `index.html` 與 `style.css`，並將二者連結。
* 撰寫一個 300px 寬度的產品卡片 div，為其設定 `padding`、`margin` 與 `border-radius`，並在滑鼠懸停時改變背景色。
* 思考：在網頁設計中，`padding` 與 `margin` 對於元素點擊範圍的影響有何不同？
"""
    },
    {
        "index": 2,
        "id": "0FLkwZ-PH2I",
        "title": "JavaScript 快速上手！用一個實戰範例迅速掌握所有重點語法！#網頁開發必學",
        "filename": "EP02_JavaScript 快速上手！用一個實戰範例迅速掌握所有重點語法！.md",
        "content_func": lambda: """## 🧠 核心概念與技術摘要
1. **JavaScript 在網頁中的定位**：
   * HTML 提供結構，CSS 提供樣式，JavaScript 則負責「互動邏輯與網頁動態行為」。
   * **引入方式**：可以直接寫在 HTML 內（較不推薦，可能阻塞網頁讀取與渲染），或寫在外部 `.js` 檔案中，並在 HTML 中導入。
2. **基本語法與資料結構**：
   * **變數 (Variables)**：用於暫存數據。其數值是可以動態更新的。
   * **資料類型 (Data Types)**：包括字串 (Strings)、數字 (Numbers) 與布林值 (Booleans)。
   * **字串操作 (String Manipulation)**：可以擷取特定範圍的字串，指定起始與結束位置。
   * **陣列 (Arrays)**：以中括號包裝的清單，索引值從 0 開始（0-indexed）。
3. **流程控制與函數**：
   * **條件判斷 (if-else)**：在圓括號內寫入判斷條件，符合條件時執行對應區塊。
   * **函數 (Functions)**：將重複使用的邏輯包裝起來，傳入參數並回傳結果。
4. **DOM 操作與事件監聽**：
   * **DOM 選擇**：為 HTML 元件添加 class 類別，在 JS 中選取該元件。
   * **事件監聽 (Event Listener)**：使用 `addEventListener` 監測用戶行為（如點擊事件 `click`）。當用戶點擊時，動態更改網頁样式（例如將文字顏色改為淺灰、新增/移除 class 等）。

## ⏱️ 附時間戳記的段落大綱
* `[00:02]` JavaScript 基礎介紹及其在前端網頁中的重要性。
* `[02:03]` 內聯 JS 的缺點：可能導致 HTML 渲染阻塞與頁面讀取變慢。
* `[04:02]` 變數宣告與數值重新指派（Updating values）。
* `[06:02]` 基礎資料類型分析（字串、數字、布林值）。
* `[08:01]` 字串常用方法示範：動態剪裁與擷取特定區段字元。
* `[10:00]` if-else 條件判斷式：圓括號內的邏輯運算與大括號的執行範疇。
* `[12:01]` 陣列 (Array) 的建立，以及如何透過索引 0 取得第一位學生的成績。
* `[14:03]` 函數 (Function) 的定義、引數傳遞與 return 回傳值。
* `[16:02]` DOM 樹操作：使用 class 類別選取網頁元素（querySelector）。
* `[18:01]` 在瀏覽器開發者工具（Console）中進行 JS 測試與調試。
* `[20:01]` 新增事件偵測器（addEventListener）以監聽 click 點擊動作。
* `[22:00]` 事件觸發後的 DOM 样式修改：文字顏色動態變為淺灰。
* `[24:02]` 排版微調：設定元素左、右為 15 像素的邊框間距。

## 🌐 中英專有名詞對照表
* **DOM (Document Object Model)**：文件物件模型
* **Variables**：變數
* **Data Types**：資料類型
* **Arrays**：陣列 / 數組
* **Conditional Statements**：條件判斷式
* **Functions**：函數
* **Event Listener**：事件監聽器 (如 click)

## 🏃‍♂️ 行動指南
* 撰寫一個 JavaScript 函數，傳入一個攝氏溫度，回傳其華氏溫度值。
* 實作一個按鈕點擊事件：當使用者點擊按鈕時，動態將一個 `div` 的背景色彩在紅色與藍色之間切換（使用 `classList.toggle`）。
* 思考：為什麼在 HTML 中，通常會把 `<script>` 標籤放在 `<body>` 的最底部？
"""
    },
    {
        "index": 3,
        "id": "FKXRiAiQFiY",
        "title": "程式與網頁開發者必備技能！Git 和 GitHub 零基礎快速上手，輕鬆掌握版本控制的要訣！",
        "filename": "EP03_Git 和 GitHub 零基礎快速上手，輕鬆掌握版本控制的要訣！.md",
        "content_func": lambda: """## 🧠 核心概念與技術摘要
1. **版本控制與 Git 概述**：
   * Git 是一個分散式的版本控制系統，用來追蹤檔案的修改歷史，防止代碼遺失。
   * **基本配置**：在使用 Git 之前，必須先設定使用者的姓名與 Email 作為認證簽名。
2. **Git 工作流與基礎指令**：
   * **git init**：初始化一個本地 Git 儲存庫（建立隱藏的 `.git` 資料夾）。
   * **git add (暫存)**：將檔案納入版本管理暫存區。可以使用通配符（如 `*.md` 代表所有 Markdown 檔案）。
   * **git commit (提交)**：為檔案建立一個「版本快照」，必須附帶有意義的說明文字（如 `git commit -m "feat: init project"`）。
   * **git log (日誌)**：查看過去的所有提交歷史。
3. **檔案異動與分支管理**：
   * **刪除檔案**：在 Git 中刪除檔案同樣會被記錄為一個版本歷史異動。
   * **分支 (Branching)**：建立獨立的分支（如 `git branch feature`）可以讓開發者在不破壞主分支（master/main）的前提下，安全地測試新功能。
4. **GitHub 雲端託管**：
   * GitHub 是 Git 儲存庫的雲端託管平台。可以將本地代碼推送（Push）至雲端，實現多人協作與備份。

## ⏱️ 附時間戳記的段落大綱
* `[00:02]` 版本控制系統的重要性，Git 與 GitHub 的角色差異。
* `[02:03]` Git 初始化設定：設定全局使用者名稱（user.name）與信箱（user.email）。
* `[04:01]` 建立本地儲存庫（git init）與暫存區域（git add）的使用。
* `[06:00]` 通配符應用：一次將目錄下所有副檔名為 .md 的檔案加到暫存區。
* `[08:00]` 將暫存區檔案提交（git commit -m）以建立版本歷史快照。
* `[10:01]` 在 Git 中追蹤檔案的刪除操作，並將其提交至版本歷史。
* `[12:00]` 檔案異動對比與 Git 快照紀錄的底層運作概念。
* `[14:00]` 分支（Branching）技術：如何建立與切換分支以進行隔離開發。

## 🌐 中英專有名詞對照表
* **Version Control System (VCS)**：版本控制系統
* **Git Repository**：Git 儲存庫
* **Staging Area**：暫存區
* **Commit**：提交 / 快照
* **Branching**：分支管理
* **GitHub**：Git 代碼託管雲端平台

## 🏃‍♂️ 行動指南
* 在本地電腦初始化一個 Git 儲存庫，新增一個 `README.md` 檔案，將其暫存並提交，最後使用 `git log` 查看提交歷史。
* 建立一個名為 `dev` 的新分支，切換過去，修改檔案後提交，再切換回 `main` 分支，觀察檔案內容的變化。
* 思考：`.gitignore` 檔案的作用是什麼？在我們的專案中，有哪些檔案應該被列入 `.gitignore`？
"""
    },
    {
        "index": 4,
        "id": "G_zGBR0mQmE",
        "title": "SQL 十四分鐘速成班！沒錯不要懷疑，資料庫語法比中午決定吃什麼還要簡單！",
        "filename": "EP04_SQL 十四分鐘速成班！資料庫語法速成教學.md",
        "content_func": lambda: """## 🧠 核心概念與技術摘要
1. **關聯式資料庫與 SQL 語言**：
   * 資料庫是用來結構化儲存大量資料的系統。SQL (Structured Query Language) 是用來與資料庫進行溝通的標準語言。
2. **基礎查詢語法**：
   * **SELECT & FROM**：指定要讀取的欄位與資料表。
   * **WHERE**：設定篩選條件（例如只篩選特定部門或成績大於某數值的記錄）。
   * **ORDER BY**：針對一個或多個欄位進行排序（升冪 ASC 或降冪 DESC）。
3. **進階關聯查詢 (JOIN)**：
   * 用來合併多個資料表。例如當學生的資料存在甲表，而其加入的社團名稱存在乙表時，利用 `JOIN` 可以透過共通的「學生 ID」欄位將兩表關聯起來，同時查詢出學生姓名與其社團名稱。
4. **資料更新與安全防護 (UPDATE)**：
   * **UPDATE**：修改現有的資料庫記錄。
   * ⚠️ **重要安全守則**：執行 `UPDATE` 時，**後面務必使用 WHERE 語法限制更新範圍**。若遺漏 `WHERE`，將導致整張資料表的所有記錄被全部覆蓋，造成毀滅性的資料損毀。

## ⏱️ 附時間戳記的段落大綱
* `[00:03]` 資料庫基本架構介紹，SQL 語法基礎概念。
* `[02:01]` SELECT（選擇欄位）與 FROM（指定資料表）的基本查詢語法。
* `[04:01]` ORDER BY 排序語法示範，單一欄位與多欄位複合排序。
* `[06:02]` WHERE 篩選子句：條件運算子與文字/數字資料篩選。
* `[08:00]` 複合查詢：同時結合 WHERE 篩選與 ORDER BY 排序輸出。
* `[10:01]` 多表合併（JOIN）原理：如何連結學生表與社團表。
* `[12:01]` UPDATE 修改數據語法，以及遺漏 WHERE 導致全表被蓋掉的災難演示。

## 🌐 中英專有名詞對照表
* **Relational Database**：關聯式資料庫
* **SQL (Structured Query Language)**：結構化查詢語言
* **SELECT / FROM / WHERE**：查詢 / 來源 / 篩選條件
* **ORDER BY**：排序子句
* **JOIN**：資料表關聯合併
* **UPDATE**：資料更新指令

## 🏃‍♂️ 行動指南
* 撰寫一個 SQL 語法：從 `employees` 資料表中，查詢所有部門為 `Sales` 且薪資大於 `50000` 的員工姓名，並按入職日期降冪排序。
* 說明 `INNER JOIN` 與 `LEFT JOIN` 的根本差異。
* 思考：在實際的企業資料庫中，為了防止執行 `UPDATE` 時遺漏 `WHERE` 造成災難，有哪些安全管理機制（如 Transaction、權限管控）可以採用？
"""
    },
    {
        "index": 5,
        "id": "NBxYW9CmpIM",
        "title": "WordPress 從零開始輕鬆架站！#01 [個人部落格/電子商務/企業網站]開張大吉！",
        "filename": "EP05_WordPress 從零開始輕鬆架站！#01 網站開張大吉！.md",
        "content_func": lambda: """## 🧠 核心概念與技術摘要
1. **WordPress (WP) 簡介與主機架設**：
   * WordPress 是全球市場佔有率最高的內容管理系統 (CMS)，適合建立部落格、企業網站與電商平台。
   * 自架站需要一個虛擬主機（如 Hostinger 提供的服務）。
2. **初始化配置與核心更新**：
   * 進入 WP 後台，首先確定網站的建立目的與目標群眾。
   * 確保 WordPress 核心程式、佈景主題與外掛（Plugins）均更新至最新版本，以維護系統安全性。
3. **外掛（Plugins）的管理與安裝**：
   * 外掛是擴充 WordPress 功能的關鍵。例如安裝並啟用 `Hostinger` 設定精靈外掛，能一鍵優化後台環境並進行基本排版配置。
4. **內容發布（文章與引用）**：
   * 建立並編輯文章，設定分類與標籤。
   * 在文章中插入外部連結、引用（Citations）與圖片，符合現代網頁豐富媒體的標準。

## ⏱️ 附時間戳記的段落大綱
* `[00:03]` WordPress 系統架構說明，自建網站與虛擬主機 Hostinger 設定入門。
* `[02:04]` 後台初始化嚮導：選擇網站目的、風格與目標受眾設定。
* `[04:01]` WordPress 系統核心、語系與外掛安全更新機制說明。
* `[06:03]` 搜尋、安裝與啟用 WP 實用外掛程式。
* `[08:00]` 執行 Hostinger 設定精靈以自動佈置網站基本結構。
* `[10:02]` 文章編輯器操作：發布首篇部落格文章、設定圖片與引用格式。
* `[12:01]` 內容管理系統 (CMS) 優勢總結與自行架站的擴充潛力。

## 🌐 中英專有名詞對照表
* **CMS (Content Management System)**：內容管理系統
* **Plugins**：外掛程式
* **Dashboard**：後台控制面板
* **Citations**：引用 / 參照
* **Self-hosting**：自主架站 / 虛擬主機託管

## 🏃‍♂️ 行動指南
* 註冊一個本地測試用的 WordPress（如使用 LocalWP 軟體），並熟悉 WP 後台控制台的各項選單。
* 安裝一個名為 `Classic Editor` 或使用預設 `Gutenberg` 編輯器，發布一篇測試文章。
* 思考：WordPress.org (自架版) 與 WordPress.com (託管版) 有何區別？為什麼多數企業選擇自架版？
"""
    },
    {
        "index": 6,
        "id": "hVqXspRfuqw",
        "title": "WordPress 從零開始輕鬆架站！#02 網頁版型設計/佈景主題/自訂頁首頁尾",
        "filename": "EP06_WordPress 從零開始輕鬆架站！#02 網頁版型設計與自訂頁首頁尾.md",
        "content_func": lambda: """## 🧠 核心概念與技術摘要
1. **網頁視覺設計與版型建構**：
   * 利用頁面編輯器（Page Builder）進行網頁版面設計。
   * 透過側邊欄工具載入圖片、文字區塊與調整排版結構（例如載入盆栽圖像範例）。
2. **佈景主題（Theme）的選擇與導入**：
   * 推薦使用輕量、相容性高的 **Astra 佈景主題**。
   * Astra 提供豐富的預建模板（Starter Templates），可一鍵導入精美的網頁樣式與結構。
3. **頁首與頁尾的自訂 (Header & Footer)**：
   * **頁首**：設定 Logo、導覽選單（Navigation Menu）與全域設定。
   * **頁尾**：加入聯絡資訊、版權聲明與快速連結。適當的頁尾設計能有效區隔主內容，增加專業感。
4. **佈局邊距調整 (Margin & Padding)**：
   * 調整 Container（容器）的 Padding 與 Margin，為文字與圖片留下足夠的「留白（Whitespace）」，提升網頁的可讀性與高級感。
   * 調整邊框間距與欄位寬度比例。

## ⏱️ 附時間戳記的段落大綱
* `[00:03]` 網頁排版設計概念：如何挑選與設定全域網頁視覺風格。
* `[02:01]` 使用區塊編輯器新增圖片元件與媒體庫管理。
* `[04:02]` 在頁面中擺放客製化宣傳圖（以盆栽照片為例）的排版技巧。
* `[06:00]` 安裝並啟用 Astra 佈景主題，一鍵導入專業 Starter Templates。
* `[08:00]` 小工具（Widgets）設定：在側邊欄或頁尾加入動態區塊。
* `[10:02]` 調整 Containers（容器）邊框外距與內距以優化閱讀間距。
* `[12:02]` 自訂控制面板：管理全域顏色、字型樣式與按鈕設計。
* `[14:03]` 設計網站頁尾（Footer）：建立版權說明與區隔版面。

## 🌐 中英專有名詞對照表
* **Astra Theme**：Astra 佈景主題
* **Header / Footer**：頁首 / 頁尾
* **Container**：版面容器
* **Margin / Padding**：外邊距 / 內邊距
* **Whitespace**：留白設計
* **Widgets**：小工具 / 側邊欄元件

## 🏃‍♂️ 行動指南
* 在你的測試 WP 網站上安裝 Astra 主題，並試著導入一個免費的電商或個人模板。
* 利用自訂功能（Customizer），修改全域的按鈕色彩，並將預設字體改為微軟正黑體或 Google Fonts。
* 思考：網頁設計中的「留白（Whitespace）」為什麼對使用者體驗有決定性的影響？
"""
    },
    {
        "index": 7,
        "id": "V4SaluYRm98",
        "title": "WordPress 從零開始輕鬆架站！#03 自訂客服表單/商品新增與管理",
        "filename": "EP07_WordPress 從零開始輕鬆架站！#03 自訂客服表單與商品管理.md",
        "content_func": lambda: """## 🧠 核心概念與技術摘要
1. **自訂客服表單 (Contact Form)**：
   * 使用聯絡表單外掛建立表單（例如命名為「訪客留言」），包含姓名、Email、主旨與內容欄位，並將表單代碼嵌入到聯絡我們頁面。
2. **WooCommerce 商品新增與管理**：
   * **WooCommerce** 是 WordPress 的官方電商系統外掛。
   * **實體商品**：新增商品名稱、設定定價與促銷價、上傳商品精選圖片（Cover Photo，顧客搜尋時看到的第一張圖）與多角度畫廊圖片（Gallery）。
   * **商品變體 (Product Variations)**：根據顏色（Color）、尺寸等屬性，為同一件商品建立不同的選購規格。
3. **虛擬與數位商品設定**：
   * 支援新增「虛擬（Virtual）」與「可下載（Downloadable）」商品，適用於電子書、數位檔案、線上課程或會員資格等。
4. **優惠券系統 (Coupons)**：
   * 建立折價券，可設定定額折扣、百分比折扣、使用期限與每人使用上限，提升行銷轉化率。

## ⏱️ 附時間戳記的段落大綱
* `[00:03]` 客服與電商功能整合概覽，表單外掛的安裝。
* `[02:04]` 設計並命名「訪客留言」聯絡表單，將其插入網頁實體區塊。
* `[04:03]` 新增 WooCommerce 產品，設定主商品封面圖與多圖畫廊（Gallery）。
* `[06:01]` 設定多規格變體商品：利用色彩（Color）屬性建立選單。
* `[08:00]` 設定非實體商品：數位課程與虛擬電子檔案的下載權限配置。
* `[10:01]` 行銷優惠券（Coupons）的新增、額度折扣與條件限制設定。

## 🌐 中英專有名詞對照表
* **WooCommerce**：WordPress 官方電商外掛
* **Contact Form**：聯絡表單
* **Product Gallery**：商品圖片藝廊
* **Product Variations**：商品變體 / 多規格商品
* **Virtual / Downloadable**：虛擬商品 / 可下載商品
* **Coupon Codes**：優惠券代碼

## 🏃‍♂️ 行動指南
* 安裝 WooCommerce 外掛，新增一個名為「精美馬克杯」的實體商品，並為其設定「紅色」與「藍色」兩種變體規格，價格不同。
* 建立一張「九折（10% Off）」優惠券，限制最低消費金額為 500 元。
* 思考：數位商品（Downloadable）在防盜鏈與下載期限上，應該做哪些安全設定？
"""
    },
    {
        "index": 8,
        "id": "SrrjY1gq27I",
        "title": "WordPress 從零開始輕鬆架站！#04 金流與物流設定/Email確認信發送",
        "filename": "EP08_WordPress 從零開始輕鬆架站！#04 金物流與Email設定.md",
        "content_func": lambda: """## 🧠 核心概念與技術摘要
1. **電商金流設定 (Payment Gateways)**：
   * 設定結帳付款管道（如綠界 ECpay、藍新或 Stripe、PayPal）。
   * 在測試階段，使用「沙盒測試模式（Sandbox）」，填入虛擬信用卡資訊來驗證交易流程是否暢通。
2. **電商物流設定 (Shipping Options)**：
   * 設定運費計算規則。可依據地區設定固定運費、滿額免運費、或整合超商取貨（7-11/全家店到店）物流介接。
3. **解決連線與安全性問題**：
   * 排除金物流介接時常見的 API 連線超時或 SSL 安全認證問題，確保交易過程符合加密規格。
4. **自動化 Email 通知與外掛啟用**：
   * 啟用相關外掛以實現「下單成功自動發送 Email 確認信」給顧客及管理員。
   * 配置 SMTP 外掛防止郵件被判定為垃圾郵件，確保確認信順利寄達。

## ⏱️ 附時間戳記的段落大綱
* `[00:03]` 金流與物流設定核心流程介紹。
* `[02:02]` 啟用測試模式（Sandbox），使用虛擬卡號進行結帳流程測試。
* `[04:01]` 排除物流與金流串接時常見的網路安全連線錯誤（SSL 錯誤）。
* `[06:00]` 安裝並設定發送通知外掛，自動化後台處理流程。
* `[08:00]` 配置 Email 範本與 SMTP，確保訂單確認信順利發送。

## 🌐 中英專有名詞對照表
* **Payment Gateway**：金流整合閘道 (如 ECpay)
* **Logistics / Shipping**：物流設定 / 運送規則
* **Sandbox Mode**：沙盒測試模式
* **SSL Certificate**：安全套接層憑證
* **SMTP (Simple Mail Transfer Protocol)**：簡單郵件傳輸協定
* **Order Confirmation Email**：訂單確認信

## 🏃‍♂️ 行動指南
* 在 WooCommerce 設定中，啟用「銀行轉帳」與「貨到付款」兩種基本付款方式。
* 設定物流規則：台灣本島固定運費 80 元，消費滿 1000 元免運費。
* 思考：為什麼在正式上線的電商網站中，安裝並設定「SMTP 外掛」是不可或缺的？
"""
    },
    {
        "index": 9,
        "id": "NrpnYQDQ5s4",
        "title": "史上最簡單「一頁式網站」建置工具！再配上專屬網址 🚀 能見度 500 英呎…800英呎愈衝愈高！ |  Google Sites 協作平台快速上手",
        "filename": "EP09_史上最簡單「一頁式網站」建置工具！Google Sites 協作平台快速上手.md",
        "content_func": lambda: """## 🧠 核心概念與技術摘要
1. **Google Sites 協作平台定位**：
   * 適合個人、學校或小企業的免費且極速的「一頁式網站（Landing Page）」建置工具。
   * **特色**：無須寫程式，完全拖曳排版，整合 Google Drive、地圖與行事曆。
2. **視覺設計與排版**：
   * 提供預建版面主題（Themes），支援拖曳調整元件大小與位置。
   * 可以插入自製的圖片（使用 Canva 或其他繪圖軟體製作的 Banner 橫幅）。
3. **嵌入實用工具**：
   * 嵌入 Google 地圖以顯示門市位置。
   * 加入帶有超連結的 Call-to-Action (CTA) 按鈕，引導客戶點擊前往表單或聯絡信箱。
4. **網域設定與協作權限**：
   * 支援多人共同編輯，可管理協作權限。
   * 可以綁定個人「專屬網址（Custom Domain）」，需要到網域註冊商（如 GoDaddy、Google Domains）後台新增 TXT 紀錄以完成網域所有權驗證。

## ⏱️ 附時間戳記的段落大綱
* `[00:02]` Google Sites 協作平台定位說明：極速一頁式網站開發。
* `[02:01]` 版面佈局、區塊結構與色彩主題的切換配置。
* `[04:00]` 結合外部繪圖軟體（如 Canva）生成網頁 Banner 與背景圖。
* `[06:00]` 使用右鍵與拖曳選單進行網頁內容元件重組。
* `[08:01]` 嵌入 Google Maps（地圖）標註店面地址，並設定資訊框。
* `[10:01]` 建立 Call-to-Action 按鈕並設定外部超連結。
* `[12:03]` 網站發布、權限管理與邀請團隊協作設定。
* `[14:00]` 綁定專屬頂級網域：說明 TXT 紀錄 DNS 所有權驗證流程。

## 🌐 中英專有名詞對照表
* **Google Sites**：Google 協作平台
* **One-page Website / Landing Page**：一頁式網站 / 落地頁
* **Call-to-Action (CTA) Button**：行動呼籲按鈕
* **Custom Domain**：客製化網址 / 專屬網域
* **DNS Verification / TXT Record**：DNS 驗證 / TXT 記錄
* **Collaborators**：協作者

## 🏃‍♂️ 行動指南
* 使用你的 Google 帳號建立一個 Google Sites，設計一個個人的作品集一頁式網站，包含自我介紹、地圖與聯絡按鈕。
* 說明如何利用 Google Sites 的「嵌入碼（Embed）」功能，放入一段自訂的 HTML 程式碼。
* 思考：Google Sites 與 WordPress 相比，其最大的優勢與劣勢分別是什麼？
"""
    },
    {
        "index": 10,
        "id": "P96TQwsY_VY",
        "title": "就是它以黑馬之姿擄獲了全球設計師的心！超人氣 UI 設計工具 Figma 快速上手！",
        "filename": "EP10_超人氣 UI 設計工具 Figma 快速上手！.md",
        "content_func": lambda: """## 🧠 核心概念與技術摘要
1. **Figma 軟體定位與優勢**：
   * Figma 是目前全球最熱門的 UI/UX 設計工具，採用雲端網頁版，支援多人即時協作。
   * 適合用來設計網頁原型（Web Prototypes）與 App 介面。
2. **畫布與網格對齊 (Frames & Grids)**：
   * 在畫布（Canvas）中建立 Frame（框架，如 Desktop 1920x1080 或 iPhone 尺寸）。
   * 啟用 Layout Grid（版面網格），使所有的文字、圖片、按鈕能精準貼齊網格邊緣，確保排版的對齊與一致性。
3. **元素繪製與文字編排**：
   * 繪製矩形、圓形等向量圖形，設定圓角與填色。
   * 設定文字大小、字重與行距。
   * **快捷鍵操作**：使用 `Alt` + 滑鼠拖曳，可以快速複製元件並保持水平/垂直對齊。
4. **簡單交互原型製作 (Prototyping)**：
   * 切換到 Prototype 標籤。
   * 設定連結節點，例如當使用者點擊「搜尋欄」時，觸發轉場動畫，顯示搜尋啟用狀態的 Frame。

## ⏱️ 附時間戳記的段落大綱
* `[00:00]` Figma 軟體優勢與 UI 設計流程基本介紹。
* `[02:00]` 向量形狀繪製、編輯與自訂圓角半徑（Corner Radius）。
* `[04:00]` 網頁字體與排版（Typography）設定要領。
* `[06:01]` 啟用與使用版面網格（Layout Grids）以保持視覺對齊。
* `[08:01]` 修改圖層名稱與文字標題，保持專案井然有序。
* `[10:01]` 組合圖層與元件（Group Selection）管理。
* `[12:01]` 快捷鍵操作：使用 Alt 鍵拖曳以極速複製與量測距離。
* `[14:01]` 切換 Prototyping 標籤設定點擊觸發轉場，模擬搜尋欄點擊狀態。

## 🌐 中英專有名詞對照表
* **Figma**：超人氣 UI 設計軟體
* **Frame / Canvas**：框架 / 畫布
* **Layout Grid**：版面網格
* **Corner Radius**：圓角半徑
* **Alt+Drag**：拖曳複製快捷鍵
* **Prototyping / Transition**：原型互動 / 轉場動畫

## 🏃‍♂️ 行動指南
* 下載並註冊 Figma 帳號，建立一個 Desktop 框架，畫出一個包含 Logo、導覽列與 Banner 的網頁首頁介面。
* 利用 `Alt` + 拖曳複製出三個相同的產品卡片，並測量它們彼此之間的間距是否均為 24 像素。
* 思考：Figma 中的「Auto Layout（自動佈局）」功能對於響應式網頁設計（RWD）有何重要性？
"""
    },
    {
        "index": 11,
        "id": "euKP5fg0f-8",
        "title": "如何使用 Wix 輕鬆製作個人網站 + 作品集？",
        "filename": "EP11_如何使用 Wix 輕鬆製作個人網站與作品集.md",
        "content_func": lambda: """## 🧠 核心概念與技術摘要
1. **Wix 網頁建置工具特性**：
   * Wix 是一款功能強大、自由度極高的「無代碼架站平台」，提供海量精美模板。
   * 極適合用來快速製作個人履歷（Resume）與設計/攝影作品集（Portfolio）網站。
2. **設計與轉場特效**：
   * 提供多種網頁區塊，可自訂背景影片或圖片。
   * 加入「向下滑動指引（Scroll Indicator）」，引導訪客繼續往下瀏覽。
   * 在自訂設計介面中，微調按鈕、文字框與全域樣式。
3. **動態內容管理與互動**：
   * 建立互動時間軸，只需編輯文字框中的年份與學經歷內容。
   * 新增訪客留言板（Guestbook），網站主可以直接在 Wix 後台查看留言並進行回覆。
4. **導覽功能與付費升級**：
   * 自訂頂部選單（Header Menu），設定點擊錨點（Anchors）跳轉到網頁特定位置。
   * 付費升級方案可以移除 Wix 廣告並綁定自訂的網域。

## ⏱️ 附時間戳記的段落大綱
* `[00:00]` Wix 平台優勢與個人履歷/作品集網站主題說明。
* `[02:00]` Wix 範本庫瀏覽，選擇適合作品集的版面配置。
* `[04:01]` 加入動態滾動按鈕與滑動指引標記（Scroll Indicator）。
* `[06:00]` 自訂設計後台：調整整體色彩、字體樣式與按鈕外觀。
* `[08:00]` 時間軸履歷編輯：修改年份文字框與經歷內容。
* `[10:00]` 訪客留言區（Guestbook）小工具整合與回信系統測試。
* `[12:00]` 設計導覽列，新增 HOME 與各分頁按鈕並連接錨點。
* `[14:00]` Wix Premium 方案：解鎖專屬網址與移除 Wix 商標廣告。

## 🌐 中英專有名詞對照表
* **Wix**：無代碼網頁架設平台
* **Portfolio / Resume**：作品集 / 個人履歷
* **Scroll Indicator**：滾動提示符
* **Anchors**：網頁定位錨點
* **Guestbook**：留言板
* **Wix Premium**：Wix 付費進階方案

## 🏃‍♂️ 行動指南
* 在 Wix 上建立一個免費網站，導入一個履歷模板，並嘗試將你的個人經歷與頭像更新上去。
* 設定一個選單錨點：點擊選單上的「聯絡我」後，畫面能平滑滾動到網頁底部的留言板。
* 思考：Wix 與 Google Sites 相比，在設計自由度與功能擴充性上有何差別？
"""
    }
]

# 3. 定義單一影片
single_videos = [
    {
        "id": "2pM-7fBXc_M",
        "title": "還在羨慕別人用 AI 開發酷產品？Claude Code 保姆級教學讓你輕鬆體驗 Vibe Coding, 動動嘴就能做出 Anything！",
        "filename": "Claude Code 快速上手與 Vibe Coding 實測.md",
        "content": """# 🎥 還在羨慕別人用 AI 開發酷產品？Claude Code 保姆級教學讓你輕鬆體驗 Vibe Coding, 動動嘴就能做出 Anything！

## 📌 影片資訊
* **影片 ID**：2pM-7fBXc_M
* **原始網址**：https://www.youtube.com/watch?v=2pM-7fBXc_M
* **講者**：PAPAYA 電腦教室
* **類別**：單一影片學習筆記
* **創作者**：PAPAYA 電腦教室

---

## 🧠 核心概念與技術摘要
1. **Claude Code 終端機開發工具**：
   * Claude Code 是 Anthropic 官方推出的命令列 AI 開發助理，能在終端機直接讀寫本機代碼、跑編譯命令及執行 shell 指令。
2. **Vibe Coding（動嘴開發模式）**：
   * 開發者只需用口語下指令（甚至結合語音輸入），AI 就會自動在本地環境撰寫程式、下載並安裝缺少的 Python/Node 依賴套件。
3. **規劃與反思機制（Plan & Refinement）**：
   * 在執行任務前，可以下指令請 Claude 規劃一份詳細的技術藍圖，讓開發者確認無誤後才批准執行（Always Proceed/Confirm）。
   * Claude 能在背景反思代碼執行錯誤，並自動修正 bug 直至跑通。
4. **狀態保持與 Agents 管理**：
   * 對話期間可以暫時離開，而對話的上下文狀態會被完整保留。
   * 可以使用 `/Agents` 指令查詢當前正在背景運行的子代理，實現多任務併行。

## ⏱️ 附時間戳記的段落大綱
* `[00:02]` 課程引言：Vibe Coding 潮流與 Claude Code CLI 工具介紹。
* `[02:03]` 下載並配置 VS Code，安裝 Claude Code 並進行本地授權登入。
* `[04:00]` 在終端機中使用 Shift + Enter 進行多行指令輸入。
* `[06:00]` 任務委託：請 Claude 自動撰寫專案的系統設計藍圖與步驟。
* `[08:01]` 演示 Claude 在編譯出錯時自動捕捉 error 並自行修正 bug 的過程。
* `[10:01]` 退出工具後，說明本地對話與上下文歷史狀態如何被完整保存。
* `[12:02]` 權限代理：讓 AI 自主執行 package 安裝與環境編譯。
* `[14:00]` 雙擊左鍵開啟代碼檔案，實際檢視 AI 生成的邏輯。
* `[16:01]` 安全限制：如何在 Harness 腳手架中限制 AI 執行高風險 Shell 指令。
* `[18:01]` 使用 /Agents 指令監控背景運行的協作代理。
* `[22:01]` 概念成型：動嘴完成產品開發、驗證與測試。

## 🌐 中英專有名詞對照表
* **Claude Code**：Anthropic 官方 CLI 開發助理
* **Vibe Coding**：動嘴/氛圍編程
* **CLI (Command Line Interface)**：命令列介面
* **State Preservation**：狀態保持 / 對話歷史保存
* **/Agents**：代理監控指令

## 🏃‍♂️ 行動指南
* 本地安裝 Claude Code，並下指令「幫我寫一個簡單的計時器網頁，並使用 Python 啟動伺服器」，實測 Vibe Coding。
* 思考：Claude Code 與一般的 GitHub Copilot 網頁版/外掛版相比，最大的優勢在哪裡？
"""
    },
    {
        "id": "-EivK7vpOXY",
        "title": "Hermes Agent 保姆級教學來了！最安全的 AI 私人助理造成 OpanClaw 大規模棄養潮，用過就回不去了！",
        "filename": "Hermes Agent 保姆級教學與私人助理實測.md",
        "content": """# 🎥 Hermes Agent 保姆級教學來了！最安全的 AI 私人助理造成 OpanClaw 大規模棄養潮，用過就回不去了！

## 📌 影片資訊
* **影片 ID**：-EivK7vpOXY
* **原始網址**：https://www.youtube.com/watch?v=-EivK7vpOXY
* **講者**：PAPAYA 電腦教室
* **類別**：單一影片學習筆記
* **創作者**：PAPAYA 電腦教室

---

## 🧠 核心概念與技術摘要
1. **Hermes Agent 系統定位**：
   * 一款主打「安全、隱私與沙盒防護」的 AI 私人助理系統，在安全性上優於傳統 OpenClaw，因此被暱稱為引發「OpenClaw 棄養潮」的強大工具。
2. **權限管控與非管理者原則**：
   * 為了防止 AI 被惡意代碼挾持，Hermes Agent 嚴格採用「一般用戶（Non-administrator）」權限運行，杜絕高風險的系統級改寫。
3. **開工指令與多 Agent 協作（Always Proceed）**：
   * 支援輸入「開工」指令一鍵喚醒多個協作代理，同時在多個背景線程執行複雜任務。
   * 採用授權式（Authorization）安全認證，保障檔案不被 AI 私自外傳。
4. **實戰助手應用（以 豆豆 助理為例）**：
   * **圖像處理**：上傳耳環照片，豆豆會自動識別物體並調用修圖腳本進行「背景裁剪」。
   * **位置規劃**：查詢台北市手工材料採購路線並給予行程建議。
   * **趣味互動**：根據指示動態生成網路梗圖（Memes）。

## ⏱️ 附時間戳記的段落大綱
* `[00:02]` Hermes Agent 簡介，它與 OpenClaw 的安全機制防護差異。
* `[02:02]` 帳戶權限配置：如何以非管理者權限安全運行 Agent。
* `[04:01]` 訂閱方案與費用說明（長約套餐性價比分析）。
* `[06:02]` 建立對話 Session 與短期對話快取管理。
* `[08:01]` 輸入關鍵指令與 AI Private Assistant 的初始交互。
* `[10:00]` 新增獨立對話分流，建立不同專案的助理大腦。
* `[12:01]` 輸入系統初始化指令，啟動自動化狀態確認。
* `[14:00]` 開工工作流：多個 Agent background 併行與同步。
* `[16:00]` 授權確認攔截點（Harness Security Confirm）設計。
* `[18:02]` 實用任務演示：台北手作材料行採購路線查詢規劃。
* `[20:02]` 調用圖片處理工具進行去背與背景裁切（耳環照片範例）。
* `[22:02]` 創意工作流：文字直接生成趣味梗圖。
* `[24:01]` 實物影像辨識分析：結合視覺模型進行圖片語意理解。
* `[26:03]` 迴圈式進程推進，一步步逼近複雜目標的拆解。

## 🌐 中英專有名詞對合表
* **Hermes Agent**：荷米斯智能代理
* **Sandboxed Environment**：沙盒防護環境
* **Non-administrator**：非管理員權限
* **Authorization Dialog**：授權確認視窗
* **Image Auto-cropping**：影像自動裁切

## 🏃‍♂️ 行動指南
* 配置 Hermes Agent，將其權限限制在非管理者模式，並嘗試傳送一張照片請它去背。
* 討論：相較於 OpenClaw，Hermes Agent 在處理用戶隱私檔案時，採取了哪些更安全的保護措施？
"""
    },
    {
        "id": "r5M0W66xcGc",
        "title": "別再小看本地 AI！Gemma 4 + LM Studio 讓你的電腦變成超級離線 AI 工作站，而且完全免費 (手機也能使用喔！)",
        "filename": "LM Studio 與 Gemma 4 離線 AI 工作站建置.md",
        "content": """# 🎥 別再小看本地 AI！Gemma 4 + LM Studio 讓你的電腦變成超級離線 AI 工作站，而且完全免費 (手機也能使用喔！)

## 📌 影片資訊
* **影片 ID**：r5M0W66xcGc
* **原始網址**：https://www.youtube.com/watch?v=r5M0W66xcGc
* **講者**：PAPAYA 電腦教室
* **類別**：單一影片學習筆記
* **創作者**：PAPAYA 電腦教室

---

## 🧠 核心概念與技術摘要
1. **本機 AI 的優勢（Offline LLM）**：
   * 完全在個人電腦運行，無需網際網路，100% 保障資料安全與隱私，且完全免費，沒有 Token 額度限制。
2. **LM Studio 軟體與模型配置**：
   * 一款簡單好用的本地模型載入器。支援下載 GGUF 格式的模型檔案（如 Gemma 4 或者是輕量化的 A3B 模型）。
   * 提供 **System Prompt (系統提示詞)** 欄位，可用來調教本地模型的角色設定。
3. **進階本地應用與數據分析**：
   * 支援在本地上傳 CSV 格式的結構化表格資料，讓本地 AI 進行數據統計、過濾與趨勢分析。
   * **工具調用 (Tool Use / Function Calling)**：本地模型同樣支援 Function Calling，可呼叫本地 Python 腳本。
4. **局域網伺服器（Local Server）擴展**：
   * LM Studio 內建一鍵啟動 API 伺服器功能，將本機變成局域網 AI 主機。其他設備（如 iPhone/Android 手機）可以透過網路連接，免費使用這台電腦的運算力進行 AI 對話。
   * 本地自動化：結合 python 自動建立檔案夾（如名為「筆記」的目錄）。

## ⏱️ 附時間戳記的段落大綱
* `[00:02]` 本機 AI 概念介紹：免網際網路、零費用、隱私保全。
* `[02:01]` 安裝 LM Studio，搜尋並下載 Gemma 4 / A3B 等熱門本地 GGUF 模型。
* `[04:00]` 設定 System Prompt 定義本地 AI 助理的語意風格與限制。
* `[06:00]` 實測 CSV 資料上傳，讓離線 AI 在本機進行複雜表格數據分析。
* `[08:03]` 演示本地模型的 Tool Use（功能呼叫）執行能力。
* `[10:00]` 在 LM Studio 中啟用本地 API 伺服器（Local Port 1234）。
* `[12:00]` 手機端設定連線，共享電腦 GPU/CPU 運算力以使用免費離線 AI。
* `[14:01]` 實測本機 Python 腳本連動：自動建立「筆記」子資料夾。
* `[16:02]` 安全提示：如何信任本地開發者簽章，雙擊執行 Python 自動化代碼。

## 🌐 中英專有名詞對照表
* **LM Studio**：本地大模型加載平台
* **Gemma 4**：Google 開源本地大語言模型
* **GGUF**：本地模型通用儲存格式
* **System Prompt**：本機系統提示詞
* **Local Server / API Port**：本機伺服器 / 接口埠
* **Tool Use (Function Calling)**：工具調用 / 函數呼叫

## 🏃‍♂️ 行動指南
* 下載並安裝 LM Studio，搜尋並下載一個 3B 或 7B 的 GGUF 格式模型（如 Gemma-2-9b-it）。
* 開啟本地伺服器，使用 Python `requests` 寫一段簡單的腳本，發送對話 POST 請求到 `http://localhost:1234/v1/chat/completions`。
* 思考：本地運行大模型，對於電腦的硬體配置（CPU、GPU 顯存、記憶體）有何具體要求？
"""
    }
]

# 4. 執行寫入
# A. 寫入單一影片
for video in single_videos:
    v_id = video["id"]
    title = video["title"]
    fname = video["filename"]
    content = video["content"]
    
    # 寫入專案 output 目錄
    out_path = os.path.join(output_singles, fname)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    # 寫入 Obsidian
    obs_path = os.path.join(obsidian_singles, fname)
    with open(obs_path, 'w', encoding='utf-8') as f:
        f.write(content)

# B. 寫入播放清單影片
success_count = 0
for video in playlist_videos:
    v_id = video["id"]
    title = video["title"]
    index = video["index"]
    fname = video["filename"]
    
    content = f"""# 🎥 {title}

## 📌 影片資訊
* **播放清單序號**：EP{index:02d}
* **影片 ID**：{v_id}
* **原始網址**：https://www.youtube.com/watch?v={v_id}
* **播放清單**：網頁 & 架站 & 開發
* **講者**：PAPAYA 電腦教室
* **創作者**：PAPAYA 電腦教室

---

"""
    content += video["content_func"]()
    
    # 寫入專案 output 目錄
    out_path = os.path.join(output_playlist, fname)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    # 寫入 Obsidian
    obs_path = os.path.join(obsidian_playlist, fname)
    with open(obs_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    success_count += 1

print(f"[SUCCESS] Re-structured and generated {success_count} playlist files plus 3 single video notes!")
