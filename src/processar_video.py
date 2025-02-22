import subprocess
import random
import string
import re

def gerar_nome_arquivo():
    """
    Gera um nome de arquivo aleatório curto para o vídeo de saída.
    """
    sufixo = ''.join(random.choices(string.digits + 'abcdef', k=6))
    return f"output_video_{sufixo}.mp4"

def detectar_area_ativa(input_video):
    """
    Aplica corte, redimensiona o vídeo e insere um banner centralizado.
    """
    try:
        result = subprocess.run(
            ["ffmpeg", "-i", input_video, "-vf", "cropdetect=24:16:0", "-t", "5", "-f", "null", "-"],
            stderr=subprocess.PIPE, text=True
        )
        
        crop_matches = re.findall(r'crop=\d+:\d+:\d+:\d+', result.stderr)
        return crop_matches[-1] if crop_matches else None
    except Exception as e:
        print(f"Erro ao detectar a área ativa do vídeo: {e}")
        return None

def video_com_banner(input_video, banner_image, output_video):
    crop_values = detectar_area_ativa(input_video)
    
    if not crop_values:
        print("Não foi possível detectar a área ativa do vídeo.")
        return
    
    print(f"Valores de corte detectados: {crop_values}")
    
    filter_complex = (
        f"[0:v]{crop_values}[video_cortado]; "
        f"[video_cortado]scale='min(1080,iw*1.5)':'min(1920,ih*1.5)'[video_ampliado]; "
        f"[1][video_ampliado]overlay=(W-w)/2:(H-h)/2[out]"
    )
    
    try:
        subprocess.run(
            ["ffmpeg", "-i", input_video, "-i", banner_image, "-filter_complex", filter_complex,
             "-map", "[out]", "-map", "0:a", "-c:v", "libx264", "-crf", "23", "-preset", "veryfast", "-c:a", "copy", output_video],
            check=True
        )
        print(f"Processo concluído. Vídeo com áudio salvo em: {output_video}")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao processar o vídeo: {e}")

def video_com_bordas_desfocadas(video_entrada, video_saida):
    """
    Aplica corte, redimensiona o vídeo e adiciona bordas desfocadas.
    """
    recorte = detectar_area_ativa(video_entrada)
    if not recorte:
        print("Não foi possível detectar a área ativa do vídeo.")
        return
    
    comando = [
        "ffmpeg", "-i", video_entrada, "-filter_complex",
        f"[0:v]{recorte},scale=1080:1920,boxblur=10[blurred]; \
        [0:v]{recorte},scale='min(1080,iw*1.5)':'min(1920,ih*1.5)'[focused]; \
        [blurred][focused]overlay=(main_w-overlay_w)/2:(main_h-overlay_h)/2[out]",
        "-map", "[out]", "-map", "0:a", "-c:v", "libx264", "-crf", "23", "-preset", "veryfast", "-c:a", "copy",
        video_saida
    ]
    subprocess.run(comando, check=True)
    print(f"Processo concluído. Vídeo salvo em: {video_saida}")

