# -*- coding: utf-8 -*-
import os
import sys

# 定義寫入目錄路徑
output_base = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "output", "YouTube學習筆記特助", "AntiGravity_google_AI_Agents"))
obsidian_base = r"C:\Users\leots\OneDrive\文件\Secondbrain\YouTube學習筆記\AntiGravity_google_AI_Agents"

os.makedirs(output_base, exist_ok=True)
os.makedirs(obsidian_base, exist_ok=True)

# 筆記內容定義
notes = {}

# ==========================================================
# EP01
# ==========================================================
notes["EP01_Google_AntiGravity_2.0_實測評價.md"] = """# 🎥 AntiGravity 基本功 EP01：Google AntiGravity 2.0 實測評價與四大天王 AI Agent 對決

## 📌 影片資訊
* **標題**：AntiGravity 基本功 EP01:Claude Code 與 Codex 的強敵？Google AntiGravity 2.0 實測評價
* **講者/頻道**：三師爸Sense Bar
* **原始網址**：https://www.youtube.com/watch?v=LyiiMVZE7uM
* **播放清單**：AntiGravity_google_AI_Agents

## 🧠 核心概念與技術摘要
1. **四大 AI Agent 對齊**：
   * 本機 AI 開發特助市場目前有四大主力：**Claude Code**、**Codex**、**OpenCode** 以及最新的 **AntiGravity 2.0**。這些工具都具備在終端機自動跑腳本、寫程式及讀取檔案的能力。
2. **MCP (Model Context Protocol) 整合**：
   * 影片展示了整合 `NotebookLM MCP` 讀取雲端筆記、`Obsidian MCP` 讀寫本地筆記、以及 `Firebase MCP` 讀取資料庫。
3. **自動核准 (Always Proceed) 與 Turbo Mode**：
   * 為防止 Agent 每次執行命令時都要人類按 Confirm（確認），須在設定中將 JavaScript、Browser、Terminal 等權限設為 **Always Proceed**，或開啟 **Turbo Mode**。
4. **Imagen 內建生圖實測**：
   * 原生提供 Imagen 生圖引擎，雖然目前限制在 1:1，但中文生成與多格漫畫（manga）處理非常方便。

## 🏃‍♂️ 行動指南
* 下載 AntiGravity 2.0 Windows 版。
* 設定連線 GitHub、Obsidian 與 NotebookLM 的 MCP 配置。
* 將工作目錄的自動化確認權限全部設為 `Always Proceed`。
"""

# ==========================================================
# EP02
# ==========================================================
notes["EP02_備課神器_自動處理多個Word_Ppt檔案與出題.md"] = """# 🎥 AntiGravity 基本功 EP02：備課神器（自動處理多個 Word/Ppt 與 PDF OCR 出題）

## 📌 影片資訊
* **標題**：AntiGravity基本功EP02:備課神器_自動處理多個Word/Ppt簡報檔案_隨機出題...
* **講者/頻道**：三師爸Sense Bar
* **原始網址**：https://www.youtube.com/watch?v=U4C0dGbQtQA
* **播放清單**：AntiGravity_google_AI_Agents

## 🧠 核心概念與技術摘要
1. **教學檔案急速批次處理**：
   * 展示如何讓 Agent 自動去網路上下載歷屆國中教育會考數學題 PDF 檔案到本地專案目錄。
2. **PDF OCR 數學解題實測**：
   * 測試 AntiGravity 讀取 PDF 當中特定的數學幾何選擇題（例如 110 年第 4 題），AI 能直接理解幾何圖形結構、解釋算式並寫出正確解答（選 C）。
3. **自訂 Word 與 PPT 產生腳本**：
   * 利用 Python 的 `python-docx` 與 `python-pptx` 套件，讓 Agent 讀取外部規格文件，直接生成排版精美的考卷 Word 檔與簡報 PPT 檔。
4. **跨 Agent 技能（Skills）移植**：
   * 展示將 Claude Code 寫好的 Markdown 格式技能（Skills）直接丟給 AntiGravity，它同樣能完美讀懂並成功安裝與執行。

## 🏃‍♂️ 行動指南
* 本地安裝 `python-docx` 與 `python-pptx` 函式庫。
* 設計一個 `math_reference.docx` 放置出題標準。
* 丟給 Agent 會考 PDF，下指令「讀取並解析第 N 題」測試 OCR 精準度。
"""

# ==========================================================
# EP03
# ==========================================================
notes["EP03_試卷批改助手_GAS與Netlify閉環系統.md"] = """# 🎥 AntiGravity 基本功 EP03：試卷批改助手（GAS 與 Netlify 零複製雙向閉環系統）

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
"""

# ==========================================================
# EP04
# ==========================================================
notes["EP04_Gems升級_自訂Skill與工作流定義.md"] = """# 🎥 AntiGravity 基本功 EP04：Gems 升級（自訂 Skill 與 Agent 工作流優勢對比）

## 📌 影片資訊
* **標題**：AntiGravity 基本功 EP04: 自訂 Gems 核心 Skill 與工作流定義...
* **講者/頻道**：三師爸Sense Bar
* **原始網址**：https://www.youtube.com/watch?v=kmmYXntln_E
* **播放清單**：AntiGravity_google_AI_Agents

## 🧠 核心概念與技術摘要
1. **傳統 Gems 網頁版限制**：
   * 傳統網頁版 Gems 只能做單純的對話與生圖，有 10 個知識檔案上傳限制，無法執行本地 Python 腳本、無法控制電腦檔案、無法進行批次工作流。
2. **Gems 升級為本地 Agent**：
   * 將 Gems 指令寫成 `SKILL.md` 與工作流定義。升級後，AI 成為具備本機執行權的 Agent，擁有 code execution（程式執行）、終端控制與無限制讀寫本地檔案的能力。
3. **生圖與工作流整合**：
   * 在工作流中，生圖不再只是對話展示，而是可以「將生好的圖片直接寫入 Word 檔中」或「自動掛載在 Web 網頁目錄中」。
4. **Imagen 生圖中文化測試**：
   * 實測 Imagen 引擎（在影片中被稱為 Nano Banana Pro）在 50 個中文字內的繁體字生成及多格漫畫風格，中文識別度高，但目前強制 1:1 的解析度。

## 🏃‍♂️ 行動指南
* 寫一份 `SKILL.md` 定義您的 Agent 大腦說明書。
* 撰寫 `AGENTS.md` 做為本機專案的全局入口守則。
* 測試生圖工作流，將產出的圖片用 Python 嵌入到考卷或教材文件中。
"""

# ==========================================================
# EP05
# ==========================================================
notes["EP05_AI語音教學卡_App五個等級與語音生成.md"] = """# 🎥 AntiGravity 基本功 EP05：AI 語音教學卡（App 五個等級與 edge-tts 免費語音生成）

## 📌 影片資訊
* **標題**：AntiGravity 基本功 EP05: AI語音教學卡製作五步驟...
* **講者/頻道**：三師爸Sense Bar
* **原始網址**：https://www.youtube.com/watch?v=hRdQCQSozY0
* **播放清單**：AntiGravity_google_AI_Agents

## 🧠 核心概念與技術摘要
1. **教學應用程式的 5 個階級 (Levels)**：
   * **L1 前端靜態網頁**：沒有資料庫、不需記住資料，單純網頁互動。
   * **L2 網頁 + Google Sheets**：用 Google 試算表存資料，開發簡單，但高並發（很多人同時寫入）時會有卡頓延遲。
   * **L3 網頁 + 專業資料庫 (Firebase/Supabase)**：零延遲、即時更新，適合即時多人在線互動（如文字雲、線上對戰）。
   * **L4 網頁 + AI API (Groq/Gemini)**：利用單一後端 Key 讓整班學生免註冊帳號，即可與 AI 進行思考對話。
   * **L5 本地 AI Agent 連線**：全面託管，AI 直接跑 Python 產出實體媒體與排版檔案。
2. **edge-tts 實現免費高品質 TTS**：
   * 無須購買昂貴的 OpenAI/Google TTS API，利用 Python `edge-tts` 套件，可以直接抓取微軟 Edge 瀏覽器的語音引擎，免費生成高品質的中英文語音 MP3。
3. **AI 語音卡自動化工作流**：
   * 寫入單字與釋義 ➔ Python 自動生成 MP3 ➔ 自動寫入 HTML5 audio 播放網頁 ➔ 部署到 Netlify。

## 🏃‍♂️ 行動指南
* 本地安裝 `pip install edge-tts`。
* 申請 Groq 的免費 API Key 來獲得高速文字推理。
* 實作語音生成腳本，讓 Agent 自動為學習單單字生成語音檔。
"""

# ==========================================================
# EP06
# ==========================================================
notes["EP06_Google_Classroom_全面接管作業派發.md"] = """# 🎥 AntiGravity 基本功 EP06：Google Classroom 全面代理（OAuth 串接與作業自動派發）

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
"""

# ==========================================================
# EP07
# ==========================================================
notes["EP07_Padlet課程看板_一鍵生成與自動化控制.md"] = """# 🎥 AntiGravity 基本功 EP07：一鍵生成 Padlet 課程看板（Padlet MCP 自動化接管）

## 📌 影片資訊
* **標題**：AntiGravity 基本功 EP07: 一鍵生成 Padlet 課程看板...
* **講者/頻道**：三師爸Sense Bar
* **原始網址**：https://www.youtube.com/watch?v=wrSYyOxf7n4
* **播放清單**：AntiGravity_google_AI_Agents

## 🧠 核心概念與技術摘要
1. **自製 Padlet MCP Server**：
   * 由於官方提供的 Padlet 整合極為陽春，講者自行開發了全功能的 Padlet MCP Server 並在 GitHub 上開源。
2. **全面接管 Padlet 功能**：
   * 安裝此 MCP 後，AI Agent 可以透過 API 直接在指定的 Padlet 看板上新增卡片（Posts）、上傳圖片與連結、自動建立投票活動。
3. **學生互動與回覆自動化**：
   * Agent 能定時下載 Padlet 板上學生的上傳檔案與附件，並根據內容自動撰寫批改回饋，回覆在 Padlet 該卡片的留言板（Comments）中。
4. **開發人員 Key 與權限**：
   * 需要擁有付費/教育版的 Padlet 帳號，並在「設定」➔「開發人員」中產生專屬的 API Key，交給 Agent 來進行配置。

## 🏃‍♂️ 行動指南
* 前往 Padlet 右上角設定 ➔ 開發人員，新增並取得 API Key。
* 從 GitHub 下載講者開源的 Padlet MCP 並由 Agent 進行 npm install。
* 執行測試：下令讓 Agent 在 Padlet 板上新增一個「今日簽到與意見調查」卡片。
"""

# ==========================================================
# EP08
# ==========================================================
notes["EP08_免費複製聲音_VoxCPM2開源模型實測.md"] = """# 🎥 AntiGravity 基本功 EP08：免費複製你的聲音（VoxCPM2 / Voice Cloner 開源 TTS 實測）

## 📌 影片資訊
* **標題**：Anti gravity EP08: Agent代理 複製你的聲音_別再付費買 AI 語音了！一行指令免費複製你的聲音
* **講者/頻道**：三師爸Sense Bar
* **原始網址**：https://www.youtube.com/watch?v=EVREOkL4wkc
* **播放清單**：AntiGravity_google_AI_Agents

## 🧠 核心概念與技術摘要
1. **免費高品質開源語音複製**：
   * 介紹高級的開源語音複製與 TTS 模型（如 Voice Cloner、VoxCPM2），可以商用且完全免費，用於替代付費的語音合成服務。
2. **硬體需求與 3D 加速 (GPU)**：
   * 雖然沒有 GPU 3D 加速卡的普通文書筆電也能執行（使用 CPU 緩慢生成），但如果電腦配有 NVIDIA 顯示卡並啟用 CUDA 3D 加速，生成速度將會有數十倍的提升。
3. **本機執行與安全隱私**：
   * 聲音模型完全在本地電腦運行，所有聲音複製訓練與生成不需要上傳到任何雲端伺服器，保證極高的聲音隱私安全。
4. **連線與用量保證**：
   * 在本地編譯與下載大體積的開源模型權重檔案前，必須確保 AI Agent 本身具備足夠的 quota 與額度（建議使用付費版 AntiGravity 以免在下載解壓過程中額度耗盡）。

## 🏃‍♂️ 行動指南
* 取得講者提供的 Voice Cloner / VoxCPM2 GitHub repo。
* 檢查電腦是否裝有 NVIDIA 驅動與 CUDA 工具包。
* 提供一段 5-10 秒的個人聲音乾淨音軌作為 Sample，讓 Agent 自動訓練並生成您個人音色的第一段文字配音。
"""

# 寫入檔案
for fname, content in notes.items():
    # 寫入專案 output
    out_path = os.path.join(output_base, fname)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    # 寫入 Obsidian
    obs_path = os.path.join(obsidian_base, fname)
    with open(obs_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("[SUCCESS] All 8 episode notes have been generated successfully!")
