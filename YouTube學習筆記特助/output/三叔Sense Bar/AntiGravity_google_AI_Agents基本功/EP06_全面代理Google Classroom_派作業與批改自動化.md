# 🎥 Antigravity 基本功 EP06:全面代理你的 Google Classroom_派作業、收作業、批改一次搞定：AI × Google Classroom 完整教學

## 📌 影片資訊
* **播放清單序號**：EP06
* **影片 ID**：vYb87aqvBuE
* **原始網址**：https://www.youtube.com/watch?v=vYb87aqvBuE
* **播放清單**：AntiGravity_google_AI_Agents基本功
* **講者**：三叔Sense Bar

---

## 🧠 核心概念與技術摘要
1. **Google Classroom API 自動化代理**：
   * 透過 Google Classroom API，AI Agent 可以直接讀取您的課堂資訊、下載學生的作答檔案、派發新作業，甚至進行自動化批改與成績登記。
2. **Google Cloud Console 認證設定**：
   * 因為是存取敏感的課堂與學生資料，必須建立專屬通行證：
     1. 前往 Google Cloud 建立新專案。
     2. 啟用 **Google Classroom API**。
     3. 設定 OAuth 同意畫面，將自己與學生的帳號加入「測試使用者（Test Users）」。
     4. 建立網頁應用程式憑證，複製重新導向 URI 並取得 Client ID 與 Client Secret 回填至 Agent 節點。
3. **學生名單與作業批量處理**：
   * 成功連接後，AI 可以一鍵拉出所有班級學生的繳交狀況。對於逾期未交者，可自動列出名單並撰寫催繳 Email 草稿。

## ⏱️ 附時間戳記的段落大綱
* `[00:00]` 課程引言：介紹如何用 AntiGravity Agent 全面接管派作業、收作業與自動批改的工作流。
* `[02:02]` 本地專案工作目錄與 Google Cloud API 的連結邏輯。
* `[04:01]` 實戰演示：在 Google Cloud Console 新建專案與啟用 Classroom API 服務。
* `[06:02]` OAuth 同意畫面配置要領（選擇外部、填寫管理者聯絡信箱）。
* `[08:01]` 測試使用者權限設定：為什麼必須將課堂測試帳號加入名單。
* `[10:01]` 如何在憑證頁面建立 OAuth 2.0 用戶端 ID，並配置 Redirect URIs。
* `[12:03]` 取得 Client ID 與 Client Secret，貼回 Agent 完成安全性握手。
* `[14:00]` 驗證連線：讓 Agent 讀取並列出目前 Google Classroom 中的所有活躍課程。
* `[16:00]` 實戰操作：批量拉取特定課程的學生作業繳交狀態。
* `[18:02]` 演示自動化批改：AI 讀取學生上傳的作業檔案，並給出初步評分建議。
* `[22:02]` 課堂行政自動化擴充：自動彙整學生成績並輸出為統計 Excel 報表。

## 🌐 中英專有名詞對照表
* **Classroom API**：Google 課堂應用程式介面
* **OAuth Consent Screen**：OAuth 授權同意畫面
* **Redirect URIs**：授權的重新導向網址
* **Client ID / Client Secret**：客戶端識別碼 / 客戶端密鑰
* **Assignment Auto-grading**：作業自動批改

## 🏃‍♂️ 行動指南
* 在您的 Google Cloud Console 啟用 Google Classroom API，並建立一組 OAuth 用戶端憑證。
* 思考：在進行「AI 自動化作業批改」時，教師應該扮演何種角色，以確保評分公正性與輔導反饋的溫度？
