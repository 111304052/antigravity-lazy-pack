# 🎥 一部影片看完 Stanford AI 系統課程，從 LLM 到 Agentic Workflow

## 📌 影片資訊
* **影片 ID**：eKW9ITaltWw
* **原始網址**：https://www.youtube.com/watch?v=eKW9ITaltWw
* **講者**：Gary Chen

---

## 🧠 核心概念與技術摘要
1. **橫軸發展與縱軸工程 (Augmenting LLMs)**：
   * 橫軸發展是訓練更強的基礎模型（Base Model，由科技巨頭主導）。
   * 縱軸工程（Augmenting LLMs）是在現有 LLM 上疊加工程技術（Prompt, RAG, Fine-Tuning, Agentic Workflow），這是 AI 工程師的核心舞台。
2. **基礎模型之商業應用局限**：
   * 缺乏特定領域知識（Domain Knowledge）、資訊滯後、輸出具機率隨機性（難以精準控制）、大上下文衰減（Lost in the Middle）。
3. **單一 LLM 增強工具對比**：
   * **Prompt Engineering**：每位工程師必備的基本功。
   * **RAG (檢索增強生成)**：動態查詢、事實準確、低成本，但受限於檢索召回率且推理延遲較高。
   * **Fine-Tuning (微調)**：靜態適應、格式與語調高度一致、低推理延遲，但訓練成本高。
4. **Agentic Workflow (代理工作流) 的四大設計模式**：
   * **Reflection (自我反思)**：AI 檢查自身產出並修正。
   * **Tool Use (工具呼叫)**：AI 調用外部 API（如搜尋、計算機）。
   * **Planning (任務規劃)**：將大目標拆解成步驟執行。
   * **Multi-Agent (多智能體)**：多個角色互相質詢與合作。
5. **鋸齒邊界與協作模式 (Jagged Frontier)**：
   * **半人馬模式 (Centaurs)**：長 Prompt 委派整個任務（企業自動化流程）。
   * **生化人模式 (Cyborgs)**：人機高頻來回對話校正（創意與判斷型任務）。

## ⏱️ 附時間戳記的段落大綱
* `[00:00]` 課程引言：AI Engineer 時代的來臨與 Stanford Course 重點。
* `[01:00]` 橫軸訓練與縱軸工程的定義，及基礎模型的四大商業局限。
* `[03:34]` 鋸齒邊界（Jagged Frontier）、方向盤前打瞌睡與半人馬/生化人協作模型。
* `[06:15]` Prompt Engineering、RAG 與 Fine-Tuning 的優缺點橫向評估。
* `[09:30]` 代理人工作流（Agentic Workflow）的四種核心設計模式。
* `[11:30]` 系統性評估（Evaluation）與多代理人（Multi-Agent）框架結論。

## 🌐 中英專有名詞對照表
* **Augmenting LLMs**：大型語言模型增強工程
* **Lost in the Middle**：大上下文中間資訊遺失現象
* **Centaur / Cyborg**：半人馬模式 / 生化人模式
* **Agentic Workflow**：代理人工作流
* **LLM Evaluation**：大型語言模型評估體系

## 🏃‍♂️ 行動指南
* 閱讀並分析您的 AI 產品任務性質，選擇採用 Centaur 模式（一鍵自動化）或 Cyborg 模式（來回對答），並建置對應的 RAG 檢索流程。
