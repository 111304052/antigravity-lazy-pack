# 🎥 【機器學習2021】類神經網路訓練不起來怎麼辦 (四)：損失函數 (Loss) 也可能有影響

## 📌 影片資訊
* **播放清單序號**：EP07
* **影片 ID**：O2VkP8dJ5FE
* **原始網址**：https://www.youtube.com/watch?v=O2VkP8dJ5FE
* **播放清單**：【機器學習2021】(中文版)
* **講者**：李宏毅教授

---

## 🧠 核心概念與技術摘要
1. **局部最小值 (Local Minima) vs. 鞍點 (Saddle Point)**：
   * 訓練卡住時，大部分人直覺是遇到了 Local Minima，但高維度空間中，更多時候是遇到了 **Saddle Point (鞍點)**。
   * 鞍點的特徵是：在某些維度是極小值，但在其他維度仍有出路。可以透過計算 Hessian 矩陣的特徵值來判斷。
2. **Batch Size 的選擇與影響**：
   * **Small Batch**：雜訊大，梯度更新方向隨機。優點是能幫助模型跳出鞍點/局部最小值，且具有更好的泛化能力 (Generalization)。
   * **Large Batch**：計算速度快（GPU 平行化佳），但容易卡在起點，且傾向收斂到 Sharp Minima，泛化表現較差。
3. **Momentum (動量)**：
   * 模擬物理學中的慣性。更新方向不只看當前的梯度，還加入上一步移動的方向，能幫助模型衝過平坦區與局部鞍點。
4. **自動調整學習速率 (Learning Rate)**：
   * 不同的參數需要不同的學習速率。**Adagrad / RMSprop / Adam** 透過統計歷史梯度的平方和，實現「坡度陡的參數走小步，坡度平緩的參數走大步」。
5. **Batch Normalization (批次標準化)**：
   * 解決 Internal Covariate Shift 問題。在每一層的前向傳播中，將同一個 Batch 內的激活特徵值進行 Normalization（減均值除標準差），使 Loss Landscape 更平滑，加速模型收斂。

## 🌐 中英專有名詞對照表
* **Saddle Point**：鞍點
* **Hessian Matrix**：海森矩陣
* **Momentum**：動量
* **Batch Normalization**：批次標準化

## 🏃‍♂️ 行動指南
* 明白 Adam 結合了 Momentum (一階動量) 與 RMSprop (二階學習率調整) 的核心算式。
* 思考為什麼小 Batch 能帶來更好的 Generalization。
