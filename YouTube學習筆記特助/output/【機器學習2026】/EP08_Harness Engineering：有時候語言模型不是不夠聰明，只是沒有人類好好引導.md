# 🎥 Harness Engineering：有時候語言模型不是不夠聰明，只是沒有人類好好引導

## 📌 影片資訊
* **播放清單序號**：EP08
* **影片 ID**：R6fZR_9kmIw
* **原始網址**：https://www.youtube.com/watch?v=R6fZR_9kmIw
* **播放清單**：【機器學習2026】
* **講者**：李宏毅教授

---

## 🧠 核心概念與技術摘要
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
