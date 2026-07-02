# -*- coding: utf-8 -*-
import os
import shutil

# 定義路徑
output_base = r"c:\Users\leots\OneDrive\Desktop\Antigravity2.20260626\YouTube學習筆記特助\output\三叔Sense Bar\AI_Agent 基本功_學習Agent一定要看的一個系列"
obsidian_base = r"C:\Users\leots\OneDrive\文件\Secondbrain\YouTube學習筆記\三叔Sense Bar\AI_Agent 基本功_學習Agent一定要看的一個系列"

# 1. 建立目錄
os.makedirs(output_base, exist_ok=True)
os.makedirs(obsidian_base, exist_ok=True)

# 2. 定義影片資訊與順序 (正向排列：EP01 到 EP03)
video_list = [
    {
        "index": 1,
        "id": "3s2Q1nViZ1w",
        "title": "AI Agent基本功EP01:用Agent來學習Agent_一個 GitHub repo，複製我的整套 AI 工作流到你的 Agent",
        "filename": "EP01_用Agent來學習Agent_複製整套AI工作流.md",
        "content": """# 🎥 AI Agent基本功EP01:用Agent來學習Agent_一個 GitHub repo，複製我的整套 AI 工作流到你的 Agent

## 📌 影片資訊
* **播放清單序號**：EP01
* **影片 ID**：3s2Q1nViZ1w
* **原始網址**：https://www.youtube.com/watch?v=3s2Q1nViZ1w
* **播放清單**：AI_Agent 基本功_學習Agent一定要看的一個系列
* **講者**：三叔Sense Bar
* **創作者**：三叔Sense Bar

---

## 🧠 核心概念與技術摘要
1. **生成式 AI 與 AI Agent 的本質區別**：
   * **生成式 AI (Generative AI)**：主要是「動嘴巴」的聊天機器人，所有的對話與處理邏輯都寄存在雲端（如 ChatGPT 網頁版、Gemini 網頁版、NotebookLM）。當更換電腦或瀏覽器登入時，資料依舊在雲端伺服器上。
   * **AI Agent (智能代理人)**：是「有手有腳」的本地端工作助手。它被安裝並運行在使用者本地電腦的「作業系統（Harness）」中，具備讀取與修改本地檔案、執行命令列腳本、上網下載、甚至是控制其他本機軟體的能力。
2. **AI 的本地「作業系統（Harness）」**：
   * 要讓 AI 在本地電腦工作，必須下載並配置一個外殼或作業系統。例如 ChatGPT 的 Codex 桌面版、Anthropic 的 Claude Code、Google 的 AntiGravity，或開源的 OpenCode。
3. **付費與免費方案的抉擇**：
   * 商業訂閱版（每月 20 美元，如 ChatGPT Plus、Gemini Advanced、Claude Pro）模型智商最高、串接速度最快，能大幅降低設定的繁雜度。
   * 免費與開源方案（如 OpenCode）設定繁複且認證步驟繁多，因此「免費等於麻煩」。
4. **「用 Agent 學習 Agent」的理念**：
   * 與其死記硬背複雜的代碼與環境配置，不如直接複製一個現成的 GitHub 儲存庫，將整套 AI 工作流與技能包（Skills）導入自己的 Agent，讓 Agent 自動幫忙設定好所有運行環境。

## ⏱️ 附時間戳記的段落大綱
* `[00:00]` AI Agent 基本功系列引言：解答初學者該不該學、如何學習 Agent 的焦慮。
* `[01:04]` 為什麼三個月到半年內，AI Agent 將會成為所有教學與研習的必學重點。
* `[02:10]` AI Agent（智能代理）的定義與生成式 AI（對話機器人）的本質區別。
* `[03:20]` 生成式 AI 依賴雲端伺服器的優劣勢分析：跨裝置方便，但缺乏本地系統操作能力。
* `[04:40]` 導入 AI Agent 能讓效率原地起飛 5 到 10 倍，克服跳出舒適圈的學習門檻。
* `[06:56]` 將雲端 AI 引入本地工作的核心：Harness 作業系統概念介紹。
* `[07:33]` ChatGPT 訂閱用戶對接 Codex 桌面端應用程式的下載與初始設定。
* `[09:00]` Google Gemini 訂閱用戶對接 AntiGravity 桌面程式與 API 設定說明。
* `[10:00]` 非付費用戶的福音：開源且免費的 OpenCode 工具介紹與環境限制。
* `[11:00]` 「免費等於麻煩」的論點：申請多個帳號與繁瑣 API 配置的痛點。
* `[12:35]` 本地 AI Agent 所擁有的硬體與檔案系統控制權（讀寫檔案、執行 Terminal 指令）。
* `[13:30]` 示範如何藉由複製 GitHub 儲存庫，在本地 Agent 中一鍵還原並學習整套 AI 工作流。

## 🌐 中英專有名詞對照表
* **Generative AI**：生成式人工智慧
* **AI Agent**：智能代理人 / AI 代理
* **Harness**：AI 運行作業平台 / 系統架底
* **Codex Desktop App**：Codex 桌面應用程式
* **AntiGravity**：Google Agent 桌面端平台
* **OpenCode / OpenClaw**：開源 AI 代理底層框架
* **GitHub Repository**：GitHub 程式碼儲存庫

## 🏃‍♂️ 行動指南
* 下載並安裝適合您帳戶訂閱狀態的 Agent 外殼（付費用戶下載 Codex 或 AntiGravity；免費體驗用戶下載 OpenCode）。
* 思考：若要將 AI Agent 應用在您日常的文書處理中，您最想讓它幫您自動化執行的「手腳」工作是什麼？
"""
    },
    {
        "index": 2,
        "id": "8nwjYouFJoE",
        "title": "AI Agent 基本功 EP02：學習 Agent 必懂的核心觀念與初始化設定",
        "filename": "EP02_學習Agent必懂的核心觀念與初始化設定.md",
        "content": """# 🎥 AI Agent 基本功 EP02：學習 Agent 必懂的核心觀念與初始化設定

## 📌 影片資訊
* **播放清單序號**：EP02
* **影片 ID**：8nwjYouFJoE
* **原始網址**：https://www.youtube.com/watch?v=8nwjYouFJoE
* **播放清單**：AI_Agent 基本功_學習Agent一定要看的一個系列
* **講者**：三叔Sense Bar
* **創作者**：三叔Sense Bar

---

## 🧠 核心概念與技術摘要
1. **本地執行權限的三種層級**：
   * **手動審查 / 待我核准 (Plan / Manual Mode)**：AI 在讀取、編輯檔案或執行任何指令前，都會彈出確認視窗。雖然最安全，但每次都需要按核准，非常浪費時間，且多數命令使用者也看不懂。
   * **半自動審查 (Auto / Turbo Mode)**：AI 自動執行大部分普通指令，僅在遇到刪除檔案、變更敏感設定或跨專案目錄操作時才會攔截確認。此為**最推薦新手**的設定。
   * **全自動無阻擋 (Bypass Permissions / Full Access)**：AI 在本地執行任何 Shell 指令或修改檔案均無需確認。適合對工作流極為熟悉的老手或封閉的沙盒測試。
2. **命令白名單 (Command Whitelist)**：
   * 在 AntiGravity 等平台的本地權限設定中，可自訂「放行關鍵字」。
   * **推薦放行命令**：將 `npm`、`python`、`pip` 加入白名單，讓 AI 在本地自動下載套件並跑程式，省去每次都要手動點擊核准的麻煩。
3. **全域設定 (Global Settings) 與專案設定 (Project-Scoped Settings)**：
   * **全域技能 (Global Skills)**：在所有對話、所有資料夾中都可被觸發的技能（例如：通用簡報製作、影片剪輯指令）。
   * **專案技能 (Project-Scoped Skills)**：僅在特定工作資料夾中生效的技能。**切勿將所有技能都塞入全域**，否則會因為技能過多、關鍵字重疊而導致 AI 觸發錯誤或解析錯亂。
4. **Agent 的啟動記憶機制**：
   * 每次 AI Agent 開啟新對話（Session）時，會先載入全域設定的藍圖檔案，再讀取目前專案資料夾下的專案設定檔。

## ⏱️ 附時間戳記的段落大綱
* `[00:00]` AI Agent 基本功第二集引言：介紹學習 Agent 必備的核心觀念與系統初始配置。
* `[00:35]` 本地電腦安全權限設定（給予 AI 多少執行權利）。
* `[01:20]` 實戰演示：在 Claude Code 中設定 Auto Mode 半自動執行與 Plan 規劃模式。
* `[02:30]` 權限全開（Bypass Permissions）的優缺點分析：執行快速，但有修改錯誤或刪除檔案風險。
* `[03:56]` 實戰演示：在 Codex 桌面版中設定「待我核准」與「自動審查」模式。
* `[05:08]` 為什麼建議新手直接選擇「半自動/待我核准」而非「每一步手動確認」。
* `[06:26]` 實戰演示：在 Google AntiGravity 設定中調整 Agent Settings 與權限安全機制。
* `[07:18]` 高級全自動技巧：在 Local Permissions 中設定 python、npm、pip 指令白名單直接放行。
* `[08:30]` 實戰演示：在開源 OpenCode 專案設定中啟用自動接受權限（Auto Accept）。
* `[09:40]` 技能安全性宣導：避免安裝來路不明的第三方 Skills 以防止木馬外洩隱私。
* `[10:44]` 全域設定（Global Settings）與專案設定（Project Settings）的定義與加載順序。
* `[11:35]` 技能分類法則：通用技能放全域，特殊學科/專案技能放專案目錄，避免關鍵字衝突。

## 🌐 中英專有名詞對照表
* **Auto Mode**：半自動執行模式
* **Bypass Permissions / Full Access**：繞過授權 / 完整存取權限
* **Turbo Mode**：加速模式 (AntiGravity 專屬)
* **Command Whitelist**：命令白名單
* **Global Settings / Project Settings**：全域設定 / 專案設定
* **Global Skills / Project-Scoped Skills**：全域技能 / 專案專屬技能
* **Malicious Skills**：惡意技能包 / 木馬技能

## 🏃‍♂️ 行動指南
* 開啟您的 Agent 設定介面，將權限調整為「半自動/Auto Mode/待我核准」。
* 在 AntiGravity 或您的 Agent 工具中，將 `python` 和 `pip` 加入免審查的 Local Command 白名單中。
* 思考：為什麼將不常用的技能包（Skills）設定為全域，會降低 AI 助理回答時的精準度？
"""
    },
    {
        "index": 3,
        "id": "b8YgyYGjJEU",
        "title": "AI Agent 基本功 EP03：一句話讓 AI 幫你讀檔、寫程式、上網、做出成品",
        "filename": "EP03_一句話讓AI幫你讀檔、寫程式、上網、做出成品.md",
        "content": """# 🎥 AI Agent 基本功 EP03：一句話讓 AI 幫你讀檔、寫程式、上網、做出成品

## 📌 影片資訊
* **播放清單序號**：EP03
* **影片 ID**：b8YgyYGjJEU
* **原始網址**：https://www.youtube.com/watch?v=b8YgyYGjJEU
* **播放清單**：AI_Agent 基本功_學習Agent一定要看的一個系列
* **講者**：三叔Sense Bar
* **創作者**：三叔Sense Bar

---

## 🧠 核心概念與技術摘要
1. **AI Agent 的四大手腳能力**：
   * **讀取檔案 (Read Files)**：能直接讀取本機任何檔案（如純文字、Markdown、PDF、CSV、Word、Excel 等）。
   * **撰寫/執行程式 (Code & Execute)**：背後自動撰寫 Python 並在本地終端機執行以處理複雜運算，使用者甚至不需要看到代碼，就能直接獲得結果。
   * **瀏覽網頁 (Browse & Download)**：能自主上網搜尋最新資料、爬取網頁、下載雲端資源。
   * **產出成品 (Generate Artifacts)**：自動生成 Office 三件套 (Word, Excel, PPT) 或是 Markdown 筆記。
2. **多模態大型語言模型 (Multimodal LLM)**：
   * 讀取純文字檔案（如 txt、csv、docx）時，一般 AI 均可勝任。
   * 若檔案中包含圖片，或者要讀取純圖片檔（jpg、png），則必須使用具備**多模態能力**的頂級模型（如 GPT-4o、Claude 3.5 Sonnet、Gemini 1.5 Pro）。
3. **終極提問技巧：複製檔案路徑**：
   * ⚠️ **核心痛點**：將大檔案直接當作附件上傳會耗損大量 Token（佔用上下文視窗），且檔案一旦更新，上傳的舊附件就不準確。
   * **解決方案**：在 Windows 中，對檔案按右鍵選擇**「複製路徑」（快捷鍵 `Ctrl + Shift + C`）**，直接將路徑字串貼給 AI Agent。如此一來，AI 會直接從實體硬碟讀取 live 檔案，省 Token 又能確保資料永遠最新。
4. **資料夾自動化整理**：
   * 將凌亂的 `Downloads` 資料夾路徑複製貼給 AI，下達分類指令，AI 會自動識別副檔名與主題，建立子資料夾歸檔，並將可疑或多餘檔案放入「待刪除」專用資料夾。

## ⏱️ 附時間戳記的段落大綱
* `[00:00]` AI Agent 基本功第三集引言：介紹 Agent 手腳能力的四大分類。
* `[01:00]` 傳統生成式 AI 的「只說不做」vs 本地 Agent 結合 Python 自動運行的「說到做到」。
* `[02:00]` 文書處理必備：Office 三件套（Word、Excel、PowerPoint）的自動化生成能力。
* `[03:00]` 多模態模型（Multimodal LLM）對於讀取 PDF 與 PowerPoint 圖片的關鍵作用。
* `[04:30]` 頂級模型（付費）與純文字模型在處理圖像和多維度分析時的智商差距。
* `[05:56]` **高階提問秘訣**：使用 Ctrl + Shift + C（複製路徑）代替手動上傳檔案附件。
* `[07:15]` 實戰演示：在 OpenCode 中貼上 CSV 檔案絕對路徑，命令 AI 讀取並進行總結。
* `[08:15]` 為什麼「給予實體路徑」比「直接附加檔案」更能省下大量上下文（Token）空間。
* `[09:20]` 實戰演示：複製凌亂下載資料夾路徑，命令 AI 自動按照檔案格式與用途進行歸類整理。
* `[10:45]` 執行安全攔截點：確保 AI 不會私自刪除您的重要檔案（分類至待刪除區由人工確認）。
* `[11:52]` 執行 Python 自動化成績計算：使用者無需接觸任何程式碼即可跑完繁瑣統計。

## 🌐 中英專有名詞對照表
* **Multimodal LLM**：多模態大型語言模型
* **Read / Write Files**：檔案讀寫
* **Artifacts Generation**：成品/產出物生成
* **Copy Path (Ctrl+Shift+C)**：複製絕對路徑
* **Context Window Saving**：節省上下文視窗空間
* **Folder Clean-up Automation**：資料夾自動化整理

## 🏃‍♂️ 行動指南
* 選取您電腦中一個包含資料的 Excel 或 CSV 檔案，按 `Ctrl+Shift+C` 複製其路徑，並貼給您的 AI Agent，要求它總結資料。
* 提供您電腦中一個非常混亂的資料夾路徑，下指令給 Agent：*「請幫我列出這個資料夾下所有檔案的格式，並規劃一個分類方案，規劃好後請先向我匯報。」*
* 思考：為什麼直接提供「檔案實體路徑」比「附加檔案上傳」更具有即時性與數據一致性？
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
    
    content = video["content"]
    
    # 寫入專案 output 目錄
    out_path = os.path.join(output_base, fname)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    # 寫入 Obsidian
    obs_path = os.path.join(obsidian_base, fname)
    with open(obs_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    success_count += 1

print(f"[SUCCESS] Re-structured and generated {success_count} Sanshu Sense Bar playlist files successfully!")
