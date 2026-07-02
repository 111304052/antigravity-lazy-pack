# 🎥 【機器學習2021】Transformer (下)

## 📌 影片資訊
* **播放清單序號**：EP13
* **影片 ID**：N6aRv06iv2g
* **原始網址**：https://www.youtube.com/watch?v=N6aRv06iv2g
* **播放清單**：【機器學習2021】(中文版)
* **講者**：李宏毅教授

---

## 🧠 核心概念與技術摘要
1. **Transformer 整體架構**：
   * 基於 Seq2Seq (Sequence-to-Sequence) 模型，分為 Encoder (編碼器) 與 Decoder (解碼器) 兩大部分。
2. **Encoder (編碼器) 內部結構**：
   * 包含多個 Block。每個 Block 包含一個 Multi-head Self-attention、Residual Connection (殘差連接)、Layer Normalization (層標準化) 以及 Feed Forward Neural Network。
3. **Decoder (解碼器) 內部結構**：
   * **Autoregressice (AR)**：逐字輸出，將前一步的輸出做為下一步的輸入。
   * **Masked Self-attention**：在 Decoder 中，Self-attention 只能看見當前位置以前的資訊，無法預知未來的資訊（Mask 掉未來的 Token）。
   * **Cross-attention (Encoder-Decoder Attention)**：Decoder 利用它的 Query 去匹配 Encoder 產生的 Key 與 Value，實現編解碼器的資訊傳遞。
4. **Non-Autoregressive (NAT) 解碼**：
   * 一次性輸出所有 Token。優點是解碼速度極快（平行化），但缺點是表現通常不如 AR 模型（有 Multi-modality 問題）。

## 🌐 中英專有名詞對照表
* **Seq2Seq**：序列到序列模型
* **Residual Connection**：殘差連接
* **Layer Normalization**：層標準化
* **Autoregressive (AR)**：自迴歸
* **Cross-attention**：交叉注意力機制
* **Non-Autoregressive (NAT)**：非自迴歸

## 🏃‍♂️ 行動指南
* 畫出 Transformer Encoder 與 Decoder 的細部串接流程圖。
* 明白 Layer Normalization 與 Batch Normalization 的計算維度差異。
