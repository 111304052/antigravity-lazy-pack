# 🎥 【機器學習2021】生成式對抗網路 (Generative Adversarial Network, GAN) (三) – 生成器效能評估與條件式生成

## 📌 影片資訊
* **播放清單序號**：EP16
* **影片 ID**：MP0BnVH2yOo
* **原始網址**：https://www.youtube.com/watch?v=MP0BnVH2yOo
* **播放清單**：【機器學習2021】(中文版)
* **講者**：李宏毅教授

---

## 🧠 核心概念與技術摘要
1. **GAN 的基本架構：對抗博弈**：
   * **Generator (生成器)**：輸入隨機雜訊，嘗試生成與真實數據分布相似的假數據，目標是「騙過 Discriminator」。
   * **Discriminator (判別器)**：輸入真實與生成的假數據，輸出一個分數，目標是「精準分辨真假」。
2. **數學原理與 Divengence 的關係**：
   * GAN 訓練的本質是最小化真實分布 $P_{data}$ 與生成分布 $P_G$ 之間的 Divergence (散度)。
   * 傳統 GAN（使用 JS Divergence）在兩分布幾乎沒有重疊時，判別器能輕易做到 100% 分辨，導致生成器得不到任何梯度。
3. **WGAN (Wasserstein GAN)**：
   * 使用 Earth Mover's Distance (Wasserstein Distance) 替代 JS 散度。即使分布沒有重疊，依然能提供平滑的梯度。
   * 限制：判別器必須滿足 1-Lipschitz 函數限制，常以 Gradient Penalty (梯度懲罰) 實現。
4. **Conditional GAN 與 Cycle GAN**：
   * **Conditional GAN**：輸入隨機雜訊的同時加上條件 (Condition) 向量，指定生成特定特徵的圖片（如指定紅髮、戴眼鏡）。
   * **Cycle GAN**：在無對齊數據下進行風格轉換。透過「X ➔ Y ➔ X」的循環一致性損失 (Cycle Consistency Loss)，確保轉換後的圖片保留原圖的輪廓特徵。

## 🌐 中英專有名詞對照表
* **Generator / Discriminator**：生成器 / 判別器
* **Wasserstein Distance**：沃瑟斯坦距離 (推土機距離)
* **Gradient Penalty**：梯度懲罰
* **Conditional GAN**：條件式生成對抗網路
* **Cycle Consistency Loss**：循環一致性損失

## 🏃‍♂️ 行動指南
* 明白為什麼 JS Divergence 在 GAN 訓練初期會導致梯度消失。
* 思考 Cycle GAN 的循環一致性損失如何限制模型不要生成不相干的圖片。
