# 🎥 AntiGravity 基本功 EP04：Gems 升級（自訂 Skill 與 Agent 工作流優勢對比）

## 📌 影片資訊
* **標題**：AntiGravity 基本功 EP04: 自訂 Gems 核心 Skill 與工作流定義...
* **講者/頻道**：三師爸Sense Bar
* **原始網址**：https://www.youtube.com/watch?v=kmmYXntln_E
* **播放清單**：AntiGravity_google_AI_Agents

## 🧠 核心概念與技術摘要
1. **傳統 Gems 網頁版限制**：
   * 傳統網頁版 Gems 只能做單純的對話與生圖，有 10 個知識檔案上傳限制，無法執行本地 Python 腳本、無法控制電腦檔案、無法進行批次工作流。
2. **Gems 升級為本地 Agent**：
   * 將 Gems 指令寫成 `SKILL.md` 與工作流定義。升級後，AI 成為具備本機執行權的 Agent，擁有 code execution（程式執行）、終端控制與無限制讀寫本地檔案的能力。
3. **生圖與工作流整合**：
   * 在工作流中，生圖不再只是對話展示，而是可以「將生好的圖片直接寫入 Word 檔中」或「自動掛載在 Web 網頁目錄中」。
4. **Imagen 生圖中文化測試**：
   * 實測 Imagen 引擎（在影片中被稱為 Nano Banana Pro）在 50 個中文字內的繁體字生成及多格漫畫風格，中文識別度高，但目前強制 1:1 的解析度。

## 🏃‍♂️ 行動指南
* 寫一份 `SKILL.md` 定義您的 Agent 大腦說明書。
* 撰寫 `AGENTS.md` 做為本機專案的全局入口守則。
* 測試生圖工作流，將產出的圖片用 Python 嵌入到考卷或教材文件中。
