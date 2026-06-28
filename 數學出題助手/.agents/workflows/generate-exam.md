# 工作流：一鍵生成考卷

當使用者輸入 `/generate-exam` 時，請執行以下步驟：

1. 檢查 `input/` 是否有新的課程參考檔案。
2. 執行指令：
   ```powershell
   python scripts/generate_exam.py
   ```
3. 確認 `output/` 目錄已生成 `數學模擬考卷_一元一次方程式.docx`。
4. 提供產出檔案的完整路徑給使用者。
