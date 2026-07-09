# 🎥 AI Agent (2/3): AI Agent 之間可以有什麼樣的互動

## 📌 影片資訊
* **播放清單序號**：EP03
* **影片 ID**：mmPmNezjCi0
* **原始網址**：https://www.youtube.com/watch?v=mmPmNezjCi0
* **播放清單**：【機器學習2026】
* **講者**：李宏毅教授

---

## 🧠 核心概念與技術摘要
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
