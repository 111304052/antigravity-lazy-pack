# 🎥 【機器學習2021】來自人類的惡意攻擊 (Adversarial Attack) (下) – 類神經網路能否躲過人類深不見底的惡意？

## 📌 影片資訊
* **播放清單序號**：EP25
* **影片 ID**：z-Q9ia5H2Ig
* **原始網址**：https://www.youtube.com/watch?v=z-Q9ia5H2Ig
* **播放清單**：【機器學習2021】(中文版)
* **講者**：李宏毅教授

---

## 🧠 核心概念與技術摘要
1. **對抗攻擊 (Adversarial Attack) 的原理**：
   * 在輸入的圖片/文字中，加入極度微小、人類肉眼無法察覺的擾動向量 $\Delta x$，就能讓訓練好的深度模型徹底分類錯誤。
2. **攻擊方法分類**：
   * **Non-targeted Attack**：目標是讓模型認錯即可。
   * **Targeted Attack**：目標是讓模型認成「指定的錯誤類別」（例如將貓認成鍵盤）。
3. **FGSM (Fast Gradient Sign Method)**：
   * 沿著 Loss 增加的方向（即梯度方向的 Sign 函數）前進一步，快速計算出干擾向量。
4. **防禦機制 (Defense)**：
   * **Passive Defense**：在輸入端加上模糊化、壓縮等圖像預處理，破壞惡意擾動。
   * **Active Defense (Adversarial Training)**：在訓練過程中加入被攻擊的對抗樣本，進行對抗訓練，增強模型本身的魯棒性 (Robustness)。

## 🌐 中英專有名詞對照表
* **Adversarial Attack**：對抗攻擊 / 惡意攻擊
* **Targeted Attack**：目標攻擊
* **FGSM**：快速梯度對角方法
* **Adversarial Training**：對抗訓練

## 🏃‍♂️ 行動指南
* 思考為什麼深度學習模型在高維空間中如此脆弱，容易受到微小干擾的影響。
* 實作一個 FGSM 干擾產生器，測試您訓練好的分類器。
