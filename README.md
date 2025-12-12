# Dataset Procesado – Landmarks y Videos con Pose

Este directorio contiene los datos generados después de aplicar los modelos de estimación de pose a los videos RAW.

Debido a su tamaño, el dataset se encuentra alojado en Google Drive:

 **Enlace al Dataset Procesado (Google Drive):**  
➡ (insertar enlace aquí)

---

## Contenido del Dataset Procesado

Incluye:
- Landmarks de MediaPipe:
  - Formato CSV.
  - Coordenadas normalizadas.
- Videos con skeleton overlay.
- Archivo de preprocesamiento:
  - Corrección de contraste
  - Recorte
  - Aumento de iluminación
- Carpeta de recortes de videos RAW → procesado.

---

##  Propósito
El dataset procesado es la fuente principal para:
- el entrenamiento del modelo,
- el análisis biomecánico de posturas,
- la clasificación de ejercicios.

Cada archivo corresponde a su video RAW equivalente, variando en el número de repetición.
