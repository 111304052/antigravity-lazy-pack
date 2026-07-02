# 🎥 YouTube 學習筆記：Google AntiGravity 2.0 實測評價

## 📌 影片基本資訊
* **影片標題**：AntiGravity 基本功 EP01:Claude Code 與 Codex 的強敵？Google AntiGravity 2.0 實測評價
* **講者/頻道**：三師爸Sense Bar
* **影片長度**：35 分 42 秒
* **原始連結**：[點我前往 YouTube 觀看影片](https://www.youtube.com/watch?v=LyiiMVZE7uM)
* **影片播放清單**：無 (獨立影片)

---

## ⏱️ 時間戳記大綱
* **`[00:00]` 介紹與開場**：開箱並介紹 GitHub 上發布的「AntiGravity 專屬懶人包（antigravity-lazy-pack）」。
* **`[01:26]` 安裝與設定**：展示如何在 Windows 上安裝並登入授權全新的 AntiGravity 2.0。
* **`[02:04]` 介面比較與市場定位**：將 AntiGravity 2.0 的介面與 Claude Code、Codex、OpenCode 進行橫向對比，指出 AI Agent 工人 (Harness) 的未來趨勢。
* **`[03:20]` 模型選擇與安全審核設定**：介紹模型選項（Gemini 3.5 Flash/Medium、Sonnet 4.6），並說明為防工作流中斷，建議開啟「Always Proceed」（自動核准）。
* **`[09:10]` MCP 服務連接測試**：
  * `[09:40]` NotebookLM 筆記本資料擷取。
  * `[10:08]` 本地 Obsidian 知識庫（Vault）讀寫。
  * `[11:15]` Firebase 專案資訊連結。
* **`[15:00]` 內建生圖功能實測**：使用中文提示詞生成「貓在鋼琴上昏倒」漫畫風格圖，評估其風格一致性與尺寸限制（目前限 1:1）。
* **`[21:15]` Web 實作與 Firestore 連線**：實作一個結合 Firebase Firestore 的文字雲 Web App。實測部署第一次失敗，經 Agent 自動修復後第二次成功。
* **`[24:00]` 四大 AI Agent 時代分析與終極評價**：分析四大 Agent 的優缺點，並給予 AntiGravity 2.0 基礎分 60 分的客觀評價。

---

## 🧠 核心知識深度摘要

### 1. 四大 AI Agent 時代的格局 ⚔️
目前市面上的 AI 開發特助已形成「四雄鼎立」的局面，功能介面極為相似，皆著重於自動化執行本機指令與讀寫檔案：
* **Claude Code**：Anthropic 推出，在程式邏輯推理上表現極佳（搭配 Sonnet 3.7/4.6 等模型）。
* **Codex**：OpenAI 生態系主力，整合度高。
* **OpenCode**：開源社群的主力，最大優點是可接任何自訂模型。
* **AntiGravity 2.0**：Google 官方推出，深度整合 Google 生態系（如 Firebase, NotebookLM），並具備原生生圖能力。

### 2. MCP (Model Context Protocol) 運作核心 🔌
影片展示了 AI Agent 不需要開啟瀏覽器，就能直接操作第三方軟體的秘密──**MCP 協定**：
* **NotebookLM MCP**：能讓 AI 直接查詢您雲端的讀書筆記，進行知識提煉。
* **Obsidian MCP (`mcpvault`)**：能讀寫本地的 Markdown 筆記，做到自動更新工作日誌（專案駕駛艙）。
* **Firebase MCP**：可自動存取後端資料庫，進行 Web App 部署。

### 3. 自動化核准 (Always Proceed) 的必要性 ⚠️
在執行複雜工作流時，如果沒有在「設定 (Settings)」中開啟對應的自動核准（如 `Always Proceed`），AI 在跑程式或寫檔時會**一直跳出「確認」提示**。這會造成：
* 工作流中斷，人類必須手動點擊。
* 失去「放著讓 AI 自己跑完」的自動化優勢。
* *註：影片中也發現目前 2.0 仍有設定後偶爾失效的 Bug。*

### 4. 實測評價：基本功 60 分，未來可期 📈
* **優點**：速度極快（受惠於 Gemini 3.5 Flash），生圖和 MCP 串接非常順暢，是 Google 生態系使用者的神兵利器。
* **缺點**：生圖比例暫時受限，且在撰寫程式碼時有時會出現低級 Bug（例如第一次寫的網頁會報錯），需要二次 Debug 才能成功。

---

## 🌐 中英專有名詞對照表
* **Agent Harness**：Agent 載具 / 執行作業環境
* **MCP (Model Context Protocol)**：模型上下文協定
* **Timestamp**：時間戳記
* **Always Proceed**：自動核准 / 一律繼續
* **Firestore**：雲端 NoSQL 資料庫 (Firebase 服務)
* **Word Cloud**：文字雲

---

## 🏃‍♂️ 行動指南 (Action Items)
1. **完成 MCP 配置**：依影片說明安裝並設定 NotebookLM 及 Obsidian 的本地 MCP 連線，釋放雙手。
2. **啟用自動核准**：在 AI 設定中，將 JavaScript 執行、瀏覽器控制與檔案修改權限設為 `Always Proceed`。
3. **建立工作流規則**：在專案根目錄放置 `ANTIGRAVITY.md`，將本機的「固定偏好」記錄下來。
