# 🎥 【機器學習2021】自督導式學習 (Self-supervised Learning) (一) – 芝麻街與進擊的巨人

## 📌 影片資訊
* **播放清單序號**：EP18
* **影片 ID**：e422eloJ0W4
* **原始網址**：https://www.youtube.com/watch?v=e422eloJ0W4
* **播放清單**：【機器學習2021】(中文版)
* **講者**：李宏毅教授

---

## 🧠 核心概念與技術摘要
1. **自督導式學習 (Self-supervised Learning)**：
   * 不需要人工標註的 Label。直接將無標註數據（如網路上的海量文本）的一部分蓋起來（Mask）或做為下一步預測目標，讓模型自己學會語言結構。
2. **BERT (Bidirectional Encoder Representations from Transformers)**：
   * **架構**：Transformer Encoder。
   * **訓練任務**：
     * **Masked LM (MLM)**：隨機將 15% 的 Token 蓋起來，預測被蓋住的字。
     * **Next Sentence Prediction (NSP)**：預測兩句話是否為相連的句子（後續研究發現此任務非必要）。
   * **優勢**：雙向上下文理解，極度適合做下游微調任務（Downstream Tasks，如分類、問答）。
3. **GPT (Generative Pre-trained Transformer)**：
   * **架構**：Transformer Decoder。
   * **訓練任務**：Autoregressive 預測下一個 Token。
   * **優勢**：強大的生成能力。演進到 GPT-3 後，展現出驚人的 Few-shot / Zero-shot 學習能力與湧現能力（Emergent Abilities）。

## 🌐 中英專有名詞對照表
* **Self-supervised Learning**：自督導式學習 / 自監督學習
* **Downstream Tasks**：下游微調任務
* **Masked Language Model (MLM)**：遮罩語言模型
* **Few-shot Learning**：少樣本學習

## 🏃‍♂️ 行動指南
* 區分 BERT (Encoder-based) 與 GPT (Decoder-based) 在預訓練任務上的根本差異。
* 理解 BERT 的微調過程如何只需極少標註資料即可在各 NLP 任務取得好成績。
