# antigravity-lazy-pack - 專案駕駛艙

## 專案資訊
- **專案名稱**：antigravity-lazy-pack
- **主要工作目錄**：`c:\Users\leots\OneDrive\Desktop\Antigravity2.20260626`
- **GitHub Repository**：[mathruffian-dot/antigravity-lazy-pack](https://github.com/mathruffian-dot/antigravity-lazy-pack)
- **目前狀態**：🟢 服務連接與全自動工作流設定完成

---

## 服務狀態與設定紀錄

### 1. NotebookLM MCP (01-notebooklm)
- **狀態**：🟢 已連接 ( leotsai0508@gmail.com )
- **安裝路徑**：`C:\Users\leots\anaconda3\Scripts\nlm.EXE`
- **MCP 註冊**：已寫入全域 `mcp_config.json`（已修正為直接呼叫 `notebooklm-mcp.EXE`）

### 2. GitHub CLI (02-github)
- **狀態**：🟢 已安裝且已完成 Web 登入
- **版本**：gh version 2.95.0
- **MCP 註冊**：使用內建 Git 工具搭配 GitHub CLI 執行

### 3. Firebase MCP (03-firebase)
- **狀態**：🟢 已安裝且已完成 Web 登入
- **MCP 註冊**：已寫入全域 `mcp_config.json` (使用 `npx.cmd -y firebase-tools@latest mcp`)

### 4. Obsidian MCP (06-obsidian)
- **狀態**：🟢 已安裝且已建立儲存庫
- **儲存庫路徑**：`C:\Users\leots\OneDrive\文件\Secondbrain`
- **MCP 註冊**：已寫入全域 `mcp_config.json` (使用 `mcpvault`)

### 5. Obsidian Git 自動備份
- **狀態**：🟢 已設定背景全自動同步
- **私有備份庫**：[https://github.com/111304052/secondbrain-vault](https://github.com/111304052/secondbrain-vault) (Private)
- **同步機制**：自動提交與同步間隔 10 分鐘，自動拉取間隔 10 分鐘，並配置專用 `.gitignore` 防衝突。

---

## 每日工作紀錄

### 2026-06-26
- **完成事項**：
  - 成功從 GitHub 複製 `antigravity-lazy-pack` 專案。
  - 將 7 個懶人包技能（00 至 06）複製並安裝至全域自訂技能目錄。
  - 安裝並驗證 `notebooklm-mcp-cli`，修正啟動路徑至 `notebooklm-mcp.EXE` 解決 MCP Error。
  - 透過 `winget` 自動安裝 **GitHub CLI** 與 **Node.js LTS**。
  - 全域安裝 `@bitbonsai/mcpvault` (Obsidian MCP 伺服器)。
  - 建立全新 Obsidian 儲存庫 `Secondbrain` 並初始化專案駕駛艙。
  - 完成 `mcp_config.json` 註冊設定，整合 NotebookLM、Firebase、Obsidian。
  - 於專案根目錄建立 `ANTIGRAVITY.md` 規則檔案。
  - 為本地 Obsidian 儲存庫進行 Git 初始化，配置排除暫存檔的 `.gitignore`。
  - 在 GitHub 上建立私有儲存庫 `secondbrain-vault` 並完成首次推送。
  - 引導使用者在 Obsidian 軟體中成功安裝並啟用 `Obsidian Git` 插件，設定每 10 分鐘自動雙向同步。
- **下一步**：
  - 專案連接與自動化備份已全部就緒，可開始進行正式開發與筆記管理。
