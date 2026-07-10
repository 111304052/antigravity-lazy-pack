# 🎥 Python 零基礎新手入門 #08 Dictionaries (字典)

## 📌 影片資訊
* **播放清單序號**：EP08
* **影片 ID**：2uhs3TOmb64
* **原始網址**：https://www.youtube.com/watch?v=2uhs3TOmb64
* **播放清單**：Python 零基礎快速上手
* **講者**：PAPAYA 電腦教室

---

## 🧠 核心概念與技術摘要
1. **Dictionary (字典) 結構**：
   * 字典是一種無序的鍵值對（Key-Value pairs）集合型態，用大括號 `{}` 表示。
   * **Key (鍵)**：必須是唯一且不可變的型態（如字串、整數）。
   * **Value (值)**：可以是任意型態。
2. **字典操作**：
   * **讀取**：`dict[key]` 或用安全讀取 `dict.get(key, default)` 避免產生 KeyError。
   * **新增/修改**：`dict[key] = value`。
   * **刪除**：`del dict[key]`。

## ⏱️ 附時間戳記的段落大綱
* `[00:00]` 鍵值對（Key-Value）非序列資料結構解說。
* `[02:40]` 字典的宣告、修改與新增元素語法。
* `[05:15]` 字典安全讀取方法 dict.get() 的重要性。
* `[08:00]` 遍歷字典中的鍵與值（dict.items()）用法實測。

## 🌐 中英專有名詞對照表
* **Dictionary**：字典
* **Key-Value Pair**：鍵值對
* **Get Method**：Get 安全讀取方法
* **KeyError**：鍵值不存在報錯

## 🏃‍♂️ 行動指南
* 建立字典 `student = {"name": "Leo", "score": 90}`，使用 `get()` 獲取 `"name"`，並修改 `"score"` 為 95。
