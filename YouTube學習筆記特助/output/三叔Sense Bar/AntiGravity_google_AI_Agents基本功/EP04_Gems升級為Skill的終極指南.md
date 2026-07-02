# 🎥 AntiGravity 基本功 EP04:一鍵將 Gems 全面升級成 Skill 的終極指南_懶人包大放送

## 📌 影片資訊
* **播放清單序號**：EP04
* **影片 ID**：kmmYXntln_E
* **原始網址**：https://www.youtube.com/watch?v=kmmYXntln_E
* **播放清單**：AntiGravity_google_AI_Agents基本功
* **講者**：三叔Sense Bar

---

## 🧠 核心概念與技術摘要
1. **Gemini Gems 與 AntiGravity Skills 的差異**：
   * **Gems (自訂角色)**：是 Google Gemini 網頁版提供的提示詞包包，只能進行純文字聊天，無法調用本地工具。
   * **Skills (技能)**：是 AntiGravity 專屬的擴充指令包。它不僅包含 System Prompt，還包含**可執行的 Supporting Scripts (輔助腳本)**，讓 AI 能直接調用本機程式來執行實體任務（如修圖、分析數據、生成報告）。
2. **Skills 結構與 SKILL.md**：
   * 一個標準的 Skill 資料夾必須包含一個 `SKILL.md` 檔案，頂部使用 **YAML Frontmatter** 定義技能名稱（name）與描述（description），後續寫入詳細的操作指令。
3. **全域與專案技能的優先順序**：
   * **全域技能**：加載於所有專案中。
   * **專案技能**：僅在當前專案目錄生效。避免過多的全域技能，以防關鍵字衝突或佔用不必要的 Token。
4. **自動化執行與 Turbo Mode**：
   * 在執行 Skills 時，啟用 AntiGravity 的 **Turbo Mode**，能讓 AI 自動同意輔助腳本的運行，達成無干擾的自動化工作流。

## ⏱️ 附時間戳記的段落大綱
* `[00:00]` 課程引言：為什麼要將雲端的 Gems 升級為本地的 Skills，兩者能力差在哪？
* `[02:01]` Skills 技能目錄的實體結構與核心檔案（SKILL.md）配置。
* `[04:01]` 知識的系統化輸出：如何在 Markdown 中撰寫結構化的 Prompt 行為約束。
* `[06:02]` 實戰演示：建立一個「Word 審題報告生成助手」技能。
* `[08:01]` 探討雲端硬碟備份：如何將本地的 Skills 自動同步備份至 Google Drive。
* `[10:00]` 技能加載機制：Agent 如何掃描資料夾並解析 YAML Frontmatter。
* `[12:00]` 為了避免彈出確認框，啟用 Turbo Mode 進行無感授權。
* `[14:01]` 實測「審題報告」技能，AI 讀取學生答案 Word 並自動產出修正意見。
* `[16:00]` 專案目錄與全域目錄（Global vs Project-Scoped）技能隔離設定。
* `[18:01]` 驚人的生成速度：實測不到一分鐘便完成整份報告的分析與導出。

## 🌐 中英專有名詞對照表
* **Gemini Gems**：Gemini 網頁版角色設定 (提示詞包)
* **AntiGravity Skills**：AntiGravity 本機可執行技能包
* **YAML Frontmatter**：YAML 格式的前置中繼資料
* **Supporting Scripts**：輔助執行腳本
* **Turbo Mode**：免點擊自動授權模式

## 🏃‍♂️ 行動指南
* 將您最常用的一個 Gemini Gem 角色提示詞，改寫為符合 `SKILL.md` 規範的 Markdown 文件，並放入專案的 `skills/` 目錄中進行測試。
* 思考：相較於單純的提示詞（Gems），Skills 結合「輔助腳本」後能解決哪些 Gems 無法處理的實體任務？
