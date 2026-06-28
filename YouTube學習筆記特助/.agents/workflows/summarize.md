# 工作流：/summarize YouTube 影片一鍵摘要

當使用者輸入 `/summarize` 時，請執行以下步驟：

1. 檢查 `input/url.txt` 是否存在並填有連結。
2. 執行指令下載影片元數據與字幕：
   ```powershell
   python scripts/download_transcript.py
   ```
3. 讀取 `input/metadata.json` 與下載下來的字幕檔（`.vtt` 或 `.srt` 等檔案，請尋找 `input/` 下最合適的字幕檔讀取）。
4. 解析字幕檔的內容，提煉出核心重點，並為各重點配上對應的影片時間戳記 `[mm:ss]`。
5. 根據影片的靈魂觀念，呼叫生圖工具產生 1-2 張精美插圖（生圖提示語寫成『產生一張圖：<描述>』），存為 `output/images/concept.png`。
6. 生成最終筆記 `output/YouTube_學習筆記.md`，並在適當位置嵌入插圖 `![概念插圖](images/concept.png)`。
7. 向使用者報告已生成，並附上檔案路徑。
