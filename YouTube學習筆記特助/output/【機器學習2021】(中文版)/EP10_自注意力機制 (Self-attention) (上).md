# 🎥 【機器學習2021】自注意力機制 (Self-attention) (上)

## 📌 影片資訊
* **播放清單序號**：EP10
* **影片 ID**：hYdO9CscNes
* **原始網址**：https://www.youtube.com/watch?v=hYdO9CscNes
* **播放清單**：【機器學習2021】(中文版)
* **講者**：李宏毅教授

---

## 🧠 核心概念與技術摘要
1. **為什麼需要 Self-attention**：
   * 傳統的 Fully Connected (FC) 或 CNN 在處理「輸入是向量序列且長度不固定」（例如排版好的句子、語音訊號、圖形結構）時力有未逮。
   * RNN 雖然能處理序列，但無法平行化計算且有長距離遺忘問題。Self-attention 能平行運算並捕捉全局上下文。
2. **Q、K、V 的運作機制**：
   * 對於每個輸入向量 $x^i$，先乘上不同的權重矩陣得到 Query ($q^i$)、Key ($k^i$)、Value ($v^i$)。
   * **Attention Score (注意力分數)**：計算 $q^i$ 與所有 $k^j$ 的 Dot Product，並除以 $\sqrt{d}$（Scaling）以穩定梯度。
   * **Softmax**：對分數進行 Softmax 標準化，得到 Attention Weight $lpha_{i,j}$。
   * **Weighted Sum**：將 $lpha_{i,j}$ 與對應的 $v^j$ 相乘加總，得到該位置的輸出 $lpha^i$。
3. **Multi-head Self-attention**：
   * 使用多個不同的 $W^Q, W^K, W^V$ 投影矩陣，讓模型能在不同的維度與子空間中學習不同的關聯性。
4. **Positional Encoding (位置編碼)**：
   * Self-attention 本身不包含任何位置資訊（即輸入順序改變，輸出內容相同）。為了解決此限制，必須加上額外的位置編碼向量 $e^i$，為模型提供順序資訊。

## 🌐 中英專有名詞對照表
* **Self-attention**：自注意力機制
* **Query / Key / Value**：查詢 / 鍵 / 值
* **Dot Product**：點積
* **Multi-head Self-attention**：多頭自注意力機制
* **Positional Encoding**：位置編碼

## 🏃‍♂️ 行動指南
* 理解 Attention 計算公式：$	ext{Attention}(Q, K, V) = 	ext{softmax}\left(rac{QK^T}{\sqrt{d_k}}ight)V$。
* 思考 Self-attention、CNN 與 RNN 的差異：CNN 是受限的 Self-attention（只看局部範疇）；RNN 無法平行運算，Self-attention 可平行化。
