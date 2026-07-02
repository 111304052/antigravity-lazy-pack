# 🎥 AntiGravity 基本功 EP07：一鍵生成 Padlet 課程看板（Padlet MCP 自動化接管）

## 📌 影片資訊
* **標題**：AntiGravity 基本功 EP07: 一鍵生成 Padlet 課程看板...
* **講者/頻道**：三師爸Sense Bar
* **原始網址**：https://www.youtube.com/watch?v=wrSYyOxf7n4
* **播放清單**：AntiGravity_google_AI_Agents

## 🧠 核心概念與技術摘要
1. **自製 Padlet MCP Server**：
   * 由於官方提供的 Padlet 整合極為陽春，講者自行開發了全功能的 Padlet MCP Server 並在 GitHub 上開源。
2. **全面接管 Padlet 功能**：
   * 安裝此 MCP 後，AI Agent 可以透過 API 直接在指定的 Padlet 看板上新增卡片（Posts）、上傳圖片與連結、自動建立投票活動。
3. **學生互動與回覆自動化**：
   * Agent 能定時下載 Padlet 板上學生的上傳檔案與附件，並根據內容自動撰寫批改回饋，回覆在 Padlet 該卡片的留言板（Comments）中。
4. **開發人員 Key 與權限**：
   * 需要擁有付費/教育版的 Padlet 帳號，並在「設定」➔「開發人員」中產生專屬的 API Key，交給 Agent 來進行配置。

## 🏃‍♂️ 行動指南
* 前往 Padlet 右上角設定 ➔ 開發人員，新增並取得 API Key。
* 從 GitHub 下載講者開源的 Padlet MCP 並由 Agent 進行 npm install。
* 執行測試：下令讓 Agent 在 Padlet 板上新增一個「今日簽到與意見調查」卡片。
