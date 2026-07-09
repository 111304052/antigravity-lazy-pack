# 🎥 Claude code desktop  從零打造 AI 語音輸入工具

## 📌 影片資訊
* **播放清單序號**：專題
* **影片 ID**：laSfvJmD5nc
* **原始網址**：https://www.youtube.com/watch?v=laSfvJmD5nc
* **播放清單**：Claude code基本功
* **講者**：三叔Sense Bar

---

## 🧠 核心概念與技術摘要
1. **語音輸入工具需求**：
   * 教師備課或行政寫信時，手動打字速度較慢，需要將語音即時且高精度地轉為繁體中文文字。
2. **本機工具整合開發**：
   * 使用 Claude Code 在本機整合系統錄音模組（Python PyAudio/Sounddevice）與 OpenAI Whisper API（或本地端語音識別庫），一鍵啟動錄音、自動辨識並自動寫入目前焦點視窗中。

## ⏱️ 附時間戳記的段落大綱
* `[00:00]` 課程引言：提高行政效率！如何從零開發出專屬的本機語音輸入工具。
* `[02:40]` 語音輸入工具的架構設計與 Python 套件安裝。
* `[05:30]` 整合錄音與 Whisper API 辨識模組。
* `[08:15]` 系統焦點視窗自動貼上（Text Injection）邏輯撰寫與現場測試。

## 🌐 中英專有名詞對照表
* **Voice Input Tool**：語音輸入工具
* **Speech-to-Text (STT)**：語音轉文字
* **Whisper API**：OpenAI 語音識別應用介面
* **Text Injection**：文字自動寫入/注入

## 🏃‍♂️ 行動指南
* 請 Agent 撰寫一段簡單的 Python 錄音測試腳本，能錄製 5 秒鐘音訊並儲存為 WAV 檔案。
