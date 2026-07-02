# 🎥 解剖小龍蝦 — 以 OpenClaw 為例介紹 AI Agent 的運作原理

## 📌 影片資訊
* **播放清單序號**：EP01
* **影片 ID**：2rcJdFuNbZQ
* **原始網址**：https://www.youtube.com/watch?v=2rcJdFuNbZQ
* **播放清單**：【機器學習2026】
* **講者**：李宏毅教授

---

## 🧠 核心概念與技術摘要
1. **什麼是 AI Agent（以 OpenClaw 為例）**：
   * 傳統大型語言模型（LLM）通常「只動口不動手」（如指導教授般只給建議，無法動手操作）。
   * AI Agent（代理）如 OpenClaw（其代表動物為小龍蝦，Claw 為螯/爪）則是具備「動手能力」的系統，可 24 小時在電腦本機或伺服器上持續運行，自動執行任務。
2. **AI Agent 的主動執行力與工具呼叫**：
   * 當給予 Agent 一個複雜指令（例如「幫我創建 YouTube 頻道、每天構想影片、審核通過後自動上傳」），Agent 能真正串接 Google/YouTube API 創立頻道，呼叫 Imagen 等繪圖工具生成頭像，並使用自動化腳本合成與發布影片。
3. **運作核心：Prompt 與 Scaffolding (Harness)**：
   * 語言模型本質是預測下一個 Token 的概率分佈，它本身沒有智慧或主動性。
   * Agent 的智慧來自其外部包裝的「Harness（腳手架）」。Harness 提供 System Prompts（定義行為準則與角色設定）、Memory（上下文記憶）以及 Tool Schema（定義工具的輸入輸出規格），並以循環迭代（Loop）的方式驅動 LLM 規劃與執行。
4. **Skills 的定義與移植**：
   * Skill 本質上是文字檔（Markdown 格式），詳細定義了 Agent 如何規劃、使用哪些工具與執行特定任務的流程。這使得 Agent 技能可以像代碼一樣被編寫、安裝與移植。

## ⏱️ 附時間戳記的段落大綱
* `[00:00]` 課程開場與 AI Agent 代表性開源專案 OpenClaw 簡介。
* `[03:01]` 實測對比：一般 LLM（只給建議）vs. AI Agent（主動建頻道、畫頭像、發訊息）。
* `[09:02]` 解密 AI Agent 背後的系統機制，人類長期以來的自動化夢想。
* `[15:00]` 語言模型與 OpenClaw 的互動過程（Prompts 與 Tool Schemas 結構）。
* `[21:02]` 語言模型的本質（Next Token Prediction）與目標驅動（Goal-Driven）Agent 的區別。
* `[30:00]` 系統提示詞（System Prompts）與行為準則對 Agent 行為的約束。
* `[45:01]` LLM 與外部工具、腳本執行的遞迴式反饋與通訊循環。
* `[57:00]` 什麼是 Skills（基於 Markdown 的技能定義文件）以及如何在 Agent 間移植。
* `[01:06:01]` 實務挑戰：API 額度限制（Quota）、死循環問題與 Agent 自我修改代碼的風險。

## 🌐 中英專有名詞對照表
* **AI Agent**：人工智能代理 / 智能體
* **OpenClaw**：開源小龍蝦 Agent 專案
* **Tool Calling / Tool Schema**：工具呼叫 / 工具規格定義
* **System Prompt**：系統提示詞
* **Scaffolding / Harness**：腳手架 / 封裝環境
* **Next Token Prediction**：下一個 Token 預測

## 🏃‍♂️ 行動指南
* 下載並在本地部署 OpenClaw，嘗試設定其 WhatsApp 或 Discord 連線。
* 閱讀一個 Skill 檔案，理解其中是如何定義 System Prompt 與工具呼叫流程的。
* 思考：若 Agent 擁有無限的代碼自改權限，會帶來哪些潛在的系統安全隱患？
