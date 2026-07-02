# 🎥 如何讓 Transformer 知道輸入 Token 的順序？Absolute、Relative、RoPE、到沒有 Positional Embedding

## 📌 影片資訊
* **播放清單序號**：EP07
* **影片 ID**：Ll-wk8x3G_g
* **原始網址**：https://www.youtube.com/watch?v=Ll-wk8x3G_g
* **播放清單**：【機器學習2026】
* **講者**：李宏毅教授

---

## 🧠 核心概念與技術摘要
1. **為什麼 Self-attention 需要位置編碼**：
   * 自注意力機制公式 $\text{Attention}(Q, K, V) = \text{softmax}(\frac{QK^T}{\sqrt{d_k}})V$ 中不包含任何位置順序資訊。如果打亂輸入 Token 的順序，輸出的特徵向量完全相同（置換不變性 Permutation Invariance）。
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
