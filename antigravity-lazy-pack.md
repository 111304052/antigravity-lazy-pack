# antigravity-lazy-pack - 專案駕駛艙

## 專案資訊
- **專案名稱**：antigravity-lazy-pack
- **主要工作目錄**：`c:\Users\leots\OneDrive\Desktop\Antigravity2.20260626`
- **GitHub Repository**：[mathruffian-dot/antigravity-lazy-pack](https://github.com/mathruffian-dot/antigravity-lazy-pack)
- **目前狀態**：🟢 服務連接與工作流初始化完成，三大學習專案建置完畢

---

## 服務狀態與設定紀錄

### 1. NotebookLM MCP (01-notebooklm)
- **狀態**：🟢 已連接 ( leotsai0508@gmail.com )
- **安裝路徑**：`C:\Users\leots\anaconda3\Scripts\nlm.EXE`
- **MCP 註冊**：已寫入全域 `mcp_config.json`

### 2. GitHub CLI (02-github)
- **狀態**：🟢 已安裝且已使用 Personal Access Token 完成登入
- **版本**：gh version 2.95.0
- **MCP 註冊**：使用內建 Git 工具搭配 GitHub CLI 執行

### 3. Firebase MCP (03-firebase)
- **狀態**：🟢 已安裝且已完成 Web 登入
- **MCP 註冊**：已寫入全域 `mcp_config.json` (使用 `npx.cmd -y firebase-tools@latest mcp`)

### 4. Obsidian MCP (06-obsidian)
- **狀態**：🟢 已安裝且已建立儲存庫
- **儲存庫路徑**：`C:\Users\leots\OneDrive\文件\Secondbrain`
- **MCP 註冊**：已寫入全域 `mcp_config.json` (使用 `mcpvault`)

---

## 每日工作紀錄

### 2026-06-26
- **完成事項**：
  - 成功從 GitHub 複製 `antigravity-lazy-pack` 專案。
  - 將 7 個懶人包技能（00 至 06）複製並安裝至全域自訂技能目錄。
  - 安裝並驗證 `notebooklm-mcp-cli`。
  - 透過 `winget` 自動安裝 **GitHub CLI** 與 **Node.js LTS**。
  - 全域安裝 `@bitbonsai/mcpvault` (Obsidian MCP 伺服器)。
  - 建立全新 Obsidian 儲存庫 `Secondbrain` 並初始化專案駕駛艙。
  - 完成 `mcp_config.json` 註冊設定，整合 NotebookLM、Firebase、Obsidian。
  - 於專案根目錄建立 `ANTIGRAVITY.md` 規則檔案。
  - **[新增]** 設定 Git 全域帳號 (`leotsai`) 與匿名保護電子郵件。
  - **[新增]** 本地與 GitHub 同步建立三個平台之 Private 儲存庫：`Tibame`、`Hahow`、`Graduate-School-of-Statistics`（統研所）。
  - **[新增]** 在 Obsidian 中為三個平台建立對應的資料夾與結構化「學習主頁」筆記，規劃專屬學習地圖。
  - **[新增]** 同步調整本機資料夾結構（Hahow 補上 `R`、`SQL`、`Tableau`；統研所調整為`必修`、`選修`、`教授`、`研究計畫`），並將所有現有課程檔案首次推送到 GitHub。
- **下一步**：
  - 開始將 PyCharm、RStudio 的學習程式碼與資料放入本機資料夾，並要求 AI 助理自動同步到 GitHub 與 Obsidian。
  - 撰寫第一個單元的學習筆記。
- **踩坑紀錄/特別注意**：
  - **Windows 上的 GitHub CLI 登入問題**：網頁登入流在背景容易卡死在等待 Enter 鍵。改用 Personal Access Token (PAT) 登入可 100% 解決此問題。
  - **GitHub 大檔案警告**：Tibame 資料夾中有大於 70MB 的 PDF 與 zip 壓縮檔，Git 雖成功推上但觸發了 GitHub 推薦 50MB 以下的警示。後續應避免放入大於 100MB 的大檔案，或使用 Git LFS。
  - **Git 全域設定未配置**：新環境初次使用 Git 時需要先設定 `user.name` 與 `user.email`，已使用 GitHub 匿名信箱完成全域配置。
