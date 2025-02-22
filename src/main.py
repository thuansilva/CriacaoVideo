from processar_video import video_com_banner,gerar_nome_arquivo,video_com_bordas_desfocadas
from download_video import download_video_from_youtube

if __name__ == "__main__":
    nome_arquivo = gerar_nome_arquivo()
    localDownload = f"./downloads/reels_{nome_arquivo}.mp4"
    video_url = 'https://www.youtube.com/shorts/51K1vMMB-tg'

    output_video = f"./video_final/reels_{nome_arquivo}.mp4"


    download_video_from_youtube(video_url,localDownload)
    video_com_banner(localDownload)
    # video_com_bordas_desfocadas(localDownload, output_video)