# -*- coding: utf-8 -*-
import os
import shutil

# 定義路徑
output_base = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "output", "YouTube學習筆記特助", "三叔Sense Bar", "AntiGravity_google_AI_Agents基本功"))
obsidian_base = r"C:\Users\leots\OneDrive\文件\Secondbrain\YouTube學習筆記\三叔Sense Bar\AntiGravity_google_AI_Agents基本功"

# 1. 建立與清理目錄
if os.path.exists(output_base):
    shutil.rmtree(output_base)
if os.path.exists(obsidian_base):
    shutil.rmtree(obsidian_base)

os.makedirs(output_base, exist_ok=True)
os.makedirs(obsidian_base, exist_ok=True)

# 2. 定義影片資訊與順序 (正向排列：EP01 到 EP08)
video_list = [
    {
        "index": 1,
        "id": "LyiiMVZE7uM",
        "title": "AntiGravity 基本功 EP01:Claude Code 與 Codex 的強敵？Google AntiGravity 2.0 實測評價",
        "filename": "EP01_Google AntiGravity 2.0 實測評價.md",
        "content": """## 🧠 核心概念與技術摘要
1. **Google AntiGravity 2.0 的定位**：
   * 它是 Google 推出的強大 AI Agent 桌面代理端系統，被定位為 Codex 與 Claude Code 的直接競爭對手。它具有深度的本地文件系統存取權、瀏覽器連線及命令行指令執行功能。
2. **初始化安裝與 Lazy-Pack**：
   * 示範如何透過 `antigravity-lazy-pack`（懶人包）進行一鍵專案環境安裝與初始化，免除繁瑣的手動依賴套件配置。
3. **無中斷批次任務 (Batch Tasks)**：
   * 支持一次性將所有待辦任務以指令列表形式餵給 Agent。Agent 會在背景自動規劃並依序解決，大幅縮短每次詢問等待的時間，徹底釋放生產力。
4. **與 Codex 等介面的主要差異**：
   * 與 Codex 類似，皆為作業系統級別的 Harness，但 AntiGravity 對 Google 生態系（如 Classroom, Calendar, Drive 等）具備原生且流暢的 MCP 支援。

## ⏱️ 附時間戳記的段落大綱
* `[00:00]` 課程引言：Google AntiGravity 2.0 與其他兩大主流工具的對決與實測重點。
* `[02:00]` 登入與界面導覽：比較 AntiGravity 與 Codex 設計風格的異同。
* `[04:02]` 首次開機設定：是否接收廣告郵件與 API Token 基本認證連線。
* `[06:02]` 開源工具 OpenCode 的連動說明。
* `[08:00]` 進階設定：確認自動接受權限與白名單指令。
* `[10:03]` 與 Claude Code 介面操作細節的橫向對比。
* `[12:00]` 初始化實戰：命令 Agent 逐一檢查 AntiGravity Lazy-Pack 懶人包中的模組是否健全。
* `[14:00]` 說明若採取手動點擊核准，可能需要耗費數十分鐘的痛點。
* `[16:00]` 自動模式配置，讓 AI 代理自行修復與安裝環境依賴。
* `[18:00]` 驗證安裝結果，完成基礎包部署。
* `[20:00]` 跨工具連動（GitHub、NotebookLM）在桌面代理端的協作形式。
* `[22:00]` 解釋 Agent 讀取並執行 OpenCode 技能庫的原理。
* `[24:01]` 提問心法：一次性交付複雜的組合指令，讓 Agent 背景批次運行。
* `[26:00]` 提示詞微調：如何糾正 Agent 的格式與錯誤判斷。
* `[28:00]` 命名規則與 antigravity-lazy-pack 目錄結構定義。
* `[30:01]` 創意實測：讓 AI 延續指定的插圖風格完成簡報設計。
* `[32:00]` 實測全自動執行成效：在完全無手動干預的情況下自動完成測試。

## 🌐 中英專有名詞對照表
* **Google AntiGravity 2.0**：谷歌智能代理系統 2.0 版
* **Lazy-Pack**：懶人包 / 預裝依賴套件包
* **Batch Execution**：批次執行
* **Codex / Claude Code**：市場兩大主流 AI Agent 平台
* **Harness UI**：AI 宿主作業介面

## 🏃‍♂️ 行動指南
* 初始化您的 AntiGravity 2.0 專案目錄，確認 `antigravity-lazy-pack.md` 等核心引導文件已就位。
* 思考：在哪些情境下，使用 AntiGravity 的批次任務處理會比一問一答的對話模式更有效率？
"""
    },
    {
        "index": 2,
        "id": "U4C0dGbQtQA",
        "title": "AntiGravity基本功EP02:備課救星_極速處理教學檔案_出考卷_填文件_下載考古題_整理檔案夾",
        "filename": "EP02_極速處理教學檔案_自動整理與考卷生成.md",
        "content": """## 🧠 核心概念與技術摘要
1. **教師行政與備課自動化**：
   * 教師備課經常面臨大量雜亂檔案（如考卷、學生名冊、考古題、教學投影片）需要整理與編輯的痛點，利用 AI Agent 的手腳能力可以極速解決。
2. **自動化資料夾整理 (Clean-up Automation)**：
   * 透過複製下載資料夾路徑，讓 Agent 自動根據副檔名、檔案屬性與日期進行階層式分類歸檔。
3. **高難度考卷與文件生成**：
   * 命令 Agent 自動讀取參考教材（如 PDF、CSV），在本地生成 Word 考卷。
   * 對於數理學科，強制要求 Agent 使用標準數學格式（如 LaTeX / Markdown 數學公式）來呈現，以維持考卷排版與字體的美觀。
4. **檔案操作的安全與限制**：
   * 進行大量檔案變更或刪除操作時具有風險。必須設定確認攔截點（待核准模式），或將刪除檔案移至「待刪除」暫存資料夾，確認無誤後再手動清空。

## ⏱️ 附時間戳記的段落大綱
* `[00:00]` 課程引言：展示 Agent 自動整理完後的乾淨資料夾結構與效率對比。
* `[02:00]` 在 AntiGravity 中啟用自動化流程的步驟與權限分配。
* `[04:00]` 額度監控：如何確保 Agent 在 API 額度限制下穩定且持續地工作。
* `[06:02]` 檔案路徑複製心法：避免手動上傳大檔案，改用實體絕對路徑。
* `[08:03]` 文書操作技能：測試 AI 對 Microsoft Word 與 Excel 的讀取與改寫能力。
* `[10:00]` 實戰演示：將 GitHub 熱門 Repo 程式碼下載並複製到專案資料夾中。
* `[12:01]` 讓 Agent 讀取本機 PDF 參考書，並依據課綱出出一份測驗卷。
* `[14:01]` 數理考卷排版：命令 Agent 將所有公式渲染為標準 LaTeX 數學排版。
* `[16:01]` 考卷生成成功，自動輸出精美的 `.docx` 格式檔案。
* `[18:02]` 成績統計與分析：利用 Python 腳本對班級成績 CSV 進行複雜加權運算。
* `[20:00]` 檢視 API 的額度使用狀況，確保無爆額風險。
* `[22:01]` 刪除與歸檔的安全性探討：設定攔截點以避免誤刪檔案。
* `[24:04]` 讀者 QA：解答本機環境變數與路徑找不到的報錯問題。

## 🌐 中英專有名詞對照表
* **LaTeX Formula**：LaTeX 數學公式
* **Format Rendering**：格式渲染 / 排版美化
* **Quota / Token Limit**：API 額度 / Token 限制
* **Absolute Path**：絕對路徑
* **Safe Deletion**：安全刪除機制

## 🏃‍♂️ 行動指南
* 請 Agent 讀取一個包含學生成績的 Excel 檔，並自動生成一份 Word 格式的「學期總結報告與成績分布圖」。
* 思考：為什麼在生成數理科考卷時，堅持使用標準 LaTeX 格式是不可或缺的？
"""
    },
    {
        "index": 3,
        "id": "-oBHrpEsJs8",
        "title": "AntiGravity基本功EP03:最強備課懶人包_寫 GAS 竟然再也不用複製貼上程式碼？我是怎麼做到的.",
        "filename": "EP03_最強備課懶人包_免複製貼上開發GAS.md",
        "content": """## 🧠 核心概念與技術摘要
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
"""
    },
    {
        "index": 4,
        "id": "kmmYXntln_E",
        "title": "AntiGravity 基本功 EP04:一鍵將 Gems 全面升級成 Skill 的終極指南_懶人包大放送",
        "filename": "EP04_Gems升級為Skill的終極指南.md",
        "content": """## 🧠 核心概念與技術摘要
1. **Gemini Gems 與 AntiGravity Skills 的差異**：
   * **Gems (自訂角色)**：是 Google Gemini 網頁版提供的提示詞包包，只能進行純文字聊天，無法調用本地工具。
   * **Skills (技能)**：是 AntiGravity 專屬的擴充指令包。它不僅包含 System Prompt，還包含**可執行的 Supporting Scripts (輔助腳本)**，讓 AI 能直接調用本機程式來執行實體任務（如修圖、分析數據、生成報告）。
2. **Skills 結構與 SKILL.md**：
   * 一個標準的 Skill 資料夾必須包含一個 `SKILL.md` 檔案，頂部使用 **YAML Frontmatter** 定義技能名稱（name）與描述（description），後續寫入詳細的操作指令。
3. **全域與專案技能的優先順序**：
   * **全域技能**：加載於所有專案中。
   * **專案技能**：僅在當前專案目錄生效。避免過多的全域技能，以防關鍵字衝突或佔用不必要的 Token。
4. **自動化執行與 Turbo Mode**：
   * 在執行 Skills 時，啟用 AntiGravity 的 **Turbo Mode**，能讓 AI 自動同意輔助腳本的運行，達成無干擾的自動化工作流。

## ⏱️ 附時間戳記的段落大綱
* `[00:00]` 課程引言：為什麼要將雲端的 Gems 升級為本地的 Skills，兩者能力差在哪？
* `[02:01]` Skills 技能目錄的實體結構與核心檔案（SKILL.md）配置。
* `[04:01]` 知識的系統化輸出：如何在 Markdown 中撰寫結構化的 Prompt 行為約束。
* `[06:02]` 實戰演示：建立一個「Word 審題報告生成助手」技能。
* `[08:01]` 探討雲端硬碟備份：如何將本地的 Skills 自動同步備份至 Google Drive。
* `[10:00]` 技能加載機制：Agent 如何掃描資料夾並解析 YAML Frontmatter。
* `[12:00]` 為了避免彈出確認框，啟用 Turbo Mode 進行無感授權。
* `[14:01]` 實測「審題報告」技能，AI 讀取學生答案 Word 並自動產出修正意見。
* `[16:00]` 專案目錄與全域目錄（Global vs Project-Scoped）技能隔離設定。
* `[18:01]` 驚人的生成速度：實測不到一分鐘便完成整份報告的分析與導出。

## 🌐 中英專有名詞對照表
* **Gemini Gems**：Gemini 網頁版角色設定 (提示詞包)
* **AntiGravity Skills**：AntiGravity 本機可執行技能包
* **YAML Frontmatter**：YAML 格式的前置中繼資料
* **Supporting Scripts**：輔助執行腳本
* **Turbo Mode**：免點擊自動授權模式

## 🏃‍♂️ 行動指南
* 將您最常用的一個 Gemini Gem 角色提示詞，改寫為符合 `SKILL.md` 規範的 Markdown 文件，並放入專案的 `skills/` 目錄中進行測試。
* 思考：相較於單純的提示詞（Gems），Skills 結合「輔助腳本」後能解決哪些 Gems 無法處理的實體任務？
"""
    },
    {
        "index": 5,
        "id": "hRdQCQSozY0",
        "title": "AntiGravity 基本功 EP05:用AI打造教學網頁的5個階段_從純前端到語音AI助教全攻略",
        "filename": "EP05_用AI打造教學網頁的五個階段.md",
        "content": """## 🧠 核心概念與技術摘要
1. **AI 輔助網頁開發的五個發展階段**：
   * **階段一：純前端網頁**：只有 HTML/CSS/JS，資料刷新即消失，適合單機小工具或測驗。
   * **階段二：結合輕後端**：使用 Google Sheets 作為簡易資料庫，透過 API 存取與寫入班級學習數據。
   * **階段三：多人互動/遊戲化**：加入 Socket 或即時同步機制，讓全班學生能即時對戰或協作。
   * **階段四：實時資料庫應用**：引入 Firebase 等 NoSQL 資料庫，儲存更複雜的學生作答明細與學習軌跡。
   * **階段五：語音 AI 助教**：整合即時語音對話 API（如 Gemini Multimodal Live API），打造能與學生口語交談的專屬 AI 導師。
2. **使用 Google Sheets 作為資料庫**：
   * 開發門檻極低，非常適合教師。學生在前台作答，後台試算表即時新增數據，方便教師進行教學大綱微調與課堂分析。
3. **API Key 安全規範**：
   * 在網頁中串接 AI API（如 OpenAI 或 Gemini Key）時，應注意安全規範，避免金鑰直接暴露在前台代碼中被他人盜刷。

## ⏱️ 附時間戳記的段落大綱
* `[00:01]` 課程引言：教學網頁開發的五個發展階段與實踐藍圖。
* `[02:02]` 必備基礎：實踐網頁自動化開發前的本地 Node.js 與環境配置。
* `[04:01]` 階段一（純前端）網頁的特性：快速、單機、無狀態保存。
* `[06:00]` 階段二（Google Sheet 後端）架構：如何將試算表當成免費資料庫。
* `[08:01]` 教師視角：如何利用後台試算表即時掌握學生的作答進度。
* `[10:01]` 階段三（多人即時對戰）開發：課堂遊戲化設計（以對戰遊戲為例）。
* `[12:01]` 階段四（Firebase 資料庫）整合，提升資料讀寫的穩定度與複雜查詢能力。
* `[14:01]` 探討輕後端在行政減災與教學統計上的具體應用案例。
* `[16:01]` 階段五（語音 AI 助教）前瞻：Gemini Live 語音對話介面串接。
* `[18:00]` 學生課堂操作演示：即時數據圖表化呈現。
* `[20:01]` 實戰演示：如何命令 Agent 在五秒內生成一個純前端計算機網頁。
* `[24:02]` 數據保存機制：將學生的遊戲積分存入本地 JSON 並自動備份。
* `[26:00]` 雙人對戰模式聯機實測。
* `[30:02]` API 密鑰獲取與安全防護設定指引。

## 🌐 中英專有名詞對照表
* **Pure Frontend**：純前端網頁
* **Google Sheet DB**：將試算表作為資料庫
* **Gamification**：教學遊戲化
* **Firebase / NoSQL**：谷歌雲端實時資料庫
* **Live Audio API**：即時語音對話介面

## 🏃‍♂️ 行動指南
* 請您的 Agent 寫一個簡單的 HTML 表單網頁，並串接您現有的 Google 試算表，實測「前台提交、後台寫入」的輕後端架構。
* 思考：在課堂教學中，引進「階段五：語音 AI 助教」可以如何輔助外語口說教學或個別指導？
"""
    },
    {
        "index": 6,
        "id": "vYb87aqvBuE",
        "title": "Antigravity 基本功 EP06:全面代理你的 Google Classroom_派作業、收作業、批改一次搞定：AI × Google Classroom 完整教學",
        "filename": "EP06_全面代理Google Classroom_派作業與批改自動化.md",
        "content": """## 🧠 核心概念與技術摘要
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
"""
    },
    {
        "index": 7,
        "id": "wrSYyOxf7n4",
        "title": "AntiGravity 基本功 EP07:一句話生成 Padlet 課程牆_分區、投票、AI 插圖全自動完成",
        "filename": "EP07_一句話生成Padlet課程牆_API自動化實戰.md",
        "content": """## 🧠 核心概念與技術摘要
1. **Padlet 課程牆自動化**：
   * Padlet 是教師常用的數位看板工具。透過 Padlet 官方 API，AI Agent 可以實現「一句話自動建牆」，包括自動劃分分區（Sections）、開啟投票與留言功能、並自動生成貼文。
2. **API 金鑰與 Repo 設定**：
   * 取得 Padlet 帳戶的 API Key。
   * 將專用的 Padlet 技能代碼庫（Repository）網址複製並導入本地 Agent 的專案路徑中。
3. **AI 自動配圖與內容整理**：
   * AI 不僅能撰寫看板內容，還能呼叫影像模型生成符合課程主題的 AI 插圖（AI Illustrations），直接配圖貼在牆上。
4. **API 限制與衝突排除**：
   * 在實作「自動點愛心」或高頻率寫入時，可能會與 Padlet 官方 API 的頻率限制或特定欄位規則產生衝突。
   * 透過修改本地 Python 介接程式碼或調整 API 參數，即可順利排除衝突。

## ⏱️ 附時間戳記的段落大綱
* `[00:00]` 課程引言：展示如何用一句話生成精美排版、帶有 AI 配圖與分區的 Padlet 課程牆。
* `[02:01]` AntiGravity 桌面版與命令列 CLI 版本的 API 連線路徑說明。
* `[04:02]` 實戰演示：將 Padlet 專用 Repo 網址複製並導入 Agent 專案目錄下。
* `[06:01]` 說明不同 Agent 工具載入第三方 Repo 與技能包的指令差異。
* `[08:01]` 任務範例：請 Agent 規劃一個「統計迷思」單元的下堂課重點整理看板。
* `[10:02]` 在 Agent 內直接設定 Padlet 課程牆的主題、分區標題與投票規則。
* `[12:04]` 填入 Padlet API Key，建立安全的 HTTPS 請求通道。
* `[14:01]` AI 插圖自動生成：調用圖像 API 為每篇貼文生成關聯的視覺插圖。
* `[16:01]` 看板自動生成成功，展示前台網頁的精美分區與插圖效果。
* `[18:01]` 安全與授權檢查：確認 AI 在後台呼叫 API 時的放行紀錄。
* `[20:00]` 故障排除：分析自動點愛心操作時，因 Padlet 官方限制產生的 API 衝突。
* `[22:00]` 程式碼微調：修改 Python 腳本中的 HTTP Header 排除衝突。
* `[26:01]` 彙整複習：如何讓 AI 整理舊的課程看板，重新分類至新看板中。

## 🌐 中英專有名詞對照表
* **Padlet Board**：Padlet 數位課程牆/看板
* **API Key**：應用程式介面金鑰
* **Sectioning**：看板分區排版
* **AI Illustration**：AI 自動生成配圖
* **API Collision**：API 規則衝突

## 🏃‍♂️ 行動指南
* 請 Agent 讀取一篇教學文章，並自動在您的 Padlet 帳號中建置一個「分區重點整理看板」，每個分區包含一則重點摘錄貼文。
* 思考：在小組協作中，利用 AI 自動生成 Padlet 看板架構，可以如何加速學生的課堂討論與發表？
"""
    },
    {
        "index": 8,
        "id": "EVREOkL4wkc",
        "title": "Anti gravity EP08：Agent代理 複製你的聲音_別再付費買 AI 語音了！一行指令免費複製你的聲音",
        "filename": "EP08_Agent語音代理_免付費複製你的聲音.md",
        "content": """## 🧠 核心概念與技術摘要
1. **本機語音複製 (Local Voice Cloning)**：
   * 傳統語音複製需要付費訂閱雲端服務。利用 AI Agent 可以在本機免費實現高品質的聲音克隆（Voice Cloning）。
2. **語音克隆工作流**：
   * **步驟一：錄製樣本**：提供或即時錄製一段 10 至 30 秒清晰、無背景雜音的個人聲音樣本。
   * **步驟二：寫入程式**：Agent 在背景調用本機 Python TTS（Text-to-Speech）腳本。
   * **步驟三：語音合成**：輸入任意文字，AI 將以您的聲音特徵朗讀出來，生成 `.wav` 或 `.mp3` 檔案。
3. **語音助理整合**：
   * 複製聲音後，可以將其設定為您的本地語音助理（如為語音助教命名為「三叔」或「小克」）的發聲大腦，實現「用您自己的聲音回答您的問題」。
4. **自動化放行設定**：
   * 語音複製涉及大量的本地音訊檔案編解碼與 Python 腳本運行，務必開啟白名單指令放行，以提升合成速度。

## ⏱️ 附時間戳記的段落大綱
* `[00:00]` 課程引言：展示語音複製前後的聲音對比，說明免付費複製個人聲音的強大之處。
* `[02:00]` 語音複製在教學影音製作、遠距教材中的應用場景。
* `[04:03]` 設定 AntiGravity 自動放行模式，加速音訊編碼依賴套件的安裝。
* `[06:00]` 使用 NPM 與 Python 安裝本地語音克隆所需的 TTS 套件。
* `[08:00]` 探討市面上付費語音克隆工具的收費模式與本地免費替代方案的優勢。
* `[10:00]` 設計前端錄音網頁，將錄製好的音訊路徑貼給 Agent。
* `[12:03]` 實戰演示：現場錄製一段聲音樣本，系統回傳錄製成功。
* `[14:00]` Agent 自動讀取聲音 WAV 檔，進行特徵值提取與音素分析。
* `[16:01]` 語音生成測試：完全由 AI 在背景執行，無需手動寫代碼。
* `[18:02]` 生成任意文字語音：將合成出的語音檔案播放，音色與講者極高相似。
* `[20:02]` 如何將生成的語音檔案替換至您的教學投影片或影片剪輯軌道中。
* `[24:01]` 整合實戰：讓本地 AI 語音助教「小克」用三叔的聲音進行實時互動。
* `[28:02]` 介紹 HyperFrame 音訊同步架構。
* `[32:01]` 使用 Python 自動編譯音訊與文字對齊的實用範例。

## 🌐 中英專有名詞對照表
* **Voice Cloning**：語音克隆 / 聲音複製
* **TTS (Text-to-Speech)**：文字轉語音
* **Audio Encoder / Decoder**：音訊編解碼器
* **Voice Assistant**：語音助理
* **Acoustic Features**：聲學特徵值 / 音素

## 🏃‍♂️ 行動指南
* 錄製一段 15 秒的自我介紹音檔，請您的 Agent 利用 Python 本地 TTS 庫將這段音檔作為 Mock 聲音，並用該聲音朗讀「歡迎來到 AI 智能代理學習課堂」。
* 思考：在數位教材製作中，使用「教師個人克隆語音」相比於 generic 的機器語音，對於學生的專注度與親切感有何提升？
"""
    }
]

# 3. 執行寫入
success_count = 0
for video in video_list:
    v_id = video["id"]
    title = video["title"]
    index = video["index"]
    fname = video["filename"]
    
    content = f"""# 🎥 {title}

## 📌 影片資訊
* **播放清單序號**：EP{index:02d}
* **影片 ID**：{v_id}
* **原始網址**：https://www.youtube.com/watch?v={v_id}
* **播放清單**：AntiGravity_google_AI_Agents基本功
* **講者**：三叔Sense Bar
* **創作者**：三叔Sense Bar

---

""" + video["content"]
    
    # 寫入專案 output 目錄
    out_path = os.path.join(output_base, fname)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    # 寫入 Obsidian
    obs_path = os.path.join(obsidian_base, fname)
    with open(obs_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    success_count += 1

print(f"[SUCCESS] Re-structured and generated {success_count} AntiGravity basic notes successfully!")
