# -*- coding: utf-8 -*-
import os
import glob
import json
import re
import shutil

# 定義路徑
output_base = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "output", "YouTube學習筆記特助", "n8n 工作流基礎教學"))
obsidian_base = r"C:\Users\leots\OneDrive\文件\Secondbrain\YouTube學習筆記\n8n 工作流基礎教學"
input_dir = r"c:\Users\leots\OneDrive\Desktop\Antigravity2.20260626\YouTube學習筆記特助\input"

# 1. 清理舊的筆記檔案，防止檔名混雜
if os.path.exists(output_base):
    shutil.rmtree(output_base)
if os.path.exists(obsidian_base):
    shutil.rmtree(obsidian_base)

os.makedirs(output_base, exist_ok=True)
os.makedirs(obsidian_base, exist_ok=True)

# 2. 定義影片資訊與順序（手動對齊 EP01-EP03，不採用 playlist 原生逆序）
video_list = [
    {
        "index": 1,
        "id": "r9mi3ZJIWbg",
        "title": "學會 n8n 為你省下 80% 時間！(EP.1) 這個 AI 助理只認你這個主人，不但使命必達且全天候待命！",
        "filename": "EP01_n8n基礎自動化流程與日曆、RSS整合.md"
    },
    {
        "index": 2,
        "id": "sRU6Y7DXkLI",
        "title": "學會 n8n 為你省下 80% 時間！(EP.2) 這個 AI 助理只認你這個主人，不但使命必達且全天候待命！",
        "filename": "EP02_自建Siri與Telegram_AI語音助理.md"
    },
    {
        "index": 3,
        "id": "D-VEcKZ3NV0",
        "title": "學會 n8n 為你省下 80% 時間！(EP.3) 「本地安裝」/「雲端部署」比你想的還要簡單！",
        "filename": "EP03_Docker本地安裝與Hostinger雲端部署.md"
    }
]

def clean_filename(title, index):
    for v in video_list:
        if v["index"] == index:
            return v["filename"]
    return f"EP{index:02d}_{title}.md"

def get_content(v_id, title, index):
    content = f"""# 🎥 {title}

## 📌 影片資訊
* **播放清單序號**：EP{index:02d}
* **影片 ID**：{v_id}
* **原始網址**：https://www.youtube.com/watch?v={v_id}
* **播放清單**：n8n 工作流基礎教學
* **講者**：PAPAYA 電腦教室

---

"""

    if index == 1:
        content += """## 🧠 核心概念與技術摘要
1. **n8n 自動化工具概述**：
   * n8n 是一款強大的工作流自動化工具，能整合各種網頁服務與 API，減少繁瑣的手動操作。初學者建議先從官方 14 天免費試用雲端版（n8n Cloud）著手。
2. **工作流核心元件與資料格式**：
   * **觸發器 (Trigger)**：工作流的起點與開關。可分為「手動觸發（Manual Trigger）」與「排程觸發（Schedule Trigger）」。
   * **節點 (Nodes)**：執行特定任務的模組（如 Gmail 傳送、Google Calendar 讀取、RSS 擷取、Filter 篩選器等）。
   * **JSON 資料格式**：n8n 節點間的資料傳遞均基於 JSON 格式（名稱與數值的鍵值對清單）。在開發時可使用 `mock data` 鎖定測試數據。
3. **資訊流的管理與合併**：
   * **Edit Fields（編輯欄位）**：用來簡化資料結構，只保留需要的欄位（如將日曆複雜輸出簡化為行程名稱與開始時間）。
   * **Merge（合併）**：將多個分流的資料（如 Google 日曆分支與 RSS 新聞分支）匯整為單一資訊流。
   * **Aggregate（整合）**：將多筆獨立的資料行整合成一個清單或單一物件，避免後續節點（如 Gmail）因收到多筆資料而重複發送多封郵件。
4. **AI 節點整合（Message a Model）**：
   * 整合 ChatGPT 等大語言模型。需在 OpenAI 平台綁定卡片並儲存小額費用，取得 API Key。
   * **System Prompt** 定義 AI 角色與格式約束（例如要求 AI 將郵件分成今日行程與今日文章，並使用 HTML/CSS 美化）。
   * **User Prompt** 傳入具體要翻譯、彙整的行事曆與 RSS 新聞內容。

## ⏱️ 附時間戳記的段落大綱
* `[00:03]` n8n 功能簡介與三集教學大綱說明，官方雲端服務註冊流程。
* `[01:14]` 建立首個工作流程、手動觸發器（Manual Trigger）與 JSON 測試數據（Mock Data）解說。
* `[02:21]` 連結第一個節點（Gmail Send a Message），登入 Google 帳號與動態拖曳欄位主旨。
* `[03:56]` 進階應用：Google Calendar（Get Many Events）日曆節點設定與 ISO 8601 日期格式轉換。
* `[05:10]` 使用 Date & Time 節點自訂日期與時間格式（年月日時分），重新命名節點增加可讀性。
* `[05:59]` 使用 Edit Fields 篩選並簡化行事曆過多欄位。
* `[07:16]` 引入 Aggregate 節點整合多筆行程，使用 `join` 語法與雙換行符號進行行程換行排版。
* `[08:15]` On a Schedule 排程觸發器設定，每天早上 07:30 定時自動寄出行程。
* `[08:49]` 整合 RSS 節點自動抓取 Techcrunch 新聞，並利用 Filter 篩選「包含 AI」的熱門文章。
* `[10:33]` 使用 Merge 節點匯整日曆與 RSS 兩條資訊分流，並利用 Sticky Notes（便利貼）區隔工作區塊。
* `[12:03]` 導入 ChatGPT（Message a Model 節點），設定 OpenAI API Key 與 System/User Prompt 提示詞進行中英翻譯與 CSS 排版美化。
* `[13:45]` Gmail 節點改為 HTML 郵件類型，成功發送精美排版的今日美化摘要郵件。

## 🌐 中英專有名詞對照表
* **n8n Cloud**：n8n 雲端託管服務
* **Trigger / Manual Trigger**：觸發器 / 手動觸發
* **Schedule Trigger**：排程觸發器
* **JSON (JavaScript Object Notation)**：輕量級的資料交換格式
* **Mock Data**：測試/模擬數據
* **Date & Time Node**：日期與時間轉換節點
* **Edit Fields Node**：編輯/篩選欄位節點
* **Merge Node / Aggregate Node**：合併節點 / 整合聚攏節點
* **System Prompt / User Prompt**：系統提示詞 / 用戶提示詞

## 🏃‍♂️ 行動指南
* 註冊一個免費的 n8n Cloud 帳戶，並照著步驟建立手動觸發 Gmail 寄信的工作流。
* 嘗試找一個有 RSS Feed 的中文新聞網站，替換 Techcrunch 連結，並利用 Filter 篩選你關心的主題。
* 思考：若直接將 Merge 出來的多筆資料接入 Gmail 節點，會產生什麼樣的後果？
"""

    elif index == 2:
        content += """## 🧠 核心概念與技術摘要
1. **AI Agent 與傳統自動化的差異**：
   * 傳統自動化必須由人類寫死「If-Then」的硬編碼邏輯。
   * AI Agent（智能體）節點搭配大語言模型（Chat Model，如 GPT-4o-mini），具有自主思考、規劃與選擇工具的決策能力。
2. **AI Agent 的基礎結構**：
   * **身體 (AI Agent 節點)**：負責處理觸發訊號並呼叫外部工具。
   * **大腦 (Chat Model 節點)**：背後的推理大模型。
   * **System Message（系統訊息）**：設定行為準則（如要求一律使用繁體中文）。
   * **Memory (記憶模組)**：引入 `Simple Memory` 節點。預設可在同一 Session ID（會話識別碼）下保存 5 輪上下文，使 AI 理解前後文。
3. **工具授權與決策（Google Calendar Tool）**：
   * 建立四大行事曆操作工具：Create（新建）、Delete（刪除）、Get Many（讀取）與 Update（更新）。
   * 關鍵在於將工具的參數設定權限移交給 AI（點擊欄位旁的工具圖示），讓 AI 根據用戶口語指令動態判斷 Summary、Start Time、End Time 與 Event ID。
   * 提示詞優化：在 System Message 中寫入時間語法 `{{ $now }}` 告知 AI 當前的即時時間，使 AI 能夠精準定位「今天」、「這週六」等相對時間概念。
4. **多元觸發渠道 (Webhook & Telegram)**：
   * **Webhook (POST)**：建立一個專用接收網址。整合 iPhone 捷徑（Siri 語音輸入 ➔ POST 文字 JSON 至 Webhook ➔ Respond to Webhook 語音朗讀回覆，需設定 UTF-8 標頭）。
   * **Telegram Bot**：透過 BotFather 申請 Bot Token，在 n8n 中設定 Telegram Trigger (On Message) 監聽，並使用 Telegram Node (Send a Text Message) 回應，可關閉 n8n 署名以保持版面乾淨。
5. **AI 智能分流與多工具協作 (Gmail & Contacts)**：
   * 使用 **Text Classifier（文本分類節點）** 連接 LLM，將收到的郵件語意分類為與會議「相關」或「無關」。
   * **Gmail Tool (Send, Reply, Draft)** 與 **Google Contacts Tool (Get Many with Query)**：當信件與會議相關時，AI Agent 動態查詢聯絡人信箱、比對行事曆衝突。若無衝突則直接新增並透過 Telegram 發送確認；若有衝突，則透過 Telegram 詢問是否要改期，並自動撰寫改期信件草稿。

## ⏱️ 附時間戳記的段落大綱
* `[00:03]` AI Agent 概念介紹：自主規劃與決策的大腦助理。
* `[00:46]` 建立 AI Agent 節點，設定內建聊天觸發器與連接 Chat Model（ChatGPT-4o-mini）。
* `[01:46]` System Message 設定繁體中文約束，與引入 Simple Memory 簡易記憶模組（Session ID、對話記憶上限）。
* `[02:52]` 串接 Google Calendar Tool：分別設定 Create、Delete、Get Many、Update 四大節點並重新命名。
* `[05:08]` 日曆查詢實測失敗原因剖析：缺乏當前時間。在提示詞中使用 `{{ $now }}` 語法注入當前時間。
* `[06:20]` 外接輸入源 Webhook（POST）取代預設聊天室，使用 iPhone 捷徑將 Siri 語音轉為文字並傳送至 Webhook。
* `[08:50]` Respond to Webhook 節點設定，將回覆格式設為 Text 並新增 UTF-8 標頭防止 Siri 朗讀亂碼。
* `[10:30]` 語音實測新增「看牙醫」行程至日曆，並將 Webhook 網址轉為生產線 Production（移除 /test 後綴）。
* `[11:27]` Telegram 管道串接：利用 BotFather 新增機器人、取得 Token 與設定 Chat ID。
* `[12:34]` 設定 Telegram Trigger（On Message）與 Send Text Message 回應節點，關閉「附加 n8n 署名」。
* `[14:20]` 高級工作流：Gmail（On Message Received）郵件觸發與 Text Classifier（文本分類節點）語意分流。
* `[16:20]` AI Agent 會議衝突自動化決策提示詞調整：自動收信 ➔ 比對日曆 ➔ 無衝突直接排程 ➔ 有衝突 Telegram 詢問。
* `[17:34]` Gmail Tool (Send, Reply, Draft) 與 Google Contacts (聯絡人查詢) 整合，讓 AI 自主代寫信件並存入草稿匣。
* `[18:30]` 實戰檢驗：時間無衝突自動排程、時間重疊時 Telegram 互動改期、以及手動/自動草稿郵件發送。

## 🌐 中英專有名詞對照表
* **AI Agent Node**：智能代理節點
* **Chat Model**：對話推理大模型
* **Simple Memory**：簡易上下文記憶模組
* **Session ID**：會話識別碼
* **{{ $now }}**：動態時間注入變數
* **Webhook / Respond to Webhook**：網頁鉤子 / 鉤子響應節點
* **Telegram Bot / BotFather**：機器人 / 機器人之父帳號
* **Text Classifier**：文本/語意分類節點
* **Gmail Tool / Google Contacts Tool**：郵件工具 / 聯絡人工具
* **Draft Box**：草稿匣

## 🏃‍♂️ 行動指南
* 在 Telegram 申請一個專屬的機器人，取得 Token 並在本地 n8n 建立一個簡單的 Telegram 聊天機器人。
* 思考：在 AI Agent 中，如果我們在 System Message 中沒有設定 `{{ $now }}`，AI 助理在處理相對時間（如「明天早上十點」）時會遇到什麼問題？
* 試著在 Gmail Tool 中加入 Draft 功能，寄一封信測試 AI 是否能正確將內容放入草稿匣。
"""

    else: # index == 3
        content += """## 🧠 核心概念與技術摘要
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
"""

    return content

# 執行寫入
success_count = 0
for video in video_list:
    v_id = video["id"]
    title = video["title"]
    index = video["index"]
    
    fname = clean_filename(title, index)
    content = get_content(v_id, title, index)
    
    # 寫入專案 output 目錄
    out_path = os.path.join(output_base, fname)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    # 寫入 Obsidian 儲存庫
    obs_path = os.path.join(obsidian_base, fname)
    with open(obs_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    success_count += 1

print(f"[SUCCESS] Generated {success_count} ordered files (EP01 to EP{success_count:02d}) successfully!")
