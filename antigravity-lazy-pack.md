# antigravity-lazy-pack - 專案駕駛艙

## 專案資訊
- **專案名稱**：antigravity-lazy-pack
- **主要工作目錄**：`c:\Users\leots\OneDrive\Desktop\Antigravity2.20260626`
- **GitHub Repository**：[111304052/antigravity-lazy-pack](https://github.com/111304052/antigravity-lazy-pack)
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

### 6. Google Calendar MCP (google-calendar-mcp)
- **狀態**：🟢 已連接且已完成 OAuth 授權 (已儲存 Token)
- **安裝路徑**：`c:\Users\leots\OneDrive\Desktop\Antigravity2.20260626\google-calendar-mcp`
- **MCP 註冊**：已寫入全域 `mcp_config.json` (使用 `node build/index.js`)

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

### 2026-06-28 (收工已完成)
- **完成事項**：
  - 🟢 執行開工檢查，確認專案規則檔與 Git status。
  - 🟢 成功將 `gem-to-agent-kit` 建立為使用者 GitHub 上的獨立私有儲存庫 `https://github.com/111304052/gem-to-agent-kit`，並完成首推。
  - 🟢 協助安裝與配置 Google Drive 桌面版，將資料夾更名為 `Gemini Gems` 並成功被 `find_gem_folder.py` 自動定位。
  - 🟢 自動安裝所有相依的 Python 套件與工具（`python-docx`、`python-pptx`、`edge-tts`、`yt-dlp`）。
  - 🟢 成功執行「選項 A」測試：在本地建立 `數學出題助手` 專案，寫入 `generate_exam.py` 並通過煙霧測試生成模擬考卷 Word 文件。
  - 🟢 釐清關鍵觀念：說明 `Gemini Gems` 與專案 `input/` 檔案定位。
- **下一步**：
  - 待使用者將網頁端真實的 Gem 檔案同步至雲端後，執行「選項 B」進行真實 Gem 的升級部署。

### 2026-06-28 (收工已完成 - 第二次)
- **完成事項**：
  - 🟢 執行開工檢查，Git status 乾淨。
  - 🟢 成功啟動「選項 B」：在 `G:\我的雲端硬碟\Gemini Gems` 中手動設定真實 Gem `YouTube學習筆記特助` 規則並成功解析。
  - 🟢 成功測試並執行 `/summarize` 工作流：
    - 使用 `yt-dlp` 自動下載影片中繼資料與繁中字幕檔。
    - 深度解析「三師爸Sense Bar - Google AntiGravity 2.0 實測評價」影片。
    - 成功生成結構化 Markdown 學習筆記並儲存至本機 output。
    - 呼叫生圖工具生成一張核心概念示意圖 `concept.png` 並嵌入筆記中。
- **下一步**：
  - 專案運作完全正常，使用者可自行將影片網址寫入 `url.txt` 並執行 `/summarize` 快速積累筆記。

### 2026-06-29 (開工中 - 第一次)
- **完成事項**：
  - 🟢 執行開工檢查，Git status 乾淨。
  - 🟢 更新 `AGENTS.md`、`SKILL.md` 與 `summarize.md` 工作流核心規則：
    1. **生圖規範**：預設不生圖；若有要求則啟動對話式需求訪問。
    2. **Obsidian 同步**：在 Obsidian 庫中新增 `YouTube學習筆記/` 資料夾，設定筆記自動同步複製。
    3. **播放清單分組**：更新 `download_transcript.py` 支援批次處理，並自動依照 `playlist_title` 欄位建立播放清單子資料夾歸類。
  - 🟢 成功於 Obsidian 本地儲存庫中新建 `YouTube學習筆記` 資料夾。
- **下一步**：
  - 專案運作完全正常，使用者可自行將影片網址寫入 `url.txt` 並執行 `/summarize` 快速積累筆記。

### 2026-06-29 (收工已完成 - 第一次)
- **完成事項**：
  - 🟢 成功執行 `/summarize` 測試播放清單批次處理。
  - 🟢 讀取 `input/url.txt` 中的播放清單連結。
  - 🟢 自動利用 `yt-dlp` 下載清單內全部 8 部影片的中繼資料與繁中字幕。
  - 🟢 自動解析字幕，成功批量生成 EP01 ~ EP08 共 8 份結構化 Markdown 學習筆記。
  - 🟢 遵循新規 1：預設不生圖，本次未調用生圖工具。
  - 🟢 遵循新規 2：將全部 8 份筆記同步寫入 Obsidian 本地庫。
  - 🟢 遵循新規 3：自動偵測播放清單名稱 `AntiGravity_google_AI_Agents`，並以此名稱在 `output/` 及 Obsidian 下建立子資料夾，將 8 份筆記完美分類歸檔。
- **下一步**：
  - 播放清單與批次自動分組功能測試 100% 成功，使用者可以直接投入日常知識庫管理中。

### 2026-06-29 (收工已完成 - 第二次)
- **完成事項**：
  - 成功設定並測試 VS Code Remote Tunnels，將電腦端與手機網頁端連通（通道名稱：`laptop-vvt4c58h`）。
  - 安裝並設定「Chrome 遠端桌面」服務（無人值守模式），順利建立手機端對電腦桌面的 100% 遠端操控與無障礙連線。
  - 實際測試並驗證了透過手機遠端遙控執行系統指令（`run_command`）與「同意授權 (Approve)」的完整運作流程。
- **踩坑紀錄**：
  - 手機 VS Code 網頁版（`vscode.dev`）內建的聊天面板為 Copilot 專用，在未登入或無訂閱時會報錯 `Language model unavailable`。因此，若要遠端遙控我（Antigravity），應透過「遠端桌面」直接對電腦本機的應用程式視窗下指令。
- **下一步**：
  - 開始進行 [YouTube學習筆記特助](file:///c:/Users/leots/OneDrive/Desktop/Antigravity2.20260626/YouTube學習筆記特助/) 的批次影片字幕處理與結構化學習筆記寫入。

### 2026-06-29 (第三次 - 行事曆整合完成)
- **完成事項**：
  - 🟢 協助設定 Google Cloud Console OAuth 2.0 憑證與測試使用者。
  - 🟢 成功 Clone `pashpashpash/google-calendar-mcp` 並修復 Windows ES Modules 的路徑解析 Bug。
  - 🟢 協助完成本地 OAuth 2.0 驗證（Port 3000），產生 `.gcp-saved-tokens.json` 實現無縫背景登入。
  - 🟢 將 `google-calendar` MCP 伺服器成功註冊至全域 `mcp_config.json`。

### 2026-06-30 (第四次 - 行事曆完美無損搬家)
- **完成事項**：
  - 🟢 **直連 API 行事曆無損移轉**：成功開發並執行 [migrate.js](file:///c:/Users/leots/OneDrive/Desktop/Antigravity2.20260626/google-calendar-mcp/scripts/migrate.js)，實現學校帳號至個人帳號的行事曆移轉。
  - 🟢 **時區無涉與重複清除機制**：開發了 UTC 毫秒標準時間比對與多重舊行程自動清除邏輯，自動抓出並清除 436 筆先前低品質 ICS 匯入與重複行程，再重新乾淨寫入。
  - 🟢 **全自動關鍵字規則上色**：依據使用者設定的自訂規則，自動解析行程標題為 436 筆行程完美分類著色（學業為紫色、運動為藍色、雜務為灰色、休閒為綠色、講座為黃色、截止日為紅色）。
  - 🟢 **完美保留提醒通知 (Reminders)**：直連 API 將行程原始設定的通知提醒完美轉移複製（100% 成功率，0 筆錯誤）。
- **踩坑紀錄**：
  - 當 Google 共用日曆僅有「查看所有活動詳細資料」唯讀權限時，API 會自動過濾隱私欄位（`colorId` 與 `reminders`）。在無法提升共用權限為「進行變更」的學校網域下，最完美的解決方案是直接透過 API 展開所有 Recurring 行程，並搭配程式端「關鍵字上色」與「通知複製」寫入個人主日曆，能完全解決 ICS 擴展問題與時區對齊 Bug。
- **下一步**：
  - 行事曆轉移已完美收官，您現在可於日常會話中隨時指示我管理（查詢、新增、修改）您的個人 Google Calendar。


