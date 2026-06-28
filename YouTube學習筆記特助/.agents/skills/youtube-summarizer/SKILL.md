---
name: youtube-summarizer
description: 讀取 YouTube 影片連結，並為其下載影片資訊與字幕檔，進行深度摘要。
---

# youtube-summarizer

這個技能主要包含以下運作流程：
1. 讀取 `input/url.txt` 取得 YouTube 影片網址。
2. 呼叫 `scripts/download_transcript.py` 下載影片資訊與字幕。
3. 讀取產出的 `input/metadata.json` 與字幕檔案（如 `input/video.zh-Hant.vtt` 等）。
4. 整理核心內容並生成排版精美的 Markdown 筆記。
5. 呼叫生圖工具生成 1-2 張示意圖存至 `output/images/`，並嵌入在筆記中。
6. 將最終筆記輸出至 `output/` 目錄。
