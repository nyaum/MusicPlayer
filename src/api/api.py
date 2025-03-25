from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import os
import uuid
import json
import chardet
import yt_dlp
import yt_dlp.options

app = Flask(__name__)
CORS(app)

# 다운로드 디렉토리 설정
DOWNLOAD_DIR = './downloads'

API_PLAYLIST = []

# 다운로드 디렉토리 생성
if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

@app.route('/download', methods=['POST'])
def download_video():
    data = request.json
    url = data.get('url')

    if not url:
        return jsonify({"error": "URL is required"}), 400

    filename = str(uuid.uuid4())
    filepath = os.path.join(DOWNLOAD_DIR, f'{filename}.%(ext)s')

    ydl_opts = {
        'writeinfojson': True,
        'skip_download': True,
        #'quiet': True,
        'default_search': 'ytsearch:' f'{url}',
        'outtmpl': filepath
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)

        # video_title = info.get('title', 'Unknown Title')
        # video_id = info.get('id', 'Unknown ID')

        # ydl.download([url])

        # json_info = json.dumps(ydl.sanitize_info(info))

        downloaded_filepath = os.path.join(DOWNLOAD_DIR, filename)
        metadata_filepath = downloaded_filepath + '.info.json'

        if os.path.exists(metadata_filepath):
            with open(metadata_filepath, 'r', encoding='utf-8') as f:
                metadata = json.load(f)
            
            # 특정 형식만 저장
            formats = metadata.get('formats', [])
            format_249 = next((f for f in formats if f.get('format_id') == '249'), None)
            
            if format_249:
                track_info = {
                    "track": metadata.get('title', 'Unknown Track'),
                    "artist": metadata.get('uploader', 'Unknown Artist'),
                    "album": metadata.get('album', 'Unknown Album'),
                    "albumCover": metadata.get('thumbnail', ''),
                    "audio": format_249["url"],
                }

                # 플레이리스트 서버에 저장
                API_PLAYLIST.append(info)
                
                return jsonify({"message": "Download successful", "playlist": track_info})
            else:
                return jsonify({"error": "Failed to find format 249"}), 500
        else:
            return jsonify({"error": "Metadata file not found"}), 500



    # try:
    #     # 임시 파일 이름 생성
    #     filename = str(uuid.uuid4())
    #     filepath = os.path.join(DOWNLOAD_DIR, f'{filename}.%(ext)s')

    #     # yt-dlp로 제목, 유튜브 링크 검색
    #     result = subprocess.run(
    #         ['yt-dlp',
    #          '--default-search',
    #          'ytsearch:', f'{url}', 
    #          '--get-title',
    #          '--get-id'],
    #         capture_output=True,
    #         text=True,
    #     )

    #     result = result.stdout.split('\n')

    #     title = result[0]
    #     url = f'https://www.youtube.com/watch?v={result[1]}'

    #     # yt-dlp 명령어 실행 (기본 검색 옵션 추가)
    #     result = subprocess.run(
    #         ['yt-dlp', 
    #          '--write-info-json',
    #          '--skip-download',
    #          '--flat-playlist',
    #          '--quiet',
    #          '--ignore-errors',
    #          #"--default-search", "ytsearch",
    #          #'-x', 
    #          #'-vU', 
    #          #'--audio-format', 'mp3', 
    #          url, '-o', filepath],
    #         capture_output=True,
    #         text=True,
    #         encoding='utf-8'
    #     )

    #     if result.returncode == 0:
    #         downloaded_filepath = os.path.join(DOWNLOAD_DIR, filename)
    #         metadata_filepath = downloaded_filepath + '.info.json'
    #         print(metadata_filepath)
    #         if os.path.exists(metadata_filepath):
    #             with open(metadata_filepath, 'r', encoding='utf-8') as f:
    #                 metadata = json.load(f)
                
    #             # 특정 형식만 저장
    #             formats = metadata.get('formats', [])
    #             format_249 = next((f for f in formats if f.get('format_id') == '249'), None)
                
    #             if format_249:
    #                 track_info = {
    #                     "track": metadata.get('title', 'Unknown Track'),
    #                     "artist": metadata.get('uploader', 'Unknown Artist'),
    #                     "album": metadata.get('album', 'Unknown Album'),
    #                     "albumCover": metadata.get('thumbnail', ''),
    #                     "audio": format_249["url"],
    #                 }

    #                 # 플레이리스트 서버에 저장
    #                 API_PLAYLIST.append(metadata_filepath)

    #                 print(API_PLAYLIST)
                    
    #                 return jsonify({"message": "Download successful", "playlist": track_info})
    #             else:
    #                 return jsonify({"error": "Failed to find format 249"}), 500
    #         else:
    #             return jsonify({"error": "Metadata file not found"}), 500

    #     else:
    #         return jsonify({"error": result.stderr}), 500
        
    # except FileNotFoundError:
    #     return jsonify({"error": "yt-dlp not found. Ensure it is installed and in the PATH."}), 500
    # except Exception as e:
    #     return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)