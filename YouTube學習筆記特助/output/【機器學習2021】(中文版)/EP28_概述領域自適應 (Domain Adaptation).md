# 🎥 【機器學習2021】概述領域自適應 (Domain Adaptation)

## 📌 影片資訊
* **播放清單序號**：EP28
* **影片 ID**：Mnk_oUrgppM
* **原始網址**：https://www.youtube.com/watch?v=Mnk_oUrgppM
* **播放清單**：【機器學習2021】(中文版)
* **講者**：李宏毅教授

---

## 🧠 核心概念與技術摘要
1. **什麼是 Domain Adaptation**：
   * **Source Domain (源領域)**：有大量有標註的訓練資料。
   * **Target Domain (目標領域)**：只有無標註或極少標註的資料，且與 Source Domain 存在分布差異（Domain Shift，例如真實貓咪照 vs. 卡通貓咪畫）。
2. **對抗式領域自適應 (Domain Adversarial Training)**：
   * 引入一個 **Domain Classifier (領域分類器)**，嘗試分辨特徵是來自 Source 還是 Target。
   * **Feature Extractor (特徵提取器)** 的目標是「提取出能騙過領域分類器的特徵」（即不分領域的通用特徵），藉此縮小兩領域間的分布距離。

## 🌐 中英專有名詞對照表
* **Source Domain / Target Domain**：源領域 / 目標領域
* **Domain Shift**：領域偏移
* **Domain Adversarial Training**：領域對抗訓練

## 🏃‍♂️ 行動指南
* 理解 Domain Adversarial Neural Network (DANN) 的梯度反轉層 (Gradient Reversal Layer) 如何實現對抗訓練。
