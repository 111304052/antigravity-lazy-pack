# 🎥 AntiGravity 基本功 EP02：備課神器（自動處理多個 Word/Ppt 與 PDF OCR 出題）

## 📌 影片資訊
* **標題**：AntiGravity基本功EP02:備課神器_自動處理多個Word/Ppt簡報檔案_隨機出題...
* **講者/頻道**：三師爸Sense Bar
* **原始網址**：https://www.youtube.com/watch?v=U4C0dGbQtQA
* **播放清單**：AntiGravity_google_AI_Agents

## 🧠 核心概念與技術摘要
1. **教學檔案急速批次處理**：
   * 展示如何讓 Agent 自動去網路上下載歷屆國中教育會考數學題 PDF 檔案到本地專案目錄。
2. **PDF OCR 數學解題實測**：
   * 測試 AntiGravity 讀取 PDF 當中特定的數學幾何選擇題（例如 110 年第 4 題），AI 能直接理解幾何圖形結構、解釋算式並寫出正確解答（選 C）。
3. **自訂 Word 與 PPT 產生腳本**：
   * 利用 Python 的 `python-docx` 與 `python-pptx` 套件，讓 Agent 讀取外部規格文件，直接生成排版精美的考卷 Word 檔與簡報 PPT 檔。
4. **跨 Agent 技能（Skills）移植**：
   * 展示將 Claude Code 寫好的 Markdown 格式技能（Skills）直接丟給 AntiGravity，它同樣能完美讀懂並成功安裝與執行。

## 🏃‍♂️ 行動指南
* 本地安裝 `python-docx` 與 `python-pptx` 函式庫。
* 設計一個 `math_reference.docx` 放置出題標準。
* 丟給 Agent 會考 PDF，下指令「讀取並解析第 N 題」測試 OCR 精準度。
