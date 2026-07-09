# 🎥 加快語言模型生成速度 (2/2)：KV Cache

## 📌 影片資訊
* **播放清單序號**：EP06
* **影片 ID**：fDQaadKysSA
* **原始網址**：https://www.youtube.com/watch?v=fDQaadKysSA
* **播放清單**：【機器學習2026】
* **講者**：李宏毅教授

---

## 🧠 核心概念與技術摘要
1. **Autoregressice Decoding（自迴歸解碼）的冗餘**：
   * 語言模型在生成文本時，是「逐字輸出」（Token by Token）。生成第 $t$ 個 Token 時，需要與前 $t-1$ 個 Token 進行注意力計算。
   * 在 Naive（無優化）狀態下，每生成一個新字，前 $t-1$ 個歷史 Token 的 Key ($K$) 和 Value ($V$) 矩陣都需要重新計算一次，這產生了巨大的重複矩陣相乘運算。
2. **KV Cache（鍵值快取）的原理**：
   * **空間換時間**：在 GPU 記憶體中，開闢一塊暫存空間，將已經生成過的 Token 的 Key ($K$) 與 Value ($V$) 向量儲存起來。
   * **增量計算**：當生成下一個 Token 時，模型只需要為「這一個新 Token」計算全新的 $Q$、$K$、$V$ 向量。然後將新的 $K$、$V$ 追加到 Cache 中，與快取中的舊 $K$、$V$ 直接做 Attention 點積。
3. **KV Cache 的代價：顯存佔用暴增**：
   * 隨着 Context 長度增加，KV Cache 佔用的顯存呈線性增長。例如，一個 70B 的模型在長上下文下，KV Cache 甚至可能超出單張 GPU 顯存。
4. **KV Cache 變體優化**：
   * **Multi-Query Attention (MQA)**：所有 Query Head 共享同一組 Key Head 和 Value Head，大幅減少快取體積。
   * **Grouped-Query Attention (GQA)**：將 Query Head 分組，每組共享一組 Key 和 Value Head，在運算速度與模型精度之間取得最佳平衡。

## ⏱️ 附時間戳記的段落大綱
* `[00:03]` 自迴歸（Autoregressive）文本生成的逐步推理特徵與效能瓶頸。
* `[03:00]` 傳統計算方式中「歷史 Token 重複計算」的運算浪費展示。
* `[09:01]` KV Cache（鍵值快取）概念的提出與工作原理詳解。
* `[15:01]` 動態內存分配：如何在矩陣尾部追加（Append）最新的 Key-Value 向量。
* `[21:00]` 顯存帶寬瓶頸（Memory Bandwidth Bound）對 GPU 運算單元利用率的限制。
* `[30:02]` Flash Decoding 技術：如何並行化處理極長 sequence 下的 KV Cache 讀取。
* `[33:02]` 減少快取體積的高級注意力架構：MQA 與 GQA 的頭部共享結構與數學原理。

## 🌐 中英專有名詞對照表
* **KV Cache**：鍵值快取 / 鍵值緩存
* **Autoregressive Decoding**：自迴歸解碼
* **Multi-Query Attention (MQA)**：多查詢注意力機制
* **Grouped-Query Attention (GQA)**：群組查詢注意力機制
* **Memory Bandwidth Bound**：記憶體頻寬限制
* **Flash Decoding**：閃電解碼技術

## 🏃‍♂️ 行動指南
* 計算一個 7B 模型（如 LLaMA），在 batch_size=4、上下文長度=4096、FP16 精度下，KV Cache 所需的實體顯存大小（GB）。
* 比較 MQA、GQA 與標準 Multi-Head Attention (MHA) 的架構差異，並說明 GQA 為什麼能成爲當前開源大模型（如 LLaMA-3）的主流選擇。
