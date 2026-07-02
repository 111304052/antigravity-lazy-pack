# 🎥 【機器學習2021】機器學習模型的可解釋性 (Explainable ML) (下) –機器心中的貓長什麼樣子？

## 📌 影片資訊
* **播放清單序號**：EP27
* **影片 ID**：0ayIPqbdHYQ
* **原始網址**：https://www.youtube.com/watch?v=0ayIPqbdHYQ
* **播放清單**：【機器學習2021】(中文版)
* **講者**：李宏毅教授

---

## 🧠 核心概念與技術摘要
1. **為什麼需要可解釋性 (Explainable ML)**：
   * 深度學習常被批評為「黑盒子 (Black Box)」。在醫療診斷、法律審判、金融貸款等高風險場景，必須理解模型的決策依據，人類才能信任它。
2. **局部解釋 (Local Explanation) ── 為什麼模型判定這張圖是貓**：
   * **Saliency Map (顯著圖)**：對輸入圖像的像素求 Loss 的偏微分，數值越大代表該像素的微小改變對最終預測影響越大（即模型最關注的區域）。
   * **LIME (Local Interpretable Model-agnostic Explanations)**：在被解釋樣本周圍進行擾動採樣，訓練一個簡單的線性模型進行局部逼近。
3. **全局解釋 (Global Explanation) ── 模型心中的貓長怎樣**：
   * **Activation Maximization**：尋找一個輸入圖像 $x$，使神經網路中代表「貓」的神經元輸出值最大化（通常需要加上正則化限制，否則只會產生雜訊）。

## 🌐 中英專有名詞對照表
* **Local Explanation**：局部解釋
* **Global Explanation**：全局解釋
* **Saliency Map**：顯著圖 / 突顯圖
* **Black Box**：黑盒子

## 🏃‍♂️ 行動指南
* 理解 Saliency Map 的計算方式，並使用 PyTorch 實作一張顯著圖。
