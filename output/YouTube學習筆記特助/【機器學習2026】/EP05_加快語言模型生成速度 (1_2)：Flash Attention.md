# 🎥 加快語言模型生成速度 (1/2)：Flash Attention

## 📌 影片資訊
* **播放清單序號**：EP05
* **影片 ID**：vXb2QYOUzl4
* **原始網址**：https://www.youtube.com/watch?v=vXb2QYOUzl4
* **播放清單**：【機器學習2026】
* **講者**：李宏毅教授

---

## 🧠 核心概念與技術摘要
1. **注意力機制的計算瓶頸**：
   * 傳統 Self-attention 計算中，注意力矩陣的計算與儲存複雜度是 $O(L^2)$（$L$ 為序列長度），成爲處理長文本（長 Context）時的硬傷。
2. **GPU 記憶體階層與頻寬瓶頸**：
   * GPU 的記憶體分爲 **HBM (High Bandwidth Memory，高頻寬記憶體/顯存，大但慢)** 與 **SRAM (晶載靜態隨機存取記憶體，極快但極小，如每個 SM 幾十 KB)**。
   * Naive Attention 需要將 $L 	imes L$ 的中間矩陣寫回 HBM，再讀出來計算 Softmax，這種頻寬頻繁讀寫（IO-bottleneck）是主要的延遲來源。
3. **Flash Attention 的核心優化 ── Tiling (分塊)**：
   * Flash Attention 不在 HBM 中儲存巨大的 $L 	imes L$ 矩陣，而是將 Query、Key、Value 矩陣切分成小塊（Tiles）載入 SRAM。
   * 在 SRAM 中計算局部注意力分數，直接完成 Weighted Sum 輸出，最後只將最終結果寫回 HBM。
4. **Online Softmax（在線 Softmax 計算）**：
   * Softmax 需要全局最大值 $m(x)$ 與全局分母和 $d(x)$ 進行歸一化。分塊計算時，我們無法一次獲得全局最大值。
   * **解決方案**：動態更新中間值。當計算到新塊時，利用公式 $\text{new\_sum} = \text{old\_sum} \times e^{m_{\text{old}} - m_{\text{new}}} + e^{x - m_{\text{new}}}$，動態縮放並修正之前的局部 Softmax 分母與分子，確保在數學上與全局 Softmax 完全等價。

## ⏱️ 附時間戳記的段落大綱
* `[00:00]` 加快語言模型生成速度的主題引言，Attention 的計算複雜度挑戰。
* `[03:01]` 溫習 Softmax 歸一化原理及其在數值計算中的溢出問題。
* `[06:01]` Flash Attention 論文背景介紹與作者 Tri Dao 的核心出發點。
* `[09:01]` GPU 硬體架構剖析：顯存 HBM 與芯片緩存 SRAM 的讀寫速度差距。
* `[12:00]` 分塊（Tiling）算法：如何在不離開 SRAM 的情況下完成 QK 點積。
* `[18:02]` 分塊計算下面臨的局部 Softmax 與全局 Softmax 不對等問題。
* `[24:02]` 在線 Softmax（Online Softmax）的動態歸一化因子調整機制。
* `[33:00]` Online Softmax 的數值穩定性推導與動態分母累加算式。
* `[39:01]` 局部縮放因子（$s_1, s_2$）在代碼執行時的動態轉換過程。
* `[42:01]` PyTorch 中 Q, K, V 矩陣分塊初始化的代碼結構與內存分配。
* `[48:00]` Naive Attention 與 Flash Attention 的運作毫秒數（ms）與顯存佔用對比。

## 🌐 中英專有名詞對照表
* **Flash Attention**：閃電注意力機制 / 快速注意力計算
* **High Bandwidth Memory (HBM)**：高頻寬記憶體 / 顯存
* **Static Random-Access Memory (SRAM)**：晶載快取記憶體
* **IO-bottleneck / Memory-bound**：記憶體讀寫瓶頸 / 記憶體受限
* **Tiling / Block**：分塊技術 / 矩陣區塊
* **Online Softmax**：在線式 Softmax 演算法

## 🏃‍♂️ 行動指南
* 推導 Online Softmax 的更新公式，證明其分塊計算結果與一次性計算全局 Softmax 的數學結果一致。
* 思考：Flash Attention 優化的是運算時間（Speed）還是顯示記憶體佔用（Memory），或者兩者皆有？
