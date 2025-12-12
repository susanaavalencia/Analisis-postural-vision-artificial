
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

