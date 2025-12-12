
# Sistema de Visión Artificial para la Detección y Corrección de Posturas en Ejercicios Físicos

Este repositorio contiene la documentación, scripts y organización del dataset utilizado en el proyecto de visión artificial orientado a la corrección automática de posturas en ejercicios de entrenamiento de fuerza.

Debido al tamaño del dataset, los archivos de video no se alojan directamente en GitHub, sino en Google Drive. En cada carpeta correspondiente se incluye un enlace oficial de descarga.

---

##  Estructura del Repositorio

### **01-Dataset-RAW**
Contiene la información del dataset original:
- Videos sin preprocesar.
- Tomas frontal y lateral.
- 4 ejercicios: sentadilla, peso muerto, curl de bíceps y press de banca.
- Enlace de descarga desde Google Drive.

### **02-Dataset-Procesado**
Incluye los datos generados por los modelos de estimación de pose:
- Landmarks en formato CSV/JSON.
- Videos con skeleton overlay.
- Archivos preprocesados para entrenamiento.
- Enlace a la carpeta completa en Google Drive.

### **03-Preprocesamiento-Estimacion-Pose**
Código utilizado en:
- Preprocesamiento de videos.
- Estimación de pose (MediaPipe y/o OpenPose).
- Generación de Landmarks.
---

## Objetivo del Proyecto
Desarrollar un sistema basado en visión artificial que detecte posturas incorrectas en ejercicios de fuerza y proporcione retroalimentación automática para la prevención de lesiones y mejora del rendimiento.

---

## Acceso al Dataset Completo
Los enlaces están disponibles dentro de:

- `/01-Dataset-RAW/link_dataset_raw.txt`
- `/02-Dataset-Procesado/link_dataset_procesado.txt`

---

## Licencia
Este proyecto se distribuye únicamente con fines académicos.
