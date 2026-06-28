# -*- coding: utf-8 -*-
import os
import sys
import glob
import re

def clean_vtt(vtt_path, txt_path):
    if not os.path.exists(vtt_path):
        return False
        
    try:
        with open(vtt_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        cleaned_lines = []
        current_time = ""
        seen_texts = set()
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            # 偵測時間戳記
            time_match = re.match(r'(\d{2}:\d{2}:\d{2})\.\d{3} --> (\d{2}:\d{2}:\d{2})\.\d{3}', line)
            if time_match:
                start_time = time_match.group(1)
                # 去掉小時，只留 mm:ss
                parts = start_time.split(':')
                if parts[0] == '00':
                    current_time = f"[{parts[1]}:{parts[2]}]"
                else:
                    current_time = f"[{parts[0]}:{parts[1]}:{parts[2]}]"
                continue
                
            # 過濾 VTT 標頭與樣式
            if line.startswith('WEBVTT') or line.startswith('Kind:') or line.startswith('Language:'):
                continue
                
            # 過濾 HTML 標籤
            line_text = re.sub(r'<[^>]+>', '', line).strip()
            if not line_text:
                continue
                
            # 避免字幕重複行輸出
            if line_text in seen_texts:
                continue
            seen_texts.add(line_text)
            
            cleaned_lines.append(f"{current_time} {line_text}")
            
        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write("\n".join(cleaned_lines))
            
        return True
    except Exception as e:
        print(f"Error cleaning {vtt_path}: {e}")
        return False

if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        
    input_dir = r"c:\Users\leots\OneDrive\Desktop\Antigravity2.20260626\YouTube學習筆記特助\input"
    cleaned_dir = os.path.join(input_dir, "cleaned")
    os.makedirs(cleaned_dir, exist_ok=True)
    
    vtt_files = glob.glob(os.path.join(input_dir, "*.vtt"))
    print(f"Cleaning {len(vtt_files)} VTT files...")
    for vpath in vtt_files:
        filename = os.path.basename(vpath)
        name_part = os.path.splitext(filename)[0]
        txt_path = os.path.join(cleaned_dir, f"{name_part}.txt")
        if clean_vtt(vpath, txt_path):
            print(f"- Cleaned: {filename} -> cleaned/{name_part}.txt")
