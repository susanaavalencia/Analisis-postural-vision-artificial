

# #codigo para press de banca lateral
# import ffmpeg
# import os

# # ================================================
# # RUTAS
# # ================================================
# ruta_entrada = r"F:\Univalle\Semestre 9\TG1\VIDEOS\SEMANA 1\FLOR ANA MARIA\IMG_6271.MOV"
# #ruta_entrada = r"F:\Univalle\Semestre 9\TG1\VIDEOS\SEMANA 1\FLOR ANA MARIA\IMG_6254.MOV"
# ruta_salida  = r"F:\Univalle\Semestre 9\TG1\videos_convertidos\Ana maria\video2.mp4"



# probe = ffmpeg.probe(ruta_entrada)
# video_info = next(s for s in probe["streams"] if s["codec_type"] == "video")

# width = int(video_info["width"])
# height = int(video_info["height"])

# ratio = width / height
# print("ratio:", ratio)

# # --------------------------
# # HEURÍSTICA FIABLE
# # --------------------------
# # 1) ratio ~1.0 – 1.3 → vertical aunque el archivo se ve horizontal físicamente
# # 2) ratio > 1.3       → horizontal de verdad
# # --------------------------

# if ratio > 1.30:
#     rotar = True
# else:
#     rotar = False

# if rotar:
#     print("🔄 Rotando 90°")
# else:
#     print("⬆ Sin rotación")

# stream = ffmpeg.input(ruta_entrada)

# if rotar:
#     stream = stream.filter("transpose", 1)

# (
#     stream
#     .output(ruta_salida, vcodec="libx264", an=None)
#     .run(overwrite_output=True)
# )

#codigo para video verticales
import os
import ffmpeg

# ============================================
# CONFIGURAR CARPETA A PROCESAR
# ============================================
carpeta = r"F:\Univalle\Semestre 9\TG1\VIDEOS\SEMANA 1\OSSA MARIA PAULA\PRESS DE BANCA"

# ============================================
# RECORRER CARPETA
# ============================================
for archivo in os.listdir(carpeta):
    if archivo.lower().endswith(".mov"):

        ruta_entrada = os.path.join(carpeta, archivo)

        # Archivo de salida (mismo nombre, extensión mp4)
        nombre_salida = "1_" + os.path.splitext(archivo)[0] + ".mp4"
        ruta_salida = os.path.join(carpeta, nombre_salida)

        print(f" Comprimiendo: {archivo}  →  {nombre_salida}")

        try:
            (
                ffmpeg
                .input(ruta_entrada)
                .output(
                    ruta_salida,
                    vcodec="libx264",
                    crf=28,              # ≈50% reducción de tamaño
                    preset="veryfast",   # fluido y eficiente
                    pix_fmt="yuv420p",
                    movflags="+faststart",
                    an=None              #  eliminar audio
                )
                .run(overwrite_output=True)
            )

            print(f" Listo: {ruta_salida}\n")

        except Exception as e:
            print(f" Error procesando {archivo}: {e}\n")

print("Proceso completado.")

