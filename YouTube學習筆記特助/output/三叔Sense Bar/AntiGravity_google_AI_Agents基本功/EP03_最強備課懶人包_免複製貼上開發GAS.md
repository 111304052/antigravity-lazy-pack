# 🎥 AntiGravity基本功EP03:最強備課懶人包_寫 GAS 竟然再也不用複製貼上程式碼？我是怎麼做到的.

## 📌 影片資訊
* **播放清單序號**：EP03
* **影片 ID**：-oBHrpEsJs8
* **原始網址**：https://www.youtube.com/watch?v=-oBHrpEsJs8
* **播放清單**：AntiGravity_google_AI_Agents基本功
* **講者**：三叔Sense Bar

---

## 🧠 核心概念與技術摘要
1. **Google Apps Script (GAS) 開發痛點**：
   * 傳統在 Google 試算表或雲端硬碟寫 GAS，必須反覆在瀏覽器的線上編輯器與本地編輯器之間「複製、貼上」程式碼，極度沒有效率。
2. **Clasp (Google Apps Script CLI) 工具整合**：
   * **Clasp** 是 Google 官方提供的命令列工具。
   * AI Agent 可以利用 `clasp clone`、`clasp push` 與 `clasp deploy` 指令，直接讀寫本地程式碼並同步至雲端 GAS 專案，實現**「免複製貼上」的一鍵開發與部署**。
3. **前端網頁的快速發布**：
   * 透過撰寫本地 `index.html` 與 `style.css` 建立網頁，並命令 Agent 一鍵部署到免費的前端靜態託管平台，即時取得可對外發布的網址。
4. **Agent 設定優化**：
   * 為了實現一鍵 Clasp 同步與網頁部署，需在 AntiGravity 的 Project Settings 中開啟特定的自動放行選項，並設定 clasp CLI 認證。

## ⏱️ 附時間戳記的段落大綱
* `[00:00]` 課程引言：展示如何在 Google 試算表中免除複製貼上程式碼的極速備課流程。
* `[02:02]` 認識 Google Apps Script 懶人包設定，檢視欄位結構。
* `[04:02]` 在專案中啟用 Clasp API 權限，進行 Google 帳號授權驗證。
* `[06:01]` 為什麼將 clasp 整合進 AI Agent 能讓寫 GAS 腳本的速度提升數倍。
* `[08:00]` 實戰演示：讓 Agent 直接生成 Google 表單自動回覆的 GAS 代碼，並自動 push 到雲端。
* `[10:02]` 介紹免費的前端靜態網站託管平台，並將生成的教學網頁上傳。
* `[12:03]` 實戰演示：在 Agent 內自訂網頁樣式與按鈕佈置。
* `[14:01]` 前後端連動：讓 HTML 表單透過 GAS 自動寫入 Google 試算表。
* `[16:01]` 部署完成，現場測試表單資料即時寫入試算表成果。
* `[18:02]` 認識 Clasp 工具的底層架構與設定檔案（.clasp.json）。
* `[20:01]` Google 帳戶安全性設定與 API 存取權限說明。
* `[22:01]` GAS 代碼的偵錯（Debugging）與錯誤排除技巧。
* `[24:00]` 實戰執行：Agent 自動偵測語法錯誤並推送修正版程式碼。

## 🌐 中英專有名詞對照表
* **GAS (Google Apps Script)**：谷歌應用服務腳本
* **Clasp (Command Line Apps Script Projects)**：Google 官方 GAS 命令行工具
* **Git Clone / Push**：複製 / 推送
* **Static Hosting**：靜態網站託管
* **Interactive Form**：互動式表單

## 🏃‍♂️ 行動指南
* 請您的 Agent 在本地建立一個簡單的 `code.js`，並利用 Clasp 自動建立一個 GAS 專案推送至您的雲端硬碟。
* 思考：結合 Clasp 之後，AI Agent 在維護大型 GAS 專案時，相比於瀏覽器編輯器有何優勢？
