# 🎥 AntiGravity 基本功 EP05：AI 語音教學卡（App 五個等級與 edge-tts 免費語音生成）

## 📌 影片資訊
* **標題**：AntiGravity 基本功 EP05: AI語音教學卡製作五步驟...
* **講者/頻道**：三師爸Sense Bar
* **原始網址**：https://www.youtube.com/watch?v=hRdQCQSozY0
* **播放清單**：AntiGravity_google_AI_Agents

## 🧠 核心概念與技術摘要
1. **教學應用程式的 5 個階級 (Levels)**：
   * **L1 前端靜態網頁**：沒有資料庫、不需記住資料，單純網頁互動。
   * **L2 網頁 + Google Sheets**：用 Google 試算表存資料，開發簡單，但高並發（很多人同時寫入）時會有卡頓延遲。
   * **L3 網頁 + 專業資料庫 (Firebase/Supabase)**：零延遲、即時更新，適合即時多人在線互動（如文字雲、線上對戰）。
   * **L4 網頁 + AI API (Groq/Gemini)**：利用單一後端 Key 讓整班學生免註冊帳號，即可與 AI 進行思考對話。
   * **L5 本地 AI Agent 連線**：全面託管，AI 直接跑 Python 產出實體媒體與排版檔案。
2. **edge-tts 實現免費高品質 TTS**：
   * 無須購買昂貴的 OpenAI/Google TTS API，利用 Python `edge-tts` 套件，可以直接抓取微軟 Edge 瀏覽器的語音引擎，免費生成高品質的中英文語音 MP3。
3. **AI 語音卡自動化工作流**：
   * 寫入單字與釋義 ➔ Python 自動生成 MP3 ➔ 自動寫入 HTML5 audio 播放網頁 ➔ 部署到 Netlify。

## 🏃‍♂️ 行動指南
* 本地安裝 `pip install edge-tts`。
* 申請 Groq 的免費 API Key 來獲得高速文字推理。
* 實作語音生成腳本，讓 Agent 自動為學習單單字生成語音檔。
