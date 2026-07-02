# 🎥 AI Agent 基本功 EP02：學習 Agent 必懂的核心觀念與初始化設定

## 📌 影片資訊
* **播放清單序號**：EP02
* **影片 ID**：8nwjYouFJoE
* **原始網址**：https://www.youtube.com/watch?v=8nwjYouFJoE
* **播放清單**：AI_Agent 基本功_學習Agent一定要看的一個系列
* **講者**：三叔Sense Bar
* **創作者**：三叔Sense Bar

---

## 🧠 核心概念與技術摘要
1. **本地執行權限的三種層級**：
   * **手動審查 / 待我核准 (Plan / Manual Mode)**：AI 在讀取、編輯檔案或執行任何指令前，都會彈出確認視窗。雖然最安全，但每次都需要按核准，非常浪費時間，且多數命令使用者也看不懂。
   * **半自動審查 (Auto / Turbo Mode)**：AI 自動執行大部分普通指令，僅在遇到刪除檔案、變更敏感設定或跨專案目錄操作時才會攔截確認。此為**最推薦新手**的設定。
   * **全自動無阻擋 (Bypass Permissions / Full Access)**：AI 在本地執行任何 Shell 指令或修改檔案均無需確認。適合對工作流極為熟悉的老手或封閉的沙盒測試。
2. **命令白名單 (Command Whitelist)**：
   * 在 AntiGravity 等平台的本地權限設定中，可自訂「放行關鍵字」。
   * **推薦放行命令**：將 `npm`、`python`、`pip` 加入白名單，讓 AI 在本地自動下載套件並跑程式，省去每次都要手動點擊核准的麻煩。
3. **全域設定 (Global Settings) 與專案設定 (Project-Scoped Settings)**：
   * **全域技能 (Global Skills)**：在所有對話、所有資料夾中都可被觸發的技能（例如：通用簡報製作、影片剪輯指令）。
   * **專案技能 (Project-Scoped Skills)**：僅在特定工作資料夾中生效的技能。**切勿將所有技能都塞入全域**，否則會因為技能過多、關鍵字重疊而導致 AI 觸發錯誤或解析錯亂。
4. **Agent 的啟動記憶機制**：
   * 每次 AI Agent 開啟新對話（Session）時，會先載入全域設定的藍圖檔案，再讀取目前專案資料夾下的專案設定檔。

## ⏱️ 附時間戳記的段落大綱
* `[00:00]` AI Agent 基本功第二集引言：介紹學習 Agent 必備的核心觀念與系統初始配置。
* `[00:35]` 本地電腦安全權限設定（給予 AI 多少執行權利）。
* `[01:20]` 實戰演示：在 Claude Code 中設定 Auto Mode 半自動執行與 Plan 規劃模式。
* `[02:30]` 權限全開（Bypass Permissions）的優缺點分析：執行快速，但有修改錯誤或刪除檔案風險。
* `[03:56]` 實戰演示：在 Codex 桌面版中設定「待我核准」與「自動審查」模式。
* `[05:08]` 為什麼建議新手直接選擇「半自動/待我核准」而非「每一步手動確認」。
* `[06:26]` 實戰演示：在 Google AntiGravity 設定中調整 Agent Settings 與權限安全機制。
* `[07:18]` 高級全自動技巧：在 Local Permissions 中設定 python、npm、pip 指令白名單直接放行。
* `[08:30]` 實戰演示：在開源 OpenCode 專案設定中啟用自動接受權限（Auto Accept）。
* `[09:40]` 技能安全性宣導：避免安裝來路不明的第三方 Skills 以防止木馬外洩隱私。
* `[10:44]` 全域設定（Global Settings）與專案設定（Project Settings）的定義與加載順序。
* `[11:35]` 技能分類法則：通用技能放全域，特殊學科/專案技能放專案目錄，避免關鍵字衝突。

## 🌐 中英專有名詞對照表
* **Auto Mode**：半自動執行模式
* **Bypass Permissions / Full Access**：繞過授權 / 完整存取權限
* **Turbo Mode**：加速模式 (AntiGravity 專屬)
* **Command Whitelist**：命令白名單
* **Global Settings / Project Settings**：全域設定 / 專案設定
* **Global Skills / Project-Scoped Skills**：全域技能 / 專案專屬技能
* **Malicious Skills**：惡意技能包 / 木馬技能

## 🏃‍♂️ 行動指南
* 開啟您的 Agent 設定介面，將權限調整為「半自動/Auto Mode/待我核准」。
* 在 AntiGravity 或您的 Agent 工具中，將 `python` 和 `pip` 加入免審查的 Local Command 白名單中。
* 思考：為什麼將不常用的技能包（Skills）設定為全域，會降低 AI 助理回答時的精準度？
