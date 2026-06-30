import os
import csv
import json
import glob

g_drive_dir = r"G:\我的雲端硬碟"
ledger_path = os.path.join(os.path.dirname(__file__), "data", "ledger.json")

print("==================================================")
print("  隨手記 (Money Flow) - 舊帳目自動增量導入工具")
print("==================================================")

# 1. Search for the latest '天天記帳' CSV file in Google Drive
search_pattern = os.path.join(g_drive_dir, "*天天記帳*.csv")
files = glob.glob(search_pattern)

if not files:
    print(f"❌ 錯誤：在 '{g_drive_dir}' 中找不到任何包含 '天天記帳' 的 CSV 檔案。")
    print("請確認您已將舊軟體導出的 CSV 檔案存入 Google 雲端硬碟中。")
    exit(1)

# Sort by modification time to get the newest file
files.sort(key=os.path.getmtime, reverse=True)
csv_path = files[0]
print(f"📂 偵測到最新的匯出檔案: {os.path.basename(csv_path)}")
print(f"🕒 檔案更新時間: {os.path.fromtimestamp(os.path.getmtime(csv_path)).strftime('%Y-%m-%d %H:%M:%S')}")

# 2. Load existing ledger.json
existing_data = {"transactions": [], "accounts": []}
if os.path.exists(ledger_path):
    try:
        with open(ledger_path, "r", encoding="utf-8") as f:
            existing_data = json.load(f)
        print("📖 已讀取目前的記帳資料庫。")
    except Exception as e:
        print(f"⚠️ 讀取現有資料庫失敗: {e}，將建立全新資料庫。")

existing_txs = existing_data.get("transactions", [])
existing_ids = {tx["id"] for tx in existing_txs}

# Category mapping table (including "美容美髮" -> "保養")
cat_mapping = {
    # 支出 (Expense)
    "飲食": "飲食",
    "日常用品": "日用品",
    "交通": "交通",
    "服飾": "服飾",
    "娛樂": "娛樂",
    "美容美髮": "保養",       # 依指示對應美容美髮為保養
    "醫療保健": "醫療",
    "學習深造": "學習",
    "教育": "學習",
    "打球": "運動",
    "水": "水電",
    "水電瓦斯": "水電",
    "洗烘": "日用品",
    "居家": "日用品",
    "交際應酬": "娛樂",
    "期末調整": "其他",
    # 收入 (Income)
    "工資": "薪資",
    "獎金": "獎金",
    "特殊開銷": "其他",
    "零用": "其他"
}

acct_mapping = {
    "現金": "cash",
    "銀行": "bank",
    "信用卡": "card"
}

migrated_count = 0
duplicate_count = 0

# 3. Read and parse CSV
try:
    with open(csv_path, "r", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        header = next(reader)
        
        for row in reader:
            if len(row) < 12:
                continue
            
            raw_date = row[0] # YYYYMMDD
            raw_cat = row[1]
            amount_str = row[3]
            member = row[5]
            raw_acct = row[6]
            tags_str = row[7]
            remarks = row[8]
            tx_type_raw = row[9] # 支 or 收
            uuid = row[11]
            
            # Skip if already exists in database
            if uuid in existing_ids:
                duplicate_count += 1
                continue
                
            # Parse Date YYYYMMDD -> YYYY-MM-DD
            if len(raw_date) == 8:
                formatted_date = f"{raw_date[0:4]}-{raw_date[4:6]}-{raw_date[6:8]}"
            else:
                formatted_date = raw_date
                
            # Parse Amount
            try:
                amount = float(amount_str)
            except ValueError:
                amount = 0.0
                
            # Parse Transaction Type
            tx_type = "expense"
            if tx_type_raw == "收":
                tx_type = "income"
                
            # Map Category
            category = cat_mapping.get(raw_cat, "其他")
            
            # Map Account ID
            account_id = acct_mapping.get(raw_acct, "cash")
            
            # Parse tags
            tags = [t.strip() for t in tags_str.split(",") if t.strip()] if tags_str else []
            
            new_tx = {
                "id": uuid,
                "date": formatted_date,
                "amount": amount,
                "type": tx_type,
                "category": category,
                "remarks": remarks,
                "tags": tags,
                "receipts": [],
                "accountId": account_id,
                "member": member if member else "自己"
            }
            
            existing_txs.append(new_tx)
            existing_ids.add(uuid)
            migrated_count += 1
            
except Exception as e:
    print(f"❌ 讀取與解析 CSV 失敗: {e}")
    exit(1)

# 4. Recalculate account balances dynamically based on all transactions
cash_balance = 0
bank_balance = 0
card_balance = 0

for tx in existing_txs:
    amt = float(tx.get("amount", 0))
    txtype = tx.get("type", "expense")
    
    if txtype == "expense":
        acct = tx.get("accountId")
        if acct == "cash": cash_balance -= amt;
        elif acct == "bank": bank_balance -= amt;
        elif acct == "card": card_balance -= amt;
    elif txtype == "income":
        acct = tx.get("accountId")
        if acct == "cash": cash_balance += amt;
        elif acct == "bank": bank_balance += amt;
        elif acct == "card": card_balance += amt;
    elif txtype == "transfer":
        from_acct = tx.get("fromAccountId")
        to_acct = tx.get("toAccountId")
        fee = float(tx.get("fee", 0))
        
        if from_acct == "cash": cash_balance -= (amt + fee)
        elif from_acct == "bank": bank_balance -= (amt + fee)
        elif from_acct == "card": card_balance -= (amt + fee)
        
        if to_acct == "cash": cash_balance += amt
        elif to_acct == "bank": bank_balance += amt
        elif to_acct == "card": card_balance += amt

# Update accounts list
existing_data["transactions"] = existing_txs
existing_data["accounts"] = [
    {"id": "cash", "name": "現金", "balance": cash_balance},
    {"id": "bank", "name": "銀行", "balance": bank_balance},
    {"id": "card", "name": "信用卡", "balance": card_balance}
]

# Write back to ledger.json
try:
    with open(ledger_path, "w", encoding="utf-8") as f:
        json.dump(existing_data, f, indent=2, ensure_ascii=False)
    print("--------------------------------------------------")
    print(f"🎉 導入順利完成！")
    print(f"➕ 新增導入交易：{migrated_count} 筆")
    print(f"⏭️ 忽略重複交易（已存在）：{duplicate_count} 筆")
    print("--------------------------------------------------")
    print("📊 帳戶餘額更新結果：")
    print(f"   💵 現金餘額: ${cash_balance:,.2f}")
    print(f"   🏦 銀行餘額: ${bank_balance:,.2f}")
    print(f"   💳 信用卡餘額: ${card_balance:,.2f}")
    print("==================================================")
except Exception as e:
    print(f"❌ 寫入資料庫失敗: {e}")
    exit(1)
