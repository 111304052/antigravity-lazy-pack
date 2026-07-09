# 🎥 【機器學習2021】機器終身學習 (Life Long Learning, LL) (一) - 為什麼今日的人工智慧無法成為天網？災難性遺忘(Catastrophic Forgetting)

## 📌 影片資訊
* **播放清單序號**：EP34
* **影片 ID**：rWF9sg5w6Zk
* **原始網址**：https://www.youtube.com/watch?v=rWF9sg5w6Zk
* **播放清單**：【機器學習2021】(中文版)
* **講者**：李宏毅教授

---

## 🧠 核心概念與技術摘要
1. **災難性遺忘 (Catastrophic Forgetting)**：
   * 類神經網路在學會任務 A 後，若直接用任務 B 的資料進行訓練，會導致模型參數劇烈改變，徹底忘記如何做任務 A。這是當前 AI 與人類大腦最大的差異之一。
2. **克服之道 ── EWC (Elastic Weight Consolidation)**：
   * 在學習任務 B 時，限制那些對任務 A 極度重要的參數 $	heta_i$ 不要改變太多。
   * 利用 Fisher Information Matrix 來評估參數對舊任務的重要程度，並在 Loss Function 中加上二次懲罰項。
3. **其他方法**：
   * **Memory Replay (記憶重放)**：在學新任務時，混合一部分舊任務的歷史資料一起訓練。
   * **Progressive Neural Networks**：為新任務開闢新的網絡分支，保留舊網絡的參數不動。

## 🌐 中英專有名詞對照表
* **Catastrophic Forgetting**：災難性遺忘
* **Elastic Weight Consolidation (EWC)**：彈性權重整合
* **Fisher Information Matrix**：費雪訊息矩陣

## 🏃‍♂️ 行動指南
* 明白 EWC 如何利用二次損失項來約束重要權重的移動範圍。
