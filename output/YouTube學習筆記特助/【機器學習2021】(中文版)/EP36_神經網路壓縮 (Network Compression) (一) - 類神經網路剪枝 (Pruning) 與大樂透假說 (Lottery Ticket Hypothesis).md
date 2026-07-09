# 🎥 【機器學習2021】神經網路壓縮 (Network Compression) (一) - 類神經網路剪枝 (Pruning) 與大樂透假說 (Lottery Ticket Hypothesis)

## 📌 影片資訊
* **播放清單序號**：EP36
* **影片 ID**：utk3EnAUh-g
* **原始網址**：https://www.youtube.com/watch?v=utk3EnAUh-g
* **播放清單**：【機器學習2021】(中文版)
* **講者**：李宏毅教授

---

## 🧠 核心概念與技術摘要
1. **為什麼需要網路壓縮**：
   * 為了在資源受限的邊緣設備（如手機、晶片、嵌入式設備）上運行龐大的類神經網路。
2. **網路剪枝 (Network Pruning)**：
   * 評估權重 (Weights) 或神經元 (Neurons) 的重要性（如看 $L_1/L_2$ 數值），將不重要的連結刪除，使模型稀疏化 (Sparse)，降低計算量。
3. **大樂透假說 (Lottery Ticket Hypothesis)**：
   * 稠密的神經網路中，包含著一組「中獎的子網路 (Winning Ticket)」。這組子網路在隨機初始狀態下，以相同初始參數獨立訓練，能達到與原網路相同的準確度。
4. **知識蒸餾 (Knowledge Distillation)**：
   * 訓練一個小模型（Student）去模仿大模型（Teacher）的輸出機率分布（Soft Targets），能將大模型的泛化能力轉移給小模型。
5. **參數化量化 (Quantization) 與 Depthwise Separable CNN**：
   * 將 32-bit 浮點數權重壓縮成 8-bit 整數。使用 Depthwise Separable 卷積大幅減少 CNN 的乘加運算次數。

## 🌐 中英專有名詞對照表
* **Network Pruning**：網路剪枝
* **Lottery Ticket Hypothesis**：大樂透假說
* **Knowledge Distillation**：知識蒸餾
* **Soft Targets**：軟目標 (富含暗物質的機率分布)

## 🏃‍♂️ 行動指南
* 明白知識蒸餾中，為什麼 Student 去學 Teacher 輸出的 Softmax 機率（如 `[0.7, 0.2, 0.1]`）比只學 Hard Label (`[1, 0, 0]`) 能學到更多知識。
