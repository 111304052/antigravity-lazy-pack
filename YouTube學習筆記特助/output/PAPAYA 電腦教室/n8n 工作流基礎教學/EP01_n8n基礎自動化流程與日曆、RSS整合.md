# 🎥 學會 n8n 為你省下 80% 時間！(EP.1) 這個 AI 助理只認你這個主人，不但使命必達且全天候待命！

## 📌 影片資訊
* **播放清單序號**：EP01
* **影片 ID**：r9mi3ZJIWbg
* **原始網址**：https://www.youtube.com/watch?v=r9mi3ZJIWbg
* **播放清單**：n8n 工作流基礎教學
* **講者**：PAPAYA 電腦教室

---

## 🧠 核心概念與技術摘要
1. **n8n 自動化工具概述**：
   * n8n 是一款強大的工作流自動化工具，能整合各種網頁服務與 API，減少繁瑣的手動操作。初學者建議先從官方 14 天免費試用雲端版（n8n Cloud）著手。
2. **工作流核心元件與資料格式**：
   * **觸發器 (Trigger)**：工作流的起點與開關。可分為「手動觸發（Manual Trigger）」與「排程觸發（Schedule Trigger）」。
   * **節點 (Nodes)**：執行特定任務的模組（如 Gmail 傳送、Google Calendar 讀取、RSS 擷取、Filter 篩選器等）。
   * **JSON 資料格式**：n8n 節點間的資料傳遞均基於 JSON 格式（名稱與數值的鍵值對清單）。在開發時可使用 `mock data` 鎖定測試數據。
3. **資訊流的管理與合併**：
   * **Edit Fields（編輯欄位）**：用來簡化資料結構，只保留需要的欄位（如將日曆複雜輸出簡化為行程名稱與開始時間）。
   * **Merge（合併）**：將多個分流的資料（如 Google 日曆分支與 RSS 新聞分支）匯整為單一資訊流。
   * **Aggregate（整合）**：將多筆獨立的資料行整合成一個清單或單一物件，避免後續節點（如 Gmail）因收到多筆資料而重複發送多封郵件。
4. **AI 節點整合（Message a Model）**：
   * 整合 ChatGPT 等大語言模型。需在 OpenAI 平台綁定卡片並儲存小額費用，取得 API Key。
   * **System Prompt** 定義 AI 角色與格式約束（例如要求 AI 將郵件分成今日行程與今日文章，並使用 HTML/CSS 美化）。
   * **User Prompt** 傳入具體要翻譯、彙整的行事曆與 RSS 新聞內容。

## ⏱️ 附時間戳記的段落大綱
* `[00:03]` n8n 功能簡介與三集教學大綱說明，官方雲端服務註冊流程。
* `[01:14]` 建立首個工作流程、手動觸發器（Manual Trigger）與 JSON 測試數據（Mock Data）解說。
* `[02:21]` 連結第一個節點（Gmail Send a Message），登入 Google 帳號與動態拖曳欄位主旨。
* `[03:56]` 進階應用：Google Calendar（Get Many Events）日曆節點設定與 ISO 8601 日期格式轉換。
* `[05:10]` 使用 Date & Time 節點自訂日期與時間格式（年月日時分），重新命名節點增加可讀性。
* `[05:59]` 使用 Edit Fields 篩選並簡化行事曆過多欄位。
* `[07:16]` 引入 Aggregate 節點整合多筆行程，使用 `join` 語法與雙換行符號進行行程換行排版。
* `[08:15]` On a Schedule 排程觸發器設定，每天早上 07:30 定時自動寄出行程。
* `[08:49]` 整合 RSS 節點自動抓取 Techcrunch 新聞，並利用 Filter 篩選「包含 AI」的熱門文章。
* `[10:33]` 使用 Merge 節點匯整日曆與 RSS 兩條資訊分流，並利用 Sticky Notes（便利貼）區隔工作區塊。
* `[12:03]` 導入 ChatGPT（Message a Model 節點），設定 OpenAI API Key 與 System/User Prompt 提示詞進行中英翻譯與 CSS 排版美化。
* `[13:45]` Gmail 節點改為 HTML 郵件類型，成功發送精美排版的今日美化摘要郵件。

## 🌐 中英專有名詞對照表
* **n8n Cloud**：n8n 雲端託管服務
* **Trigger / Manual Trigger**：觸發器 / 手動觸發
* **Schedule Trigger**：排程觸發器
* **JSON (JavaScript Object Notation)**：輕量級的資料交換格式
* **Mock Data**：測試/模擬數據
* **Date & Time Node**：日期與時間轉換節點
* **Edit Fields Node**：編輯/篩選欄位節點
* **Merge Node / Aggregate Node**：合併節點 / 整合聚攏節點
* **System Prompt / User Prompt**：系統提示詞 / 用戶提示詞

## 🏃‍♂️ 行動指南
* 註冊一個免費的 n8n Cloud 帳戶，並照著步驟建立手動觸發 Gmail 寄信的工作流。
* 嘗試找一個有 RSS Feed 的中文新聞網站，替換 Techcrunch 連結，並利用 Filter 篩選你關心的主題。
* 思考：若直接將 Merge 出來的多筆資料接入 Gmail 節點，會產生什麼樣的後果？
