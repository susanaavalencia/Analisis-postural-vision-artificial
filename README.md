# Estimación de Pose Humana – Landmarks y Videos con Pose

Este directorio contiene los datos generados después de aplicar los modelos de estimación de pose a los videos del dataset procesado.

Debido a su tamaño, la carpeta se encuentra alojado en Google Drive:

 **Enlace a Carpeta de Estimación de Pose (Google Drive):**  
➡ (insertar enlace aquí)

---

## Contenido de Estimación de Pose

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
La carpeta de estimación de pose humana es la fuente principal para:
- el entrenamiento del modelo,
- el análisis biomecánico de posturas,
- la clasificación de ejercicios.

Cada archivo corresponde a su video RAW equivalente, variando en el número de repetición.
