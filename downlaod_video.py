import yt_dlp

# URL do vídeo do YouTube
video_url = 'https://www.youtube.com/watch?v=EPwSkTErC-M&ab_channel=FullCycle'

# Opções para o download
ydl_opts = {
    'format': 'bestvideo+bestaudio/best',  # Baixa o melhor vídeo e áudio separados e combina
    'merge_output_format': 'webm',          # Combina o vídeo e áudio em MP4
    'outtmpl': 'downloads/%(title)s.%(ext)s',  # Define o caminho e nome do arquivo
    'noplaylist': True,                    # Impede o download de playlists
    # 'postprocessors': [
    #     {
    #         'key': 'FFmpegExtractAudio',  # Extrai e converte o áudio
    #         'preferredcodec': 'aac',      # Converte o áudio para AAC (formato mais comum)
    #         'preferredquality': '192',    # Qualidade do áudio (192 kbps)
    #     },
    #     {
    #         'key': 'FFmpegVideoConvertor',  # Converte o vídeo para MP4 (se necessário)
    #     },
    # ],
}

# Realizar o download
try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
    print("Download concluído com sucesso!")
except Exception as e:
    print(f"Ocorreu um erro durante o download: {e}")
