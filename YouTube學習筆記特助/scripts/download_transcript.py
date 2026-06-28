# -*- coding: utf-8 -*-
import os
import sys
import json
import glob
import yt_dlp

def fetch_youtube_data(url, input_dir):
    os.makedirs(input_dir, exist_ok=True)
    
    # 設置 yt-dlp 選項，以影片 ID 做為檔名，避免多影片覆蓋
    ydl_opts = {
        'skip_download': True,
        'writeinfojson': True,
        'writesubtitles': True,
        'writeautomaticsub': True,
        'subtitleslangs': ['zh-Hant', 'zh-TW', 'zh', 'en'],
        'outtmpl': os.path.join(input_dir, '%(id)s'),
        'quiet': True,
        'no_warnings': True,
    }
    
    print(f"正在從 YouTube 擷取資訊：{url} ...")
    
    try:
        playlist_title = None
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # extract_info 並下載中繼資料與字幕
            info = ydl.extract_info(url, download=True)
            
            # 如果是播放清單中的影片，會含有 playlist_title
            playlist_title = info.get('playlist_title')
            video_id = info.get('id')
            
        if not video_id:
            print(f"[ERROR] 無法取得影片 ID：{url}")
            return False
            
        info_file = os.path.join(input_dir, f"{video_id}.info.json")
        if not os.path.exists(info_file):
            print(f"[ERROR] 無法取得影片 {video_id} 的 info.json")
            return False
            
        # 讀取並簡化資訊
        with open(info_file, 'r', encoding='utf-8') as f:
            meta = json.load(f)
            
        # 尋找對應的字幕檔案
        sub_files = glob.glob(os.path.join(input_dir, f"{video_id}.*.vtt"))
        subtitle_path = sub_files[0] if sub_files else None
        
        simplified_meta = {
            'id': video_id,
            'title': meta.get('title', '未知標題'),
            'uploader': meta.get('uploader', '未知上傳者'),
            'duration_string': meta.get('duration_string', '未知長度'),
            'webpage_url': meta.get('webpage_url', url),
            'playlist_title': playlist_title or meta.get('playlist'), # 取得播放清單名稱
            'subtitle_path': subtitle_path,
            'description': meta.get('description', '')[:500] + '...'
        }
        
        # 寫入特定影片的簡化中繼資料
        meta_out = os.path.join(input_dir, f"{video_id}_metadata.json")
        with open(meta_out, 'w', encoding='utf-8') as f:
            json.dump(simplified_meta, f, ensure_ascii=False, indent=2)
            
        print(f"[SUCCESS] 影片 {video_id} (播放清單: {playlist_title}) 下載完成！")
        return True
        
    except Exception as e:
        print(f"[ERROR] 執行失敗 {url}：{str(e)}")
        return False

if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        
    url_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "input", "url.txt"))
    input_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "input"))
    
    if not os.path.exists(url_file):
        os.makedirs(os.path.dirname(url_file), exist_ok=True)
        with open(url_file, 'w', encoding='utf-8') as f:
            f.write("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        print(f"[INFO] 已建立預設的 url.txt 範本。請寫入網址：{url_file}")
        sys.exit(0)
        
    # 讀取所有非空白行
    urls = []
    with open(url_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                urls.append(line)
                
    if not urls:
        print("[ERROR] url.txt 內容為空，請填入 YouTube 影片網址。")
        sys.exit(1)
        
    print(f"[INFO] 偵測到 {len(urls)} 個網址，開始批次下載...")
    success_count = 0
    for url in urls:
        if fetch_youtube_data(url, input_dir):
            success_count += 1
            
    print(f"\n[INFO] 批次處理完畢！成功：{success_count}/{len(urls)}")
