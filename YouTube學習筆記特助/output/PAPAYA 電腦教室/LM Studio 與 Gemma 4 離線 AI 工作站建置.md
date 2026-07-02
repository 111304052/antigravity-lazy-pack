# 🎥 別再小看本地 AI！Gemma 4 + LM Studio 讓你的電腦變成超級離線 AI 工作站，而且完全免費 (手機也能使用喔！)

## 📌 影片資訊
* **影片 ID**：r5M0W66xcGc
* **原始網址**：https://www.youtube.com/watch?v=r5M0W66xcGc
* **講者**：PAPAYA 電腦教室
* **類別**：單一影片學習筆記

---

## 🧠 核心概念與技術摘要
1. **本機 AI 的優勢（Offline LLM）**：
   * 完全在個人電腦運行，無需網際網路，100% 保障資料安全與隱私，且完全免費，沒有 Token 額度限制。
2. **LM Studio 軟體與模型配置**：
   * 一款簡單好用的本地模型載入器。支援下載 GGUF 格式的模型檔案（如 Gemma 4 或者是輕量化的 A3B 模型）。
   * 提供 **System Prompt (系統提示詞)** 欄位，可用來調教本地模型的角色設定。
3. **進階本地應用與數據分析**：
   * 支援在本地上傳 CSV 格式的結構化表格資料，讓本地 AI 進行數據統計、過濾與趨勢分析。
   * **工具調用 (Tool Use / Function Calling)**：本地模型同樣支援 Function Calling，可呼叫本地 Python 腳本。
4. **局域網伺服器（Local Server）擴展**：
   * LM Studio 內建一鍵啟動 API 伺服器功能，將本機變成局域網 AI 主機。其他設備（如 iPhone/Android 手機）可以透過網路連接，免費使用這台電腦的運算力進行 AI 對話。
   * 本地自動化：結合 python 自動建立檔案夾（如名為「筆記」的目錄）。

## ⏱️ 附時間戳記的段落大綱
* `[00:02]` 本機 AI 概念介紹：免網際網路、零費用、隱私保全。
* `[02:01]` 安裝 LM Studio，搜尋並下載 Gemma 4 / A3B 等熱門本地 GGUF 模型。
* `[04:00]` 設定 System Prompt 定義本地 AI 助理的語意風格與限制。
* `[06:00]` 實測 CSV 資料上傳，讓離線 AI 在本機進行複雜表格數據分析。
* `[08:03]` 演示本地模型的 Tool Use（功能呼叫）執行能力。
* `[10:00]` 在 LM Studio 中啟用本地 API 伺服器（Local Port 1234）。
* `[12:00]` 手機端設定連線，共享電腦 GPU/CPU 運算力以使用免費離線 AI。
* `[14:01]` 實測本機 Python 腳本連動：自動建立「筆記」子資料夾。
* `[16:02]` 安全提示：如何信任本地開發者簽章，雙擊執行 Python 自動化代碼。

## 🌐 中英專有名詞對照表
* **LM Studio**：本地大模型加載平台
* **Gemma 4**：Google 開源本地大語言模型
* **GGUF**：本地模型通用儲存格式
* **System Prompt**：本機系統提示詞
* **Local Server / API Port**：本機伺服器 / 接口埠
* **Tool Use (Function Calling)**：工具調用 / 函數呼叫

## 🏃‍♂️ 行動指南
* 下載並安裝 LM Studio，搜尋並下載一個 3B 或 7B 的 GGUF 格式模型（如 Gemma-2-9b-it）。
* 開啟本地伺服器，使用 Python `requests` 寫一段簡單的腳本，發送對話 POST 請求到 `http://localhost:1234/v1/chat/completions`。
* 思考：本地運行大模型，對於電腦的硬體配置（CPU、GPU 顯存、記憶體）有何具體要求？
