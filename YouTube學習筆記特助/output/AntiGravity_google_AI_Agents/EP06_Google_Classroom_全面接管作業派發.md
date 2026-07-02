# 🎥 AntiGravity 基本功 EP06：Google Classroom 全面代理（OAuth 串接與作業自動派發）

## 📌 影片資訊
* **標題**：Antigravity 基本功 EP06: 連結您的 Google Classroom_作業自動派發...
* **講者/頻道**：三師爸Sense Bar
* **原始網址**：https://www.youtube.com/watch?v=vYb87aqvBuE
* **播放清單**：AntiGravity_google_AI_Agents

## 🧠 核心概念與技術摘要
1. **個人帳號與教育帳號的橋接**：
   * 學校的 Google 教育帳號（Google Workspace for Education）通常不支援直接開啟 Google AntiGravity 的實驗性服務。
   * **解決方案**：在 Google Cloud Console 中，使用個人 Google 帳號建立 OAuth 憑證，並將教育帳號加入為「測試使用者」，即可安全登入教育版 Google Classroom。
2. **Google Classroom API 設定步驟**：
   * 前往 Google Cloud Console ➔ 啟用 Google Classroom API ➔ 配置 OAuth 同意畫面 ➔ 新增測試使用者 ➔ 建立憑證（下載 client_secret.json）。
3. **全面接管 Classroom CLI**：
   * 利用 Classroom Agent Kit 讀取憑證，授權後 Agent 可直接透過 Python 腳本查詢課程清單、自動發布作業公告（CourseWork）、下載學生交上來的附件，並在本地批改完後自動登記分數。

## 🏃‍♂️ 行動指南
* 前往 Google Cloud Console 啟用 Classroom API。
* 下載並設定 OAuth 2.0 `credentials.json` 憑證。
* 測試以 Agent 執行 Python 程式碼，列出您 Classroom 當中的所有課程名稱。
