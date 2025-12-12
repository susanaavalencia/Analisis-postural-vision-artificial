# Data Set Procesado 

En esta rama se adjunta el **data set procesado**, el cual incluye:

- Recortes individuales de cada repetición de los ejercicios  
- Conversión completa de los videos originales de formato **MOV → MP4**  
- Organización estandarizada para facilitar el preprocesamiento, extracción de pose y entrenamiento del modelo

Debido al tamaño del dataset, este se encuentra alojado en Google Drive:

 **Enlace al dataset procesado (recortes + MOV→MP4):**  
 (insertar aquí el enlace de Drive)

---


#  Conversión de videos: MOV → MP4

Muchos de los videos capturados desde dispositivos móviles vienen en formato **.MOV**, lo cual genera incompatibilidades con MediaPipe, OpenCV y otros pipelines de procesamiento.  
Por esta razón, se incluye un conjunto de scripts para realizar:

###  Conversión masiva de archivos `.MOV` a `.MP4`  
###  Normalización del códec (H.264) compatible con la mayoría de librerías  
###  Compresión   

Los scripts utilizan **FFmpeg**, herramienta estándar en procesamiento de video.

---

## Scripts incluidos

### **MOVaMP4.py**
Convierte un solo video MOV a MP4.



---

# Recorte de repeticiones de ejercicios

En esta rama también se incluyen los scripts para segmentar cada repetición de un ejercicio dentro de un video original continuo.  
Esto permite tener un dataset más ordenado y facilita el procesamiento frame-by-frame.

---

##  Scripts incluidos

### **RECORTES.pynb**
Convierte todos los videos de una carpeta de manera automática al establecer los puntos de recorte.

Ambos scripts permiten ajustar:
- resolución,
- bitrate,
- códec,
- directorio de salida.
