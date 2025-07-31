import os
import yt_dlp
from tqdm import tqdm

def get_url():
    return input("Lien TikTok : ").strip()

def get_format():
    fmt = input("Format (mp3 / mp4) : ").strip().lower()
    if fmt not in ['mp3', 'mp4']:
        print("Format invalide.")
        return get_format()
    return fmt

def download_tiktok(url, output_format):
    output_dir = 'downloads'
    os.makedirs(output_dir, exist_ok=True)

    progress = {'pbar': None}

    def progress_hook(d):
        if d['status'] == 'downloading':
            if progress['pbar'] is None:
                total_bytes = d.get('total_bytes') or d.get('total_bytes_estimate')
                if total_bytes:
                    progress['pbar'] = tqdm(total=total_bytes, unit='B', unit_scale=True, desc="Téléchargement")
            if progress['pbar'] and d.get('downloaded_bytes'):
                progress['pbar'].n = d['downloaded_bytes']
                progress['pbar'].refresh()
        elif d['status'] == 'finished':
            if progress['pbar']:
                progress['pbar'].close()
                progress['pbar'] = None
            print("✔ Téléchargement terminé. Conversion en cours...")

    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'progress_hooks': [progress_hook],
        'format': 'bestaudio/best' if output_format == 'mp3' else 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'postprocessors': [],
    }

    if output_format == 'mp3':
        ydl_opts['postprocessors'].append({
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        })
    elif output_format == 'mp4':
        ydl_opts['postprocessors'].append({
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        })

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        print(f"[ERREUR] Téléchargement échoué : {str(e)}")

if __name__ == '__main__':
    url = get_url()
    fmt = get_format()
    download_tiktok(url, fmt)
