# -*- coding: utf-8 -*-
import os
import sys
import json
import yt_dlp

def fetch_youtube_data(url, input_dir):
    os.makedirs(input_dir, exist_ok=True)
    
    # 設置 yt-dlp 選項
    # 下載自動生成的繁體中文、繁體中文（台灣）、簡體中文或英文翻譯字幕
    ydl_opts = {
        'skip_download': True,
        'writeinfojson': True,
        'writesubtitles': True,
        'writeautomaticsub': True,
        'subtitleslangs': ['zh-Hant', 'zh-TW', 'zh', 'en'],
        'outtmpl': os.path.join(input_dir, 'video'),
        'quiet': True,
        'no_warnings': True,
    }
    
    print(f"正在從 YouTube 擷取資訊：{url} ...")
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        info_file = os.path.join(input_dir, 'video.info.json')
        if not os.path.exists(info_file):
            print("[ERROR] 無法取得影片中繼資料 (info.json 不存在)")
            return False
            
        # 讀取並簡化資訊
        with open(info_file, 'r', encoding='utf-8') as f:
            meta = json.load(f)
            
        simplified_meta = {
            'title': meta.get('title', '未知標題'),
            'uploader': meta.get('uploader', '未知上傳者'),
            'duration_string': meta.get('duration_string', '未知長度'),
            'webpage_url': meta.get('webpage_url', url),
            'description': meta.get('description', '')[:500] + '...' # 簡短描述
        }
        
        # 寫入簡化後的資訊，供 Agent 讀取
        with open(os.path.join(input_dir, 'metadata.json'), 'w', encoding='utf-8') as f:
            json.dump(simplified_meta, f, ensure_ascii=False, indent=2)
            
        print("[SUCCESS] 影片資訊與字幕下載完成！")
        return True
        
    except Exception as e:
        print(f"[ERROR] 執行失敗：{str(e)}")
        return False

if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        
    url_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "input", "url.txt"))
    input_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "input"))
    
    if not os.path.exists(url_file):
        # 建立預設範本
        os.makedirs(os.path.dirname(url_file), exist_ok=True)
        with open(url_file, 'w', encoding='utf-8') as f:
            f.write("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        print(f"[INFO] 已建立預設的 url.txt 範本。請將您想摘要的 YouTube 網址寫入：{url_file}")
        sys.exit(0)
        
    with open(url_file, 'r', encoding='utf-8') as f:
        url = f.read().strip()
        
    if not url:
        print("[ERROR] url.txt 內容為空，請填入 YouTube 影片網址。")
        sys.exit(1)
        
    fetch_youtube_data(url, input_dir)
