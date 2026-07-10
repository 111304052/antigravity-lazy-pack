# 🎥 Python 零基礎新手入門 #09 Module (模組)

## 📌 影片資訊
* **播放清單序號**：EP09
* **影片 ID**：I-xm8wVqO1o
* **原始網址**：https://www.youtube.com/watch?v=I-xm8wVqO1o
* **播放清單**：Python 零基礎快速上手
* **講者**：PAPAYA 電腦教室

---

## 🧠 核心概念與技術摘要
1. **Module (模組) 概念**：
   * 模組是一個包含 Python 程式碼的 `.py` 檔案。可以透過 `import` 引入其他檔案中的函式與類別，達成模組化開發。
2. **引入語法 (Importing)**：
   * `import module_name`：引入整個模組，使用時需加前綴（如 `module_name.func()`）。
   * `from module_name import function_name`：只引入特定功能，可直接使用。
3. **內建模組與外部套件**：
   * 介紹 Python 內建的強大模組（如 `random`, `math`），以及使用 `pip install` 下載第三方擴充包的流程。

## ⏱️ 附時間戳記的段落大綱
* `[00:00]` 代碼重用性進階：Python 模組的原理與結構。
* `[02:30]` 本地自訂模組的建立與跨檔案 import 指引。
* `[05:10]` random 隨機模組的常用功能（randint、choice）實作。
* `[07:45]` 認識 Python 包管理工具 pip 的用途與第三方套件。

## 🌐 中英專有名詞對照表
* **Module**：模組
* **Import**：引入 / 導入
* **Built-in Module**：內建模組
* **PIP (Package Installer for Python)**：Python 套件管理工具

## 🏃‍♂️ 行動指南
* 建立一個 `math_tool.py`，寫入函式 `square(x)` 回傳 x 的平方；在另一個檔案中 `import math_tool` 並呼叫該函式。
