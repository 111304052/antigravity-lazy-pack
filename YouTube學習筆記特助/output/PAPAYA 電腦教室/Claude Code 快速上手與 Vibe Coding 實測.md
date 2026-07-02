# 🎥 還在羨慕別人用 AI 開發酷產品？Claude Code 保姆級教學讓你輕鬆體驗 Vibe Coding, 動動嘴就能做出 Anything！

## 📌 影片資訊
* **影片 ID**：2pM-7fBXc_M
* **原始網址**：https://www.youtube.com/watch?v=2pM-7fBXc_M
* **講者**：PAPAYA 電腦教室
* **類別**：單一影片學習筆記
* **創作者**：PAPAYA 電腦教室

---

## 🧠 核心概念與技術摘要
1. **Claude Code 終端機開發工具**：
   * Claude Code 是 Anthropic 官方推出的命令列 AI 開發助理，能在終端機直接讀寫本機代碼、跑編譯命令及執行 shell 指令。
2. **Vibe Coding（動嘴開發模式）**：
   * 開發者只需用口語下指令（甚至結合語音輸入），AI 就會自動在本地環境撰寫程式、下載並安裝缺少的 Python/Node 依賴套件。
3. **規劃與反思機制（Plan & Refinement）**：
   * 在執行任務前，可以下指令請 Claude 規劃一份詳細的技術藍圖，讓開發者確認無誤後才批准執行（Always Proceed/Confirm）。
   * Claude 能在背景反思代碼執行錯誤，並自動修正 bug 直至跑通。
4. **狀態保持與 Agents 管理**：
   * 對話期間可以暫時離開，而對話的上下文狀態會被完整保留。
   * 可以使用 `/Agents` 指令查詢當前正在背景運行的子代理，實現多任務併行。

## ⏱️ 附時間戳記的段落大綱
* `[00:02]` 課程引言：Vibe Coding 潮流與 Claude Code CLI 工具介紹。
* `[02:03]` 下載並配置 VS Code，安裝 Claude Code 並進行本地授權登入。
* `[04:00]` 在終端機中使用 Shift + Enter 進行多行指令輸入。
* `[06:00]` 任務委託：請 Claude 自動撰寫專案的系統設計藍圖與步驟。
* `[08:01]` 演示 Claude 在編譯出錯時自動捕捉 error 並自行修正 bug 的過程。
* `[10:01]` 退出工具後，說明本地對話與上下文歷史狀態如何被完整保存。
* `[12:02]` 權限代理：讓 AI 自主執行 package 安裝與環境編譯。
* `[14:00]` 雙擊左鍵開啟代碼檔案，實際檢視 AI 生成的邏輯。
* `[16:01]` 安全限制：如何在 Harness 腳手架中限制 AI 執行高風險 Shell 指令。
* `[18:01]` 使用 /Agents 指令監控背景運行的協作代理。
* `[22:01]` 概念成型：動嘴完成產品開發、驗證與測試。

## 🌐 中英專有名詞對照表
* **Claude Code**：Anthropic 官方 CLI 開發助理
* **Vibe Coding**：動嘴/氛圍編程
* **CLI (Command Line Interface)**：命令列介面
* **State Preservation**：狀態保持 / 對話歷史保存
* **/Agents**：代理監控指令

## 🏃‍♂️ 行動指南
* 本地安裝 Claude Code，並下指令「幫我寫一個簡單的計時器網頁，並使用 Python 啟動伺服器」，實測 Vibe Coding。
* 思考：Claude Code 與一般的 GitHub Copilot 網頁版/外掛版相比，最大的優勢在哪裡？
