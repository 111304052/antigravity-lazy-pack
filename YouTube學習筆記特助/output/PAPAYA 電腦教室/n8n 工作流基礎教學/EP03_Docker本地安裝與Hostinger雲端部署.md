# 🎥 學會 n8n 為你省下 80% 時間！(EP.3) 「本地安裝」/「雲端部署」比你想的還要簡單！

## 📌 影片資訊
* **播放清單序號**：EP03
* **影片 ID**：D-VEcKZ3NV0
* **原始網址**：https://www.youtube.com/watch?v=D-VEcKZ3NV0
* **播放清單**：n8n 工作流基礎教學
* **講者**：PAPAYA 電腦教室

---

## 🧠 核心概念與技術摘要
1. **n8n 的部署方式**：
   * 官方雲端版（n8n Cloud）便利但有 14 天試用限制，後續付費高昂（每月 20 歐元起）。
   * 自建部署主要有兩種方式：**本機部署**（使用電腦的 Docker，適合測試與個人隱私防護）與**雲端部署**（使用 VPS 伺服器，適合 24 小時不中斷運行）。
2. **本機 Docker 安裝與配置**：
   * **Docker**：一種類似「免安裝軟體套件（容器）」的虛擬化工具，不影響宿主主機系統，不殘留系統登錄檔。
   * **Images (映像檔)**：包含應用程式的靜態壓縮套件。
   * **Container (容器)**：解壓後實際運行的實體。
   * **Port (連接埠)**：連接埠號設為 `5678`。
   * **Volumes (資料卷)**：用來將容器內部的檔案路徑（`/home/node/.n8n`）映射對齊到本地實體檔案夾，確保工作流程與認證資訊永久保存，重啟容器不丟失。
3. **自架版 Google API OAuth 驗證設定**：
   * 因為自架服務屬於 Google 認可的「外部未知應用」，無法直接像雲端版一樣一鍵授權，必須建立自己的通行證。
   * **步驟**：前往 Google Cloud Console ➔ 建立新專案 ➔ 啟用 Google Calendar API 和 Gmail API ➔ 設定 OAuth 同意畫面（選擇「外部」並將個人帳號加入為「測試使用者」） ➔ 建立憑證（網頁應用程式）並在「重新導向 URI」中填入自架 n8n 專屬的 OAuth callback URL ➔ 複製 Client ID 與 Client Secret 回填至 n8n，即可完成帳號綁定。
4. **雲端伺服器（VPS）部署**：
   * 本地 Docker 部署的缺點是電腦不能關機，且斷網會導致自動化流程失效。
   * **Hostinger VPS** 方案：提供一鍵安裝 n8n 模板。配置安全掃描與伺服器管理員密碼。以較低成本（如每月 4.99 美元）提供 24 小時穩定運行的雲端自動化環境。

## ⏱️ 附時間戳記的段落大綱
* `[00:02]` 自架 n8n 部署背景與官方 14 天到期停止服務之限制分析。
* `[01:04]` 下載並啟動 Docker Desktop，映像檔 (Image) 與容器 (Container) 的概念對比。
* `[02:02]` n8n 映像檔 Pull 與執行設定：Container Name、門牌 Port (5678)、以及本地 Volumes 資料夾路徑對應。
* `[02:31]` 瀏覽器開啟登入本機 `localhost:5678`，設定管理員帳號、獲取免費授權碼解鎖歷史紀錄等進階功能。
* `[03:19]` 將原雲端版的工作流 JSON 檔案匯出，並重新匯入至本地自架平台的還原示範。
* `[03:50]` 自架版節點警示標記原因：說明自架服務連接 Google Calendar & Gmail 需要 OAuth 專屬憑證。
* `[04:30]` Google Cloud Console 專案新建，API 櫃台啟用（Google Calendar API、Gmail API）。
* `[04:47]` OAuth 同意畫面設定（外部類型、測試使用者名單加入、填寫聯絡信箱）。
* `[05:41]` 建立網頁應用程式用戶端憑證，複製 n8n 重新導向 URI 並貼至 Google Cloud Console。
* `[06:05]` 取得用戶端 ID (Client ID) 與用戶端密碼 (Client Secret)，貼回 n8n 完成授權。
* `[06:44]` 連接 OpenAI API Key，測試本地自建平台重新收發郵件與行程處理成功。
* `[07:12]` 本機 Docker 運作的缺點：電腦不能關機、断網即失效。雲端部署方案介紹。
* `[07:37]` 使用 Hostinger 一鍵安裝 n8n 範本部署 VPS，套餐選擇與付費週期成本計算。
* `[08:24]` 付款後設定伺服器管理密碼，一鍵啟用並進入 VPS 架設完成之 n8n 雲端登入頁面。

## 🌐 中英專有名詞對照表
* **Docker / Docker Desktop**：開源應用程式容器引擎 / 本地桌面版
* **Image / Container**：映像檔 / 容器
* **Port / Volumes**：連接埠 / 資料卷
* **Google Cloud Console**：Google 雲端主控台
* **OAuth Consent Screen**：OAuth 同意畫面
* **Test Users**：測試使用者
* **Client ID / Client Secret**：用戶端 ID / 用戶端密碼
* **Redirect URIs**：已授權的重新導向 URI
* **VPS (Virtual Private Server)**：虛擬專用伺服器
* **Hostinger**：知名 VPS 雲端主機提供商

## 🏃‍♂️ 行動指南
* 在本地電腦安裝 Docker，並成功拉取 `n8n` 映像檔，啟動一個本機容器。
* 前往 Google Cloud Console 建立一個專案，模擬生成一組 Client ID 與 Client Secret，並成功將自建的本地 n8n 與你的 Google Calendar 串接。
* 討論：相較於本地部署，將自動化工作流部署在雲端 VPS（如 Hostinger）會帶來哪些好處與壞處？
