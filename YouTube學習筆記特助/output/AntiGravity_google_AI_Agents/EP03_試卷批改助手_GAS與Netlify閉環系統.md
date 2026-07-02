# 🎥 AntiGravity 基本功 EP03：試卷批改助手（GAS 與 Netlify 零複製雙向閉環系統）

## 📌 影片資訊
* **標題**：AntiGravity基本功EP03:超強試卷批改助手_用 GAS 與 AI 進行批次自動閱卷...
* **講者/頻道**：三師爸Sense Bar
* **原始網址**：https://www.youtube.com/watch?v=-oBHrpEsJs8
* **播放清單**：AntiGravity_google_AI_Agents

## 🧠 核心概念與技術摘要
1. **GitHub 與 Firebase 的低門檻替代方案**：
   * 對於不熟悉 Git 註冊與 Firebase 設定的初學者，可以使用 **Netlify**（掛載靜態網頁）與 **Google Sheets + GAS**（作為後端資料庫）的輕量化組合。
2. **Google Sheets 當作即時資料庫**：
   * 透過 Google Apps Script (GAS) 將試算表發布成 WebApp API，前端網頁可以直接 POST 學生分數與作答紀錄寫入試算表。
3. **clasp 串接 Workspace 服務**：
   * 安裝 Google 的 `clasp` 工具，讓 Agent 可以直接透過命令列登入並發布 GAS 程式碼。這讓 AI 能自動串接 Gmail、Google 行事曆與試算表服務。
4. **雙向閉環自動閱卷**：
   * 學生在網頁上填寫答案 ➔ 資料傳入試算表 ➔ Agent 讀取試算表記錄 ➔ 自動調用 AI 進行申論題批改與評語 ➔ 將結果寫回試算表並發送 Email。

## 🏃‍♂️ 行動指南
* 註冊 Netlify 帳號並安裝 Netlify CLI (`npm install -g netlify-cli`)。
* 安裝 `@google/clasp` 工具來部署 Google Apps Script。
* 建立一個成績登錄試算表，並設定 WebApp API 接收前端資料。
