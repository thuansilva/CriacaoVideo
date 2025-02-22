import argparse
from processar_video import video_com_banner,gerar_nome_arquivo,video_com_bordas_desfocadas
from download_video import download_video_from_youtube

if __name__ == "__main__":
    # Passar URL
    parser = argparse.ArgumentParser(description="Comando para passar uma URL")
    parser.add_argument('--url', type=str, required=True, help="A URL a ser inserida no código")
    args = parser.parse_args()

    nome_arquivo = gerar_nome_arquivo()
    localDownload = f"./downloads/reels_{nome_arquivo}.mp4"
    video_url = args.url

    output_video = f"./video_final/reels_{nome_arquivo}.mp4"


    download_video_from_youtube(video_url,localDownload)
    video_com_banner(localDownload)
    # video_com_bordas_desfocadas(localDownload, output_video)