# 🎥 我做 AI Agent 一年,90% 在做表面功夫——直到我換了思路

## 📌 影片資訊
* **影片 ID**：H0XmxIalAEQ
* **原始網址**：https://www.youtube.com/watch?v=H0XmxIalAEQ
* **講者**：數字黑魔法

---

## 🧠 核心概念與技術摘要
1. **AI Agent 開發痛點：手動測試占據 90% 的時間**：
   * AI Agent 系統具備隨機性與不確定性，微調 Prompt 可能導致其他功能損壞。缺乏自動化測試時，開發者必須反覆手動點擊網頁、輸入測試集並用肉眼判斷好壞。
2. **驗證的不對稱性 (Verification Asymmetry) 與 Verifier's Rule**：
   * OpenAI 研究員 Jason Wei 提出：生成任務很難，但驗證正確性很容易。Verifier's Rule 指出：*任何可解且易於驗證的任務終將被 AI 解決*。Agent 開發的瓶頸在於「生成便宜、驗證昂貴」。
3. **晶片設計與驗證 (IC Verification) 的啟示**：
   * 晶片行業中，驗證工程師與設計工程師的比例常為 2:1 或 3:1，因為流片失敗代價極高。當 AI 讓代碼編寫變得極其廉價時，開發的核心價值轉向「建置可自動化、可重複的驗證/回歸測試體系」。
4. **可驗證 Agent 架構實踐步驟**：
   * **步驟 1：可程式化與可觀測性 (Controllability & Observability)**：將 Agent 改造成對程式友好的 API 接口，回傳結構化 JSON，並輸出中間決策路徑。
   * **步驟 2：建置回歸測試集 (Regression Test Suite)**：累積歷史測試案例與黃金標準資料（Golden Dataset）。
   * **步驟 3：量化評估指標 (Evaluation Metrics)**：使用斷言（Assertions）、LLM-as-a-judge 或程式語法檢查，取代肉眼與直覺判斷。

## ⏱️ 附時間戳記的段落大綱
* `[00:00]` 痛點揭露：為什麼開發 AI Agent 時 90% 的時間都在做手動測試？
* `[01:16]` Jason Wei 的 Verifier's Rule 觀點：生成便宜與驗證昂貴的不對稱性。
* `[02:30]` 晶片設計（IC Design）行業的歷史隱喻：設計與驗證的角色轉變。
* `[04:00]` 打造可驗證 AI Agent 的三大具體步驟：API 化、回歸測試與量化指標。

## 🌐 中英專有名詞對照表
* **Verification Asymmetry**：驗證不對稱性
* **Verifier's Rule**：驗證者定律
* **Regression Testing**：回歸測試
* **Observability**：可觀測性 / 可監測性
* **LLM-as-a-judge**：以大型語言模型作為裁判

## 🏃‍♂️ 行動指南
* 將您目前開發的 Agent 改寫為能接收並輸出 JSON 的 API，並為其編寫一個包含 3 個歷史案例的簡單 Python 測試腳本。
