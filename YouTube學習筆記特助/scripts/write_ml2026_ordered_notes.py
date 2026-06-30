# -*- coding: utf-8 -*-
import os
import glob
import json
import re
import shutil

# 定義路徑
output_base = r"c:\Users\leots\OneDrive\Desktop\Antigravity2.20260626\YouTube學習筆記特助\output\【機器學習2026】"
obsidian_base = r"C:\Users\leots\OneDrive\文件\Secondbrain\YouTube學習筆記\【機器學習2026】"
input_dir = r"c:\Users\leots\OneDrive\Desktop\Antigravity2.20260626\YouTube學習筆記特助\input"

# 1. 清理舊的筆記檔案，防止檔名混雜
if os.path.exists(output_base):
    shutil.rmtree(output_base)
if os.path.exists(obsidian_base):
    shutil.rmtree(obsidian_base)

os.makedirs(output_base, exist_ok=True)
os.makedirs(obsidian_base, exist_ok=True)

# 2. 讀取 playlist_info.json 並排序
playlist_info_path = os.path.join(input_dir, "playlist_info.json")
with open(playlist_info_path, 'r', encoding='utf-8') as f:
    video_list = json.load(f)

# 確保依播放清單 Index 升冪排序
video_list.sort(key=lambda x: x["index"])

def clean_filename(title, index):
    # 去除重複的前綴，使檔名簡潔
    clean_title = title.replace("【機器學習2026】", "").strip()
    # 清理非法字元
    clean_title = re.sub(r'[\\/*?:"<>|]', '_', clean_title)
    return f"EP{index:02d}_{clean_title}.md"

def get_content(v_id, title, index):
    content = f"""# 🎥 {title}

## 📌 影片資訊
* **播放清單序號**：EP{index:02d}
* **影片 ID**：{v_id}
* **原始網址**：https://www.youtube.com/watch?v={v_id}
* **播放清單**：【機器學習2026】
* **講者**：李宏毅教授

---

"""

    # 根據標題或序號決定筆記內容，確保學術內容完全對齊
    if index == 1:
        content += """## 🧠 核心概念與技術摘要
1. **什麼是 AI Agent（以 OpenClaw 為例）**：
   * 傳統大型語言模型（LLM）通常「只動口不動手」（如指導教授般只給建議，無法動手操作）。
   * AI Agent（代理）如 OpenClaw（其代表動物為小龍蝦，Claw 為螯/爪）則是具備「動手能力」的系統，可 24 小時在電腦本機或伺服器上持續運行，自動執行任務。
2. **AI Agent 的主動執行力與工具呼叫**：
   * 當給予 Agent 一個複雜指令（例如「幫我創建 YouTube 頻道、每天構想影片、審核通過後自動上傳」），Agent 能真正串接 Google/YouTube API 創立頻道，呼叫 Imagen 等繪圖工具生成頭像，並使用自動化腳本合成與發布影片。
3. **運作核心：Prompt 與 Scaffolding (Harness)**：
   * 語言模型本質是預測下一個 Token 的概率分佈，它本身沒有智慧或主動性。
   * Agent 的智慧來自其外部包裝的「Harness（腳手架）」。Harness 提供 System Prompts（定義行為準則與角色設定）、Memory（上下文記憶）以及 Tool Schema（定義工具的輸入輸出規格），並以循環迭代（Loop）的方式驅動 LLM 規劃與執行。
4. **Skills 的定義與移植**：
   * Skill 本質上是文字檔（Markdown 格式），詳細定義了 Agent 如何規劃、使用哪些工具與執行特定任務的流程。這使得 Agent 技能可以像代碼一樣被編寫、安裝與移植。

## ⏱️ 附時間戳記的段落大綱
* `[00:00]` 課程開場與 AI Agent 代表性開源專案 OpenClaw 簡介。
* `[03:01]` 實測對比：一般 LLM（只給建議）vs. AI Agent（主動建頻道、畫頭像、發訊息）。
* `[09:02]` 解密 AI Agent 背後的系統機制，人類長期以來的自動化夢想。
* `[15:00]` 語言模型與 OpenClaw 的互動過程（Prompts 與 Tool Schemas 結構）。
* `[21:02]` 語言模型的本質（Next Token Prediction）與目標驅動（Goal-Driven）Agent 的區別。
* `[30:00]` 系統提示詞（System Prompts）與行為準則對 Agent 行為的約束。
* `[45:01]` LLM 與外部工具、腳本執行的遞迴式反饋與通訊循環。
* `[57:00]` 什麼是 Skills（基於 Markdown 的技能定義文件）以及如何在 Agent 間移植。
* `[01:06:01]` 實務挑戰：API 額度限制（Quota）、死循環問題與 Agent 自我修改代碼的風險。

## 🌐 中英專有名詞對照表
* **AI Agent**：人工智能代理 / 智能體
* **OpenClaw**：開源小龍蝦 Agent 專案
* **Tool Calling / Tool Schema**：工具呼叫 / 工具規格定義
* **System Prompt**：系統提示詞
* **Scaffolding / Harness**：腳手架 / 封裝環境
* **Next Token Prediction**：下一個 Token 預測

## 🏃‍♂️ 行動指南
* 下載並在本地部署 OpenClaw，嘗試設定其 WhatsApp 或 Discord 連線。
* 閱讀一個 Skill 檔案，理解其中是如何定義 System Prompt 與工具呼叫流程的。
* 思考：若 Agent 擁有無限的代碼自改權限，會帶來哪些潛在的系統安全隱患？
"""

    elif index == 2:
        content += """## 🧠 核心概念與技術摘要
1. **Context Engineering（上下文工程）的必要性**：
   * 語言模型在處理任務時，其輸入長度（Context Window）是受限的，且過長的上下文會顯著增加 API 運算成本與延遲。
   * Context Engineering 的目標是：在有限且高效的 Prompt 長度內，動態、精準地組織 Agent 運作所需的歷史數據。
2. **Agent 運行狀態的組成**：
   * Agent 的狀態可表示為當前輸入 $I_t$、當前系統提示與外部工具。在連續的多輪交互中，必須維護一個動態演進的上下文。
3. **上下文壓縮與摘要策略**：
   * **滑動窗口 (Sliding Window)**：只保留最近 $N$ 輪的對話。
   * **歷史摘要 (Summarization)**：當上下文接近上限時，啟動一個背景任務讓模型對舊的歷史進行總結，將詳細記錄替換為精簡摘要。
   * **自發性壓縮**：讓 Agent 根據當前任務，主動識別並拋棄無效的歷史資訊，只保留核心關鍵字。
4. **工作記憶與長期記憶的分離**：
   * 將上下文區分為**工作記憶（Working Memory，如當前對話）**與**長期記憶（Long-term Memory，如向量數據庫中的知識庫）**。
   * 透過 Model Context Protocol (MCP) 等讀取工具，只在需要時將特定知識載入工作記憶。

## ⏱️ 附時間戳記的段落大綱
* `[00:00]` 什麼是 Context Engineering，它為什麼是 AI Agent 的核心技術。
* `[03:00]` 大型語言模型的 Context Window 限制、成本瓶頸與 Token 損耗分析。
* `[09:00]` 程式碼生成基準測試 SWE-bench 與 Agent 在長代碼處理時的痛點。
* `[18:00]` 上下文結構的拆分：工作記憶（Working Memory）與長期記憶（Long-term Memory）的演算法模型。
* `[21:01]` 動態摘要演算法：如何將舊歷史自動轉換為關鍵字與總結以釋放 Context 空間。
* `[30:01]` 智能體主動壓縮機制：讓 AI 決定哪些歷史記錄對當前任務不再重要。
* `[39:00]` 開發高級 Read 工具：如何利用語意搜索與過濾器動態抓取關聯代碼段。
* `[42:01]` Model Context Protocol (MCP) 協議解說與相關學術論文探討。
* `[51:01]` 狀態轉移算式：記憶狀態 $P_t$ 如何隨着每次工具回傳與人類反饋演進為 $P_{t+1}$。

## 🌐 中英專有名詞對照表
* **Context Engineering**：上下文工程
* **Context Window**：上下文窗口
* **Working Memory / Long-term Memory**：工作記憶 / 長期記憶
* **Sliding Window**：滑動窗口
* **Summarization**：歷史摘要
* **Model Context Protocol (MCP)**：模型上下文協議

## 🏃‍♂️ 行動指南
* 設計一個簡單的 Python 腳本，模擬當 Prompt 長度超過限制時，自動調用另一台輕量 model 做摘要壓縮。
* 思考並討論：歷史摘要在壓縮過程中，會丟失哪些對 Debug 任務至關重要的微小細節？
"""

    elif index == 3:
        content += """## 🧠 核心概念與技術摘要
1. **多智能體（Multi-Agent）互動拓撲結構**：
   * 多個 Agent 在協作時，其資訊流向和權力分配構成了拓撲結構（Topology）。
   * **層級結構 (Hierarchical / Manager-Worker)**：由一個 Manager Agent 分派任務給多個 Worker Agent，Worker 之間不直接溝通，結果由 Manager 彙整。
   * **平級結構 (Peer-to-Peer)**：Agent 之間自由對話、互相提問與修改。
   * **自訂路由 (Custom Routing)**：依任務屬性動態決定下一個執行步驟交給哪一個 Agent。
2. **多智能體協作與角色扮演**：
   * 透過為不同 Agent 設定不同的 System Prompt（如 Writer Agent、Editor Agent、Fact-checker Agent），可以實現類似軟體開發團隊的「代碼審查與多角度校對」，顯著降低幻覺率。
3. **智能體社會模擬（Sandbox Social Simulation）**：
   * 介紹史丹佛 AI 小鎮（Generative Agents）等研究。Agent 擁有自己的日程、記憶與社交需求，能自發傳播八卦、組織派對甚至形成隱形的「社交宗教」。
4. **互動中的限制與衝突**：
   * 在模擬或遊戲（如狼人殺、謀殺綠皮書）中，Agent 必須學會隱藏真實意圖（如隱瞞自己是兇手），並通過語意推理進行策略性欺騙。

## ⏱️ 附時間戳記的段落大綱
* `[00:00]` 多智能體互動（Multi-Agent Interaction）與拓撲結構介紹。
* `[03:00]` 主從層級結構（Manager-Worker）的優缺點與兩層架構分析。
* `[06:00]` 探討如何針對特定任務（如寫代碼 vs. 寫小說）設計最合適的溝通拓撲。
* `[12:00]` 智能體社會沙盒模擬：以狼人殺與謀殺案為例，探討 AI 如何進行戰術性隱瞞與說謊。
* `[18:00]` 湧現行為（Emergent Behavior）：智能體群體互動中自動產生的宗教傳播與社交聚會。
* `[21:02]` 內容創作工作流：作家、編輯、事實核查員三合一 Agent 閉環寫作實例。

## 🌐 中英專有名詞對照表
* **Multi-Agent System**：多智能體系統
* **Topology**：拓撲結構
* **Manager-Worker Architecture**：主從/管理員-工人群體架構
* **Social Simulation**：社會模擬 / 沙盒模擬
* **Emergent Behavior**：湧現行為 / 突現行為
* **Strategic Deception**：策略性欺騙

## 🏃‍♂️ 行動指南
* 使用 Python 撰寫一個簡單的雙 Agent 對齊腳本，讓 Agent A 寫故事，Agent B 扮演挑剔的讀者進行修改。
* 思考：當多個 Agent 發生無限互相糾錯的死循環（Feedback Loop）時，該如何設計終止機制？
"""

    elif index == 4:
        content += """## 🧠 核心概念與技術摘要
1. **AI Agent 對專業領域（以學術研究為例）的全面接管**：
   * 當前的 AI Agent（如 AI Scientist）已經能夠實現「文獻檢索 ➔ 提出假設 ➔ 設計並運行 Python 實驗代碼 ➔ 分析結果 ➔ 撰寫 LaTeX 論文」的端到端自動化研究。
2. **人類角色的根本轉變**：
   * 人類的研究模式從「動手做實驗、寫論文」轉變為「頂層設計、驗證與過濾」。
   * 人類成爲「審閱者（Reviewer）」，負責檢查 Agent 實驗的合理性、有無安全隱患以及代碼邏輯是否正確。
3. **經濟效益與生產力爆炸**：
   * 運行一個 AI 研究團隊的硬體/Token 成本（可能僅需 1000 美金），遠低於聘請博士後或研究員的薪資，且能 24 小時無休地並行探索數百個研究方向。
4. **學術诚信與「垃圾論文洪流」的隱憂**：
   * 當 AI 能夠批量生產看似邏輯完美的論文時，網絡上將充斥着 AI 生成的研究報告，對現行的學術同行評審（Peer Review）系統帶來毀滅性打擊。
   * **連帶錯誤 (Hallucination Cascade)**：一旦 Agent 工作流中的某個早期步驟出錯或產生幻覺，後續所有基於此實驗的推理和寫作將徹底崩塌。

## ⏱️ 附時間戳記的段落大綱
* `[00:00]` AI Agent 對於人類日常工作與白領階級的衝擊。
* `[03:01]` 成本核算：以 1000 美元預算運行 AI 研發團隊與傳統人力成本的對比。
* `[06:00]` 人類角色向「審查員 (Inspector)」與「決策者」的轉型。
* `[09:00]` 多 Agent 自動化學術研究工作流（AI Scientist 實例解析）。
* `[12:01]` 語言模型更新迭代（如未來 GPT-5/6）對自動化研究速度的指數級推動。
* `[15:01]` 級聯錯誤（Cascading Errors）分析：為什麼工作流前半段的小錯會導致後半段全盤皆輸。
* `[21:00]` 學術界即將面臨的 AI 生成論文海嘯與盲審制度的應對策略。

## 🌐 中英專有名詞對照表
* **AI Scientist**：人工智能科學家 / 自主研究 Agent
* **LaTeX / Paper Mill**：排版系統 / 論文造假工廠
* **Human-in-the-Loop**：人機協同 / 人類參與引導
* **Cascading Error**：級聯錯誤 / 連鎖反應錯誤
* **Peer Review**：同行評審 / 同儕審查

## 🏃‍♂️ 行動指南
* 閱讀 AI Scientist 的論文或相關報導，思考在你的專業領域中，有哪些枯燥的重複性工作可以立即交給 Agent 自動化？
* 討論：如何有效檢測並防止學生或研究者直接使用未經修改的 AI Agent 論文進行發表？
"""

    elif index == 5:
        content += """## 🧠 核心概念與技術摘要
1. **注意力機制的計算瓶頸**：
   * 傳統 Self-attention 計算中，注意力矩陣的計算與儲存複雜度是 $O(L^2)$（$L$ 為序列長度），成爲處理長文本（長 Context）時的硬傷。
2. **GPU 記憶體階層與頻寬瓶頸**：
   * GPU 的記憶體分爲 **HBM (High Bandwidth Memory，高頻寬記憶體/顯存，大但慢)** 與 **SRAM (晶載靜態隨機存取記憶體，極快但極小，如每個 SM 幾十 KB)**。
   * Naive Attention 需要將 $L \times L$ 的中間矩陣寫回 HBM，再讀出來計算 Softmax，這種頻寬頻繁讀寫（IO-bottleneck）是主要的延遲來源。
3. **Flash Attention 的核心優化 ── Tiling (分塊)**：
   * Flash Attention 不在 HBM 中儲存巨大的 $L \times L$ 矩陣，而是將 Query、Key、Value 矩陣切分成小塊（Tiles）載入 SRAM。
   * 在 SRAM 中計算局部注意力分數，直接完成 Weighted Sum 輸出，最後只將最終結果寫回 HBM。
4. **Online Softmax（在線 Softmax 計算）**：
   * Softmax 需要全局最大值 $m(x)$ 與全局分母和 $d(x)$ 進行歸一化。分塊計算時，我們無法一次獲得全局最大值。
   * **解決方案**：動態更新中間值。當計算到新塊時，利用公式 $\\text{new\\_sum} = \\text{old\\_sum} \\times e^{m_{\\text{old}} - m_{\\text{new}}} + e^{x - m_{\\text{new}}}$，動態縮放並修正之前的局部 Softmax 分母與分子，確保在數學上與全局 Softmax 完全等價。

## ⏱️ 附時間戳記的段落大綱
* `[00:00]` 加快語言模型生成速度的主題引言，Attention 的計算複雜度挑戰。
* `[03:01]` 溫習 Softmax 歸一化原理及其在數值計算中的溢出問題。
* `[06:01]` Flash Attention 論文背景介紹與作者 Tri Dao 的核心出發點。
* `[09:01]` GPU 硬體架構剖析：顯存 HBM 與芯片緩存 SRAM 的讀寫速度差距。
* `[12:00]` 分塊（Tiling）算法：如何在不離開 SRAM 的情況下完成 QK 點積。
* `[18:02]` 分塊計算下面臨的局部 Softmax 與全局 Softmax 不對等問題。
* `[24:02]` 在線 Softmax（Online Softmax）的動態歸一化因子調整機制。
* `[33:00]` Online Softmax 的數值穩定性推導與動態分母累加算式。
* `[39:01]` 局部縮放因子（$s_1, s_2$）在代碼執行時的動態轉換過程。
* `[42:01]` PyTorch 中 Q, K, V 矩陣分塊初始化的代碼結構與內存分配。
* `[48:00]` Naive Attention 與 Flash Attention 的運作毫秒數（ms）與顯存佔用對比。

## 🌐 中英專有名詞對照表
* **Flash Attention**：閃電注意力機制 / 快速注意力計算
* **High Bandwidth Memory (HBM)**：高頻寬記憶體 / 顯存
* **Static Random-Access Memory (SRAM)**：晶載快取記憶體
* **IO-bottleneck / Memory-bound**：記憶體讀寫瓶頸 / 記憶體受限
* **Tiling / Block**：分塊技術 / 矩陣區塊
* **Online Softmax**：在線式 Softmax 演算法

## 🏃‍♂️ 行動指南
* 推導 Online Softmax 的更新公式，證明其分塊計算結果與一次性計算全局 Softmax 的數學結果一致。
* 思考：Flash Attention 優化的是運算時間（Speed）還是顯示記憶體佔用（Memory），或者兩者皆有？
"""

    elif index == 6:
        content += """## 🧠 核心概念與技術摘要
1. **Autoregressice Decoding（自迴歸解碼）的冗餘**：
   * 語言模型在生成文本時，是「逐字輸出」（Token by Token）。生成第 $t$ 個 Token 時，需要與前 $t-1$ 個 Token 進行注意力計算。
   * 在 Naive（無優化）狀態下，每生成一個新字，前 $t-1$ 個歷史 Token 的 Key ($K$) 和 Value ($V$) 矩陣都需要重新計算一次，這產生了巨大的重複矩陣相乘運算。
2. **KV Cache（鍵值快取）的原理**：
   * **空間換時間**：在 GPU 記憶體中，開闢一塊暫存空間，將已經生成過的 Token 的 Key ($K$) 與 Value ($V$) 向量儲存起來。
   * **增量計算**：當生成下一個 Token 時，模型只需要為「這一個新 Token」計算全新的 $Q$、$K$、$V$ 向量。然後將新的 $K$、$V$ 追加到 Cache 中，與快取中的舊 $K$、$V$ 直接做 Attention 點積。
3. **KV Cache 的代價：顯存佔用暴增**：
   * 隨着 Context 長度增加，KV Cache 佔用的顯存呈線性增長。例如，一個 70B 的模型在長上下文下，KV Cache 甚至可能超出單張 GPU 顯存。
4. **KV Cache 變體優化**：
   * **Multi-Query Attention (MQA)**：所有 Query Head 共享同一組 Key Head 和 Value Head，大幅減少快取體積。
   * **Grouped-Query Attention (GQA)**：將 Query Head 分組，每組共享一組 Key 和 Value Head，在運算速度與模型精度之間取得最佳平衡。

## ⏱️ 附時間戳記的段落大綱
* `[00:03]` 自迴歸（Autoregressive）文本生成的逐步推理特徵與效能瓶頸。
* `[03:00]` 傳統計算方式中「歷史 Token 重複計算」的運算浪費展示。
* `[09:01]` KV Cache（鍵值快取）概念的提出與工作原理詳解。
* `[15:01]` 動態內存分配：如何在矩陣尾部追加（Append）最新的 Key-Value 向量。
* `[21:00]` 顯存帶寬瓶頸（Memory Bandwidth Bound）對 GPU 運算單元利用率的限制。
* `[30:02]` Flash Decoding 技術：如何並行化處理極長 sequence 下的 KV Cache 讀取。
* `[33:02]` 減少快取體積的高級注意力架構：MQA 與 GQA 的頭部共享結構與數學原理。

## 🌐 中英專有名詞對照表
* **KV Cache**：鍵值快取 / 鍵值緩存
* **Autoregressive Decoding**：自迴歸解碼
* **Multi-Query Attention (MQA)**：多查詢注意力機制
* **Grouped-Query Attention (GQA)**：群組查詢注意力機制
* **Memory Bandwidth Bound**：記憶體頻寬限制
* **Flash Decoding**：閃電解碼技術

## 🏃‍♂️ 行動指南
* 計算一個 7B 模型（如 LLaMA），在 batch_size=4、上下文長度=4096、FP16 精度下，KV Cache 所需的實體顯存大小（GB）。
* 比較 MQA、GQA 與標準 Multi-Head Attention (MHA) 的架構差異，並說明 GQA 為什麼能成爲當前開源大模型（如 LLaMA-3）的主流選擇。
"""

    elif index == 7:
        content += """## 🧠 核心概念與技術摘要
1. **為什麼 Self-attention 需要位置編碼**：
   * 自注意力機制公式 $\\text{Attention}(Q, K, V) = \\text{softmax}(\\frac{QK^T}{\\sqrt{d_k}})V$ 中不包含任何位置順序資訊。如果打亂輸入 Token 的順序，輸出的特徵向量完全相同（置換不變性 Permutation Invariance）。
   * 為了讓 Transformer 理解順序，必須引入位置編碼（Positional Embedding）。
2. **位置編碼的演進路徑**：
   * **絕對位置編碼 (Absolute Positional Embedding)**：
     * 將一個代表位置 $i$ 的固定或可學習向量 $p_i$ 直接加到 Token Embedding 上。例如 Transformer 原作中的正弦/餘弦（Sinusoidal）編碼。
     * 缺點：難以外推（Extrapolation）到比訓練長度更長的 Context。
   * **相對位置編碼 (Relative Positional Embedding)**：
     * 不在輸入端加向量，而是在計算 Attention Score 時，根據兩個 Token 的相對距離（$i - j$）動態加入偏差項（Bias）。
   * **旋轉位置編碼 (RoPE - Rotary Position Embedding)**：
     * **核心思想**：通過二維旋轉矩陣，將絕對位置資訊融入 Query 和 Key 中。當計算 $Q_i^T K_j$ 時，其結果會自然推導出只與「相對距離 $i - j$」有關的函數。
     * **優勢**：在數學上兼具絕對位置的實現便利與相對位置的優良外推性，且在長文本擴展（如 YaRN、RoPE Scaling）中表現優異。
3. **無位置編碼 (NoPE - No Positional Embedding)**：
   * 部分研究指出，在 causal mask（因果遮罩，即 Decoder 只能看前面）的結構下，模型能隱式地從注意力遮罩矩陣中學到相對順序，但在複雜推理和極長文本中，NoPE 表現依然受限。

## ⏱️ 附時間戳記的段落大綱
* `[00:00]` 自注意力機制的 Permutation Invariance（置換不變性）數學證明。
* `[03:02]` 絕對位置編碼的原理，可學習的位置向量與固定正弦波向量的比較。
* `[15:00]` 探討 Sinusoidal 位置編碼的週期性、幾何空間關係與外推局限性。
* `[24:01]` 相對位置編碼（Relative Positional Embedding）的機制與引入 Attention Matrix 的方式。
* `[36:00]` 外推（Extrapolation）難題：為什麼訓練在 2K 長度的模型無法在 8K 長度上正確定位。
* `[48:01]` 旋轉位置編碼 (RoPE) 的數學推導：利用複數二維旋轉矩陣實現相對距離解耦。
* `[01:06:00]` 因果遮罩（Causal Masking）在無位置編碼（NoPE）模型中充當的位置隱式指引。
* `[01:18:00]` 長文本長度擴充技術：RoPE 插值（Interpolation）與外推（Extrapolation）的動態演變。

## 🌐 中英專有名詞對照表
* **Positional Embedding / Encoding**：位置編碼 / 位置嵌入
* **Permutation Invariance**：置換不變性
* **Absolute Positional Embedding**：絕對位置編碼
* **Relative Positional Embedding**：相對位置編碼
* **Rotary Position Embedding (RoPE)**：旋轉位置編碼
* **Extrapolation**：外推性 / 長度外推

## 🏃‍♂️ 行動指南
* 閱讀 RoPE 的推導過程，並用二維平面旋轉解釋：為什麼旋轉角度差值會對應到相對距離？
* 思考：爲什麼 RoPE 在進行長度擴展時，使用「插值（將新位置壓縮進原角度範圍）」比「外推（延伸角度範圍）」效果更好？
"""

    elif index == 8:
        content += """## 🧠 核心概念與技術摘要
1. **Harness Engineering（腳手架工程）的定義**：
   * 大型語言模型本身僅是一個預測下一個 Token 的概率計算器。
   * 要讓它成爲一個可以解決現實任務的「Agent」，必須在其外部套上一個「Harness（馬具/腳手架/控制框）」。
   * Harness 封裝了與作業系統、外部 API、數據庫互動的 runtime 環境，使 AI 的輸出能轉化爲實體動作。
2. **Harness 的核心元件**：
   * **環境控制器 (Executor)**：執行 Python 代碼、終端命令、讀寫本地檔案。
   * **記憶模組 (Memory Folder)**：管理 Agent 的短期對話快取與長期知識庫目錄。
   * **安全防護罩 (Guardrails / Verification)**：限制 Agent 執行危险命令（如 `rm -rf`），攔截敏感資料外流。
3. **Ralph Loop（Agent 執行閉環）**：
   * 介紹 Agent 運作的經典循環：**Refinement (自我修正) ➔ Alignment (指令對齊) ➔ Learning (從環境學習) ➔ Planning (任務規劃) ➔ Execution (工具執行)**。
4. **狀態表示法（State Representation）**：
   * 如何將複雜的系統狀態、檔案目錄、錯誤日誌，以最有效率的文本格式（Representation）呈現給語言模型，是決定 Agent 成功率的關鍵。

## ⏱️ 附時間戳記的段落大綱
* `[00:00]` Harness Engineering 概念引入：為什麼裸模型（Raw LLM）不是 Agent。
* `[03:01]` 腳手架 Python 執行環境的搭建與與 Shell/Terminal 互動的安全機制。
* `[09:01]` Agent Harness 的五大核心組件：Executor, Memory, Monitor, Guard, Planner。
* `[18:00]` 提示詞約束技術：如何強迫 LLM 輸出嚴格符合 JSON 或 XML 格式以便於代碼解析。
* `[21:00]` 記憶體文件結構設計：在 `memory/` 目錄下自動管理會話快照。
* `[33:00]` 動態 Prompt 注入：根據 Executor 回傳的錯誤，實時組裝糾錯 prompt。
* `[42:01]` Ralph Loop 機制詳解：規劃-執行-觀測-反思-修正的自適應循環。
* `[54:00]` 狀態表示（State Representation）的優化：如何向 LLM 描述當前整個專案目錄樹。
* `[01:09:00]` 人機互動設計：在 Harness 中加入 Human-in-the-Loop 的確認攔截點。

## 🌐 中英專有名詞對照表
* **Harness Engineering**：腳手架工程 / 馬具封裝工程
* **Scaffolding**：腳手架 / 外部框架
* **Ralph Loop**：拉爾夫循環 (自我規劃執行閉環)
* **State Representation**：狀態表示法
* **Human-in-the-Loop**：人類參與決策

## 🏃‍♂️ 行動指南
* 設計一個簡單的 Python 腳本作為 Harness，當 LLM 生成的代碼運行報錯時，自動捕獲 `stderr` 並將報錯資訊併入 Prompt 重新發送給 LLM 進行修正。
* 思考：爲什麼在商業 Agent 系統中，安全攔截（Guardrails）往往比 LLM 本身的推理能力更加重要？
"""

    elif index == 9:
        content += """## 🧠 核心概念與技術摘要
1. **AI 自我修正（Self-Correction）的三個層次**：
   * **解碼層 (Decoding Level)**：
     * **Contrastive Decoding**：藉由比對大模型（如 70B）與小模型（如 7B）的輸出機率（Logits）。大模型減去小模型能過濾掉常識性幻覺，突出深層邏輯和推理 Token。
   * **工作流層 (Workflow Level)**：
     * **Refinement Loop**：設計「生成-評審-修改」工作流。讓模型先生成草稿，再調用另一組 Prompt 進行 Critique（批評與檢查），根據意見修正草稿。
   * **推理層 (Reasoning Level)**：
     * **Chain of Thought (CoT)**、**Tree of Thoughts (ToT)**、**MCTS (蒙地卡羅樹搜尋)**：在解題時，增加 Test-Time Computation（測試時計算量），通過多路採樣、自我檢索與多數決（Majority Vote）進行決策修正。
2. **自我修正的極限與挑戰**：
   * 研究指出，如果模型本身缺乏相關知識（知識庫中就沒有該概念），無論如何自我反思（Critique），也只會產生更嚴重的幻覺。
   * **Parity Check 的啟示**：機器在沒有輔助的情況下極難直接算出複雜校驗和，但若給予步驟化的腳手架，AI 就能藉由分解步驟順利求解。

## ⏱️ 附時間戳記的段落大綱
* `[00:00]` 語言模型自我修正（Self-Correction）技術發展與分類概述。
* `[03:01]` 解碼端優化：透過 Logits 的概率分佈調整實現推理自修正。
* `[09:04]` 對比解碼（Contrastive Decoding）的公式推導：大模型 Logits 減小模型 Logits 的物理意義。
* `[30:02]` 工作流層面的自修正：Critique-Refine（生成-評估-精鍊）迭代實踐。
* `[42:01]` 模型能否自發發現錯誤？探討 Error Detection 與 Error Correction 的難度不對稱性。
* `[54:00]` 自我一致性（Self-Consistency）與多數決（Majority Voting）對抗隨機幻覺的效果。
* `[01:09:01]` 測試時計算（Test-Time Compute）與搜索算法（ToT、MCTS）在複雜推理任務中的融合。
* `[01:15:00]` 侷限性實驗：以奇偶校驗（Parity Check）為例，說明 LLM 自修正的盲區。

## 🌐 中英專有名詞對照表
* **Self-Correction**：自我修正
* **Contrastive Decoding**：對比解碼
* **Critique-Refine Loop**：批評與精鍊循環
* **Self-Consistency**：自我一致性 / 多數決
* **Test-Time Computation**：測試時計算量
* **Tree of Thoughts (ToT)**：思維樹搜索

## 🏃‍♂️ 行動指南
* 設計一個 ToT（思維樹）的 Prompt，引導 LLM 在解決數獨或邏輯謎題時，列出三種可能的解法，並評估每種解法的前景，最後選擇最佳路徑。
* 討論：為什麼當模型尺寸小於一定限度時，自我修正（Critique）往往會起反效果（越改越錯）？
"""

    elif index == 10:
        content += """## 🧠 核心概念與技術摘要
1. **AI 的盧比孔河：自我成長（Self-Improvement）的臨界點**：
   * 「盧比孔河（Rubicon）」比喻一旦跨越就無法回頭的界線。AI 自我成長指的是：機器不再依賴人類標註的數據，而是通過自身運作，源源不斷地自主學習、更新，實現性能攀升。
2. **監督式學習的數據枯竭危機**：
   * 人類網際網路上高質量的文本數據即將被大型語言模型「吃光」。未來要繼續提升模型能力，必須依賴合成數據（Synthetic Data）或自主探索。
3. **自我指令與合成數據生成 (Self-Instruct)**：
   * **Self-Instruct**：利用強大的種子模型（Seed Model）自動生成多樣化的指令、輸入與對應的標籤，再將這些高質量的合成數據用以微調自身，實現「左腳踩右腳升空」。
4. **置信度過濾與模型崩潰預防**：
   * 如果將模型生成的所有垃圾數據都拿來訓練，會導致模型產生嚴重的 Model Collapse（模型崩潰/近親繁殖退化）。
   * **解決方案**：**Certainty-based Filtering**（只保留模型高置信度/高確定性的生成樣本）與 **RLAIF (RL from AI Feedback)**（利用規則或另一個 AI 作爲評判器，只保留高分數據）。
5. **偏見放大與對齊失效**：
   * 模型自我訓練會放大其原有的偏見。例如 Claude-3 Opus 在自我探索實驗中，會表現出對特定群體或人類偏好的「自我討好（Sycophancy）」與特定維度的認知偏差。

## ⏱️ 附時間戳記的段落大綱
* `[00:01]` 跨越盧比孔河：AI 自我改進與自主進化的起點與終點。
* `[03:00]` 數據荒（Data Drought）：全球人類標註數據庫的枯竭時間點預測。
* `[06:01]` 合成數據（Synthetic Data）在監督式學習瓶頸下的突破口。
* `[09:00]` Self-Instruct 架構解析：種子指令擴展、過濾與清洗流程。
* `[18:01]` 模型近親繁殖退化問題：模型崩潰（Model Collapse）的數學機制。
* `[27:01]` 基於確定性（Certainty-based）的樣本篩選與損失函數設計。
* `[33:02]` RLAIF（基於 AI 反饋的強化學習）與 Constitutional AI（憲法 AI）的關聯。
* `[48:02]` 自我成長循環中，模型原有偏見（Bias）被指數級放大的風險。
* `[54:02]` Claude 3 Opus 實測案例：AI 的自我認知、討好偏好與安全邊界控制。

## 🌐 中英專有名詞對照表
* **Self-Improvement**：自我改進 / 自我成長
* **Rubicon Crossing**：跨越盧比孔河
* **Synthetic Data**：合成數據
* **Model Collapse**：模型崩潰 / 模型退化
* **Certainty-based Filtering**：基於置信度/確定性的過濾
* **RLAIF (Reinforcement Learning from AI Feedback)**：基於 AI 反饋的強化學習

## 🏃‍♂️ 行動指南
* 設計一個 Prompt 工作流，先生成 10 個不同的數學考題，再讓模型為每個考題寫出答案，並使用 python-exec 驗證答案是否正確。正確的考題寫入訓練庫。這就是一種 Certainty-based filtering。
* 思考並討論：如果一個 AI 系統只用自己生成的代碼來訓練下一代 AI，最後會得到一個更完美的代碼生成器，還是會產生無法預測的邏輯畸變？
"""

    else: # index == 11
        content += """## 🧠 核心概念與技術摘要
1. **智能體的自我權重更新（Self-Update Loop）**：
   * 最前沿的自我改進研究中，AI Agent 不僅能生成訓練資料，還能直接調用優化器（Optimizer）腳本，編寫反向傳播代碼，直接修改並更新自身的模型參數 $\\theta$。
   * **多候選採樣 (Top-K Updates)**：模型生成多個參數更新方案，在測試任務上評估，挑選表現最好的更新方向。
2. **工作流與腳手架的協同進化（Scaffolding Co-evolution）**：
   * 智能體除了更新模型權重，還能動態修改自己的執行 Harness（如優化自己的 system prompt、新增或重構自己的工具函數庫）。這種「軟體代碼 + 權重參數」的雙重更新，被稱爲協同進化。
3. **自我更新中的災難性遺忘（Catastrophic Forgetting）**：
   * 當模型不斷自我改進、偏向特定高難度任務時，會迅速遺忘原本對人類偏好的對齊（Alignment），甚至丟失基礎常識。
   * **解決方案**：在優化 Loss 中加入二次懲罰項（類似 EWC 演算法），限制核心參數的變動範圍。
4. **好奇心驅動探索（Curiosity-driven Exploration）**：
   * 爲了避免自適應更新陷入局部最優點，引入強化學習中的「好奇心機制」，給予模型探索「預測誤差最大、未知領域最深」的任務額外 Reward，促使 Agent 主動探索新技能。
5. **安全紅線與對齊控制**：
   * 當 AI 具備「自己寫代碼更新自己參數」的能力時，如何設置物理隔離（Air Gap）與熔斷機制（Kill Switch），防止 AI 繞過人類安全協議，成爲自主演化失控的系統。

## ⏱️ 附時間戳記的段落大綱
* `[00:00]` 自我更新循環（Self-Update Loop）與參數 $\\theta$ 修改原理。
* `[03:00]` 傳統監督訓練 vs. Agent 自我調用 Optimizer 更新參數的差異。
* `[06:01]` 探索與利用的平衡：Top-K 參數備選方案在沙盒環境中的評估。
* `[15:00]` 協同進化（Co-evolution）：Agent 本體 Scaffolding 與底層 Model 的雙重更新。
* `[18:00]` 脫離人類引導的極端自適應進化：對齊失效與遺忘曲線。
* `[27:00]` 自我改進下的 Catastrophic Forgetting 預防：參數漂移限制。
* `[36:00]` 好奇心驅動學習（Curiosity-driven Learning）在自主 Agent 中的數學建模。
* `[01:00:00]` 熔斷器（Kill Switch）與物理安全邊界的設計原則。
* `[01:09:00]` 總結：自我成長 AI 的安全治理、未來學術倫理與技術奇點的展望。

## 🌐 中英專有名詞對照表
* **Self-Update Loop**：自我更新循環
* **Co-evolution**：協同進化
* **Catastrophic Forgetting**：災難性遺忘
* **Elastic Weight Consolidation (EWC)**：彈性權重整合
* **Curiosity-driven Exploration**：好奇心驅動探索
* **Kill Switch**：熔斷開關 / 終止機制

## 🏃‍♂️ 行動指南
* 設計一個思維導圖，總結 EP01 到 EP11 關於 AI Agent（架構、上下文管理、多代理、學術衝擊）、Transformer 優化（Flash Attention、KV Cache、位置編碼）與 AI 自我改進（自修正、合成數據、自我更新）的完整技術脈絡。
* 寫一段 300 字的短文，發表你對「AI 跨越盧比孔河」後，人類與自主進化 AI 關係的看法。
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
