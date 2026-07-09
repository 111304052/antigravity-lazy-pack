# 🎥 claude基本功EP11:把 GPT-Image 2.0 裝進 Claude_讓 Claude 擁有最強生圖引擎

## 📌 影片資訊
* **播放清單序號**：EP11
* **影片 ID**：JqoZH5__gsk
* **原始網址**：https://www.youtube.com/watch?v=JqoZH5__gsk
* **播放清單**：Claude code基本功
* **講者**：三叔Sense Bar

---

## 🧠 核心概念與技術摘要
1. **生圖引擎集成**：
   * 傳統 Claude 雖然文字推理極強，但缺乏直接生成圖片的內置能力。
2. **GPT-Image 2.0 技能包**：
   * 藉由撰寫一個 Custom Skill，讓 Claude 可以透過呼叫外部繪圖 API（如 DALL-E 3 或 Midjourney/Flux API）或本地生圖腳本，實現在對話中「直接說、直接生圖」的功能，為簡報和網頁增色。

## ⏱️ 附時間戳記的段落大綱
* `[00:00]` 課程引言：打破 Claude 不能畫圖的限制，裝入最強生圖引擎。
* `[02:15]` 繪圖 API 的獲取與本地 Python 繪圖腳本編寫。
* `[05:00]` 在 Claude 中設定 GPT-Image 技能包 Frontmatter。
* `[08:10]` 現場實測：輸入「生成一張科幻教室的背景圖」，Claude 自動產出圖片。

## 🌐 中英專有名詞對照表
* **Image Generation Engine**：生圖引擎 / 影像生成引擎
* **DALL-E 3 / Flux**：主流影像生成模型
* **Custom Drawing Skill**：自訂生圖技能

## 🏃‍♂️ 行動指南
* 設定您的影像生成 API 金鑰，並請 Claude 測試在您的本地 outputs/ 目錄下自動生成一個 PNG 圖檔。
