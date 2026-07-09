# 🎥 AI Agent (1/3)：核心技術 Context Engineering 基本概念解說

## 📌 影片資訊
* **播放清單序號**：EP02
* **影片 ID**：urwDLyNa9FU
* **原始網址**：https://www.youtube.com/watch?v=urwDLyNa9FU
* **播放清單**：【機器學習2026】
* **講者**：李宏毅教授

---

## 🧠 核心概念與技術摘要
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
