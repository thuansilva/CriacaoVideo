import yt_dlp

def download_video_from_youtube(video_url: str, download_path: str = './downloads/video1.%(ext)s'):
    """
    Baixa um vídeo do YouTube, combinando o melhor vídeo e áudio em formato MP4.
    
    :param video_url: URL do vídeo do YouTube.
    :param download_path: Caminho onde o vídeo será salvo. O padrão é 'downloads/video1.%(ext)s'.
    """
    # Opções para o download
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Baixa o melhor vídeo e áudio separados e combina
        'merge_output_format': 'mp4',          # Combina o vídeo e áudio em MP4
        'outtmpl': download_path,              # Define o caminho e nome do arquivo
        'noplaylist': True,                    # Impede o download de playlists
        'postprocessors': [
            {
                'key': 'FFmpegVideoConvertor',  # Converte o vídeo para MP4 (se necessário)
                'preferedformat': 'mp4',       # Garantir que o formato final seja MP4
            },
            {
                'key': 'FFmpegMerger',         # Garante a combinação do áudio e vídeo
            },
        ],
    }

    # Realizar o download
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print("Download concluído com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro durante o download: {e}")
