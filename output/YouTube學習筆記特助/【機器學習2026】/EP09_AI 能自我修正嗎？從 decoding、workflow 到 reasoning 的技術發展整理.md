# 🎥 AI 能自我修正嗎？從 decoding、workflow 到 reasoning 的技術發展整理

## 📌 影片資訊
* **播放清單序號**：EP09
* **影片 ID**：m3i2mk5hs8U
* **原始網址**：https://www.youtube.com/watch?v=m3i2mk5hs8U
* **播放清單**：【機器學習2026】
* **講者**：李宏毅教授

---

## 🧠 核心概念與技術摘要
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
