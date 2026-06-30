@echo off
chcp 65001 > nul
echo 正在偵測並自動匯入 Google 雲端硬碟的「天天記帳」新資料...
python "%~dp0accounting-app\import_data.py"
pause
