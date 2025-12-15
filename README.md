# Estimación de Pose Humana – Landmarks y Videos con Pose

Este directorio contiene los datos generados después de aplicar los modelos de estimación de pose a los videos del dataset procesado.

Debido a su tamaño, la carpeta se encuentra alojada en Google Drive:

 **Enlace a Carpeta de Estimación de Pose (Google Drive):**   https://drive.google.com/drive/folders/1kIbLHavsj7hghHZLfrhX9Xt2cykNQXBX?usp=sharing

---

## Contenido de Estimación de Pose

Incluye:
- Landmarks obtenidos con MediaPipe Pose:
  - Archivos en formato CSV.
  - Coordenadas normalizadas para cada fotograma.
- Videos con skeleton overlay.
- Archivos de preprocesamiento:
  - Corrección de contraste
  - Recortes de cada repetición
  - Aumento de iluminación
- Carpeta con videos recortados RAW → procesado.

---

## Código incluido en esta carpeta

Se adjunta el siguiente archivo desarrollado en Google Colab:

### **ESTIMACION POSE.ipynb**
Notebook en el cual se realiza:
- La carga de los videos preprocesados.
- La estimación de pose utilizando **MediaPipe Pose**.
- La generación de:
  - Landmarks por fotograma.
  - Videos con esqueleto dibujado.
  - CSV finales listos para análisis y modelado.

Este notebook corresponde al pipeline oficial utilizado para generar la base de datos procesada.

## Propósito

La carpeta de estimación de pose humana es la fuente principal para:
- El entrenamiento del modelo,
- El análisis biomecánico de posturas,
- La clasificación de ejercicios,
- La reconstrucción del movimiento mediante landmarks.


