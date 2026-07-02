# 🎥 學會 n8n 為你省下 80% 時間！(EP.2) 這個 AI 助理只認你這個主人，不但使命必達且全天候待命！

## 📌 影片資訊
* **播放清單序號**：EP02
* **影片 ID**：sRU6Y7DXkLI
* **原始網址**：https://www.youtube.com/watch?v=sRU6Y7DXkLI
* **播放清單**：n8n 工作流基礎教學
* **講者**：PAPAYA 電腦教室

---

## 🧠 核心概念與技術摘要
1. **AI Agent 與傳統自動化的差異**：
   * 傳統自動化必須由人類寫死「If-Then」的硬編碼邏輯。
   * AI Agent（智能體）節點搭配大語言模型（Chat Model，如 GPT-4o-mini），具有自主思考、規劃與選擇工具的決策能力。
2. **AI Agent 的基礎結構**：
   * **身體 (AI Agent 節點)**：負責處理觸發訊號並呼叫外部工具。
   * **大腦 (Chat Model 節點)**：背後的推理大模型。
   * **System Message（系統訊息）**：設定行為準則（如要求一律使用繁體中文）。
   * **Memory (記憶模組)**：引入 `Simple Memory` 節點。預設可在同一 Session ID（會話識別碼）下保存 5 輪上下文，使 AI 理解前後文。
3. **工具授權與決策（Google Calendar Tool）**：
   * 建立四大行事曆操作工具：Create（新建）、Delete（刪除）、Get Many（讀取）與 Update（更新）。
   * 關鍵在於將工具的參數設定權限移交給 AI（點擊欄位旁的工具圖示），讓 AI 根據用戶口語指令動態判斷 Summary、Start Time、End Time 與 Event ID。
   * 提示詞優化：在 System Message 中寫入時間語法 `{{ $now }}` 告知 AI 當前的即時時間，使 AI 能夠精準定位「今天」、「這週六」等相對時間概念。
4. **多元觸發渠道 (Webhook & Telegram)**：
   * **Webhook (POST)**：建立一個專用接收網址。整合 iPhone 捷徑（Siri 語音輸入 ➔ POST 文字 JSON 至 Webhook ➔ Respond to Webhook 語音朗讀回覆，需設定 UTF-8 標頭）。
   * **Telegram Bot**：透過 BotFather 申請 Bot Token，在 n8n 中設定 Telegram Trigger (On Message) 監聽，並使用 Telegram Node (Send a Text Message) 回應，可關閉 n8n 署名以保持版面乾淨。
5. **AI 智能分流與多工具協作 (Gmail & Contacts)**：
   * 使用 **Text Classifier（文本分類節點）** 連接 LLM，將收到的郵件語意分類為與會議「相關」或「無關」。
   * **Gmail Tool (Send, Reply, Draft)** 與 **Google Contacts Tool (Get Many with Query)**：當信件與會議相關時，AI Agent 動態查詢聯絡人信箱、比對行事曆衝突。若無衝突則直接新增並透過 Telegram 發送確認；若有衝突，則透過 Telegram 詢問是否要改期，並自動撰寫改期信件草稿。

## ⏱️ 附時間戳記的段落大綱
* `[00:03]` AI Agent 概念介紹：自主規劃與決策的大腦助理。
* `[00:46]` 建立 AI Agent 節點，設定內建聊天觸發器與連接 Chat Model（ChatGPT-4o-mini）。
* `[01:46]` System Message 設定繁體中文約束，與引入 Simple Memory 簡易記憶模組（Session ID、對話記憶上限）。
* `[02:52]` 串接 Google Calendar Tool：分別設定 Create、Delete、Get Many、Update 四大節點並重新命名。
* `[05:08]` 日曆查詢實測失敗原因剖析：缺乏當前時間。在提示詞中使用 `{{ $now }}` 語法注入當前時間。
* `[06:20]` 外接輸入源 Webhook（POST）取代預設聊天室，使用 iPhone 捷徑將 Siri 語音轉為文字並傳送至 Webhook。
* `[08:50]` Respond to Webhook 節點設定，將回覆格式設為 Text 並新增 UTF-8 標頭防止 Siri 朗讀亂碼。
* `[10:30]` 語音實測新增「看牙醫」行程至日曆，並將 Webhook 網址轉為生產線 Production（移除 /test 後綴）。
* `[11:27]` Telegram 管道串接：利用 BotFather 新增機器人、取得 Token 與設定 Chat ID。
* `[12:34]` 設定 Telegram Trigger（On Message）與 Send Text Message 回應節點，關閉「附加 n8n 署名」。
* `[14:20]` 高級工作流：Gmail（On Message Received）郵件觸發與 Text Classifier（文本分類節點）語意分流。
* `[16:20]` AI Agent 會議衝突自動化決策提示詞調整：自動收信 ➔ 比對日曆 ➔ 無衝突直接排程 ➔ 有衝突 Telegram 詢問。
* `[17:34]` Gmail Tool (Send, Reply, Draft) 與 Google Contacts (聯絡人查詢) 整合，讓 AI 自主代寫信件並存入草稿匣。
* `[18:30]` 實戰檢驗：時間無衝突自動排程、時間重疊時 Telegram 互動改期、以及手動/自動草稿郵件發送。

## 🌐 中英專有名詞對照表
* **AI Agent Node**：智能代理節點
* **Chat Model**：對話推理大模型
* **Simple Memory**：簡易上下文記憶模組
* **Session ID**：會話識別碼
* **{{ $now }}**：動態時間注入變數
* **Webhook / Respond to Webhook**：網頁鉤子 / 鉤子響應節點
* **Telegram Bot / BotFather**：機器人 / 機器人之父帳號
* **Text Classifier**：文本/語意分類節點
* **Gmail Tool / Google Contacts Tool**：郵件工具 / 聯絡人工具
* **Draft Box**：草稿匣

## 🏃‍♂️ 行動指南
* 在 Telegram 申請一個專屬的機器人，取得 Token 並在本地 n8n 建立一個簡單的 Telegram 聊天機器人。
* 思考：在 AI Agent 中，如果我們在 System Message 中沒有設定 `{{ $now }}`，AI 助理在處理相對時間（如「明天早上十點」）時會遇到什麼問題？
* 試著在 Gmail Tool 中加入 Draft 功能，寄一封信測試 AI 是否能正確將內容放入草稿匣。
