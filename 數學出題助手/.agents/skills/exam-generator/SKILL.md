---
name: exam-generator
description: 數學出題助手技能，負責讀取課程標準並產生 Word 模擬考卷。
---

# exam-generator

這個技能負責自動化生成數學考卷：
1. 讀取 `input/` 下的課程標準檔案。
2. 執行 `scripts/generate_exam.py`。
3. 將排版好的 `.docx` 考卷儲存至專案根目錄的 `output/` 目錄。
