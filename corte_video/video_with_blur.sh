!/bin/bash

# # Arquivo de entrada e banner
# INPUT_VIDEO="v1.mp4"
# BANNER_IMAGE="b.webp"
# OUTPUT_VIDEO="video_final_com_novo_banner.mp4"

# # Passo 1: Detectar a área ativa do vídeo
# CROP_VALUES=$(ffmpeg -i "$INPUT_VIDEO" -vf "cropdetect=24:16:0" -t 5 -f null - 2>&1 | grep -oP 'crop=\d+:\d+:\d+:\d+' | tail -1)

# # Verificar se os valores de corte foram encontrados
# if [ -z "$CROP_VALUES" ]; then
#   echo "Não foi possível detectar a área ativa do vídeo."
#   exit 1
# fi

# echo "Valores de corte detectados: $CROP_VALUES"

# # Passo 2: Aplicar o corte, redimensionar, centralizar no banner e manter o áudio
# ffmpeg -i "$INPUT_VIDEO" -i "$BANNER_IMAGE" -filter_complex "\
# [0:v]$CROP_VALUES[video_cortado]; \
# [video_cortado]scale='min(1080,iw*1.5)':'min(1920,ih*1.5)'[video_ampliado]; \
# [1][video_ampliado]overlay=(W-w)/2:(H-h)/2[out]" \
# -map "[out]" -map 0:a -c:v libx264 -crf 23 -preset veryfast -c:a copy "$OUTPUT_VIDEO"

# echo "Processo concluído. Vídeo com áudio salvo em: $OUTPUT_VIDEO"


# Arquivo de entrada e saída
INPUT_VIDEO="v2.mp4"
OUTPUT_VIDEO="output_with_blur_video_$(openssl rand -hex 3).mp4"

# Passo 1: Detectar a área ativa do vídeo
CROP_VALUES=$(ffmpeg -i "$INPUT_VIDEO" -vf "cropdetect=24:16:0" -t 5 -f null - 2>&1 | grep -oP 'crop=\d+:\d+:\d+:\d+' | tail -1)

# Verificar se os valores de corte foram encontrados
if [ -z "$CROP_VALUES" ]; then
  echo "Não foi possível detectar a área ativa do vídeo."
  exit 1
fi

echo "Valores de corte detectados: $CROP_VALUES"

# Passo 2: Aplicar o corte, redimensionar, criar as bordas desfocadas e manter o áudio
ffmpeg -i "$INPUT_VIDEO" -filter_complex "\
[0:v]$CROP_VALUES,scale=1080:1920,boxblur=10[blurred]; \
[0:v]$CROP_VALUES,scale='min(1080,iw*1.5)':'min(1920,ih*1.5)'[focused]; \
[blurred][focused]overlay=(W-w)/2:(H-h)/2[out]" \
-map "[out]" -map 0:a -c:v libx264 -crf 23 -preset veryfast -c:a copy "$OUTPUT_VIDEO"

echo "Processo concluído. Vídeo com bordas desfocadas salvo em: $OUTPUT_VIDEO"



