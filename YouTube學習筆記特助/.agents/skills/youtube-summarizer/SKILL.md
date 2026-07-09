---
name: youtube-summarizer
description: 讀取一個或多個 YouTube 影片連結，下載影片資訊與字幕檔，進行深度摘要。
---

# youtube-summarizer

這個技能主要包含以下運作流程：
1. 讀取 `input/url.txt` 中填入的一個或多個 YouTube 影片/播放清單網址。
2. 呼叫 `scripts/download_transcript.py` 批次下載所有影片資訊與字幕。
3. 讀取 `input/` 下所有影片的中繼資料與對應字幕檔。
4. 解析字幕文字，提煉核心重點並附帶 `[mm:ss]` 時間戳記。
5. **生圖流程控制**：預設不生圖。若使用者有明確生圖要求，執行生圖前對話提問訪問（確認風格、比例與色彩），待使用者確認後再進行生圖。
6. **分組與 Obsidian 同步**：
   * 檢查是否有 `playlist_title` 播放清單屬性。
   * 自動建立「播放清單名稱」資料夾並對筆記分類。
   * 將最終筆記同時寫入專案根目錄的 `output/YouTube學習筆記特助/` 及 Obsidian 本地儲存庫的 **`YouTube學習筆記/`** 資料夾中。
