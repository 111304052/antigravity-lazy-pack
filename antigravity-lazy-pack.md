# antigravity-lazy-pack - 專案駕駛艙

## 專案資訊
- **專案名稱**：antigravity-lazy-pack
- **主要工作目錄**：`c:\Users\leots\OneDrive\Desktop\Antigravity2.20260626`
- **GitHub Repository**：[111304052/antigravity-lazy-pack](https://github.com/111304052/antigravity-lazy-pack)
- **目前狀態**：🟢 記帳軟體與資料轉移完成，運作正常

---

## 每日工作紀錄

### 2026-06-26
- **開工確認**：專案初始化開工。
- **完成事項**：
  - 成功從 GitHub 複製 `antigravity-lazy-pack` 專案。
  - 將 7 個自訂技能複製並安裝至全域技能目錄。
  - 安裝並驗證 `notebooklm-mcp-cli`，修正啟動路徑至 `notebooklm-mcp.EXE`。
  - 安裝 GitHub CLI、Node.js，並全域安裝 `@bitbonsai/mcpvault` (Obsidian)。
  - 建立 Obsidian `Secondbrain` 庫，初始化 Git 私有庫與 Obsidian Git 自動備份（10 分鐘同步）。
- **下一步**：
  - 開始進行正式開發與筆記管理。

### 2026-06-28
- **開工確認**：執行開工檢查，Git status 乾淨。
- **完成事項**：
  - **工具與環境**：將 `gem-to-agent-kit` 上傳至個人 GitHub 私有庫；配置 Google Drive 桌面版「Gemini Gems」資料夾；安裝相依 Python 套件（`python-docx`、`python-pptx`、`edge-tts`、`yt-dlp`）。
  - **數學出題助手**：在本地建立專案並寫入 `generate_exam.py`，通過 Word 考卷生成煙霧測試。
  - **YouTube學習筆記特助**：設定真實 Gem 規則並成功解析影片字幕，批量生成結構化 Markdown 筆記並儲存至 output，生成 `concept.png` 示意圖。
- **下一步**：
  - 進行 YouTube 影片批次字幕處理與結構化筆記寫入。

### 2026-06-29
- **開工確認**：執行開工檢查，Git status 乾淨。
- **完成事項**：
  - **特助功能升級**：更新 `AGENTS.md`、`SKILL.md`，設定生圖問答機制與播放清單分組子目錄；在 Obsidian 中建立 `YouTube學習筆記` 資料夾；成功批次解析 `AntiGravity_google_AI_Agents` 播放清單共 8 部影片並完美分類歸檔。
  - **遠端連線**：設定 VS Code Remote Tunnels 與 Chrome 遠端桌面，實測手機端對電腦桌面的 100% 遠端操控與授權。
  - **行事曆整合**：配置 Google Calendar MCP 並成功進行 OAuth 2.0 驗證。
- **下一步**：
  - 進行學校行事曆向個人帳戶移轉。

### 2026-06-30
- **開工確認**：檢查規則與 Git 狀態，NotebookLM 認證過期。
- **完成事項**：
  - **工具維護**：協助執行 `nlm login`，成功恢復 NotebookLM MCP 連線狀態。
  - **行事曆移轉**：開發並執行 `migrate.js`，將 436 筆行程由學校帳戶完美移轉至個人帳戶（包含時區對齊、重複行程清除、關鍵字分色與 Reminders 保留）。
  - **隨手記開發**：開發「隨手記」記帳網頁應用程式（Node.js 本地伺服器 + PWA/iOS 全螢幕適配網頁），內建計算機鍵盤。
  - **資料轉移**：從雲端硬碟 `天天記帳` CSV 成功移轉 3,911 筆歷史明細，將「美容美髮」類別對齊為「保養」，自動計算更新帳戶餘額。
  - **App 升級與優化**：在圖表頁面新增「類別比/帳戶比/成員比」三維度分析；實作「離線暫存與自動背景同步」機制；配合「舊 App 繼續記帳 ➔ 定期匯出自動增量導入」的工作流，開發了 [import_data.py](file:///c:/Users/leots/OneDrive/Desktop/Antigravity2.20260626/accounting-app/import_data.py) 自動抓取雲端最新導出檔的腳本，並建立桌面的雙擊啟動捷徑 [一鍵導入舊帳.bat](file:///c:/Users/leots/OneDrive/Desktop/Antigravity2.20260626/一鍵導入舊帳.bat) 增量導入。
  - **YouTube學習筆記特助**：更新 `url.txt` 後，批次下載並解析全新【機器學習2026】播放清單共 11 部影片之資訊與中文 VTT 字幕；開發並執行 `write_ml2026_ordered_notes.py` 腳本，依照播放清單順序（EP01 至 EP11）批量生成結構化 Markdown 學習筆記，同步寫入本機 `output` 目錄與 Obsidian `YouTube學習筆記/【機器學習2026】` 中。
- **下一步**：
  - 交付使用者日常使用，後續若有新需求（如預算管理、其他播放清單整理）再行擴充。

### 2026-07-02
- **開工確認**：執行開工檢查，Git status 乾淨。
- **完成事項**：
  - **YouTube學習筆記特助**：更新 `url.txt` 後，批次下載並解析【n8n 工作流基礎教學】播放清單共 3 部影片之資訊與中文 VTT 字幕；開發並執行 `write_n8n_ordered_notes.py` 腳本，手動調整為正向順序（EP01 至 EP03，對應 EP.1 到 EP.3）批量生成結構化學習筆記，同步寫入本機 `output` 目錄與 Obsidian `YouTube學習筆記/n8n 工作流基礎教學` 中。
- **下一步**：
  - 繼續進行其他播放清單的整理與日常維護。

