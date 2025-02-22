from processar_video import video_com_banner,gerar_nome_arquivo


if __name__ == "__main__":
    input_video = "./downloads/v2.mp4"
    banner_image = "./banner/banner1.png"
    output_video = f"./video/reels_{gerar_nome_arquivo()}.mp4"

    video_com_banner(input_video, banner_image, output_video)
    # video_com_bordas_desfocadas(input_video, output_video)