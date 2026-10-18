# Clasificación de Ruido Ambiental
Teoría de Señales - Sexto Semestre | Universidad de Manizales
Miguel Angel Santafé - Divinson José Cárdenas
Docente: Milady Cristina Guapacha

## Descripción
Sistema de análisis y clasificación de ruido urbano mediante procesamiento
digital de señales. Se trabaja con audios de sirenas, motores, disparos
y voces, aplicando análisis temporal y frecuencial sobre la base de datos
UrbanSound8K.

## Estado actual
- Carga de señales desde UrbanSound8K (8732 audios, 10 clases)
- Verificación del Teorema de Nyquist (Fs = 22050 Hz)
- Análisis temporal: RMS, ZCR y amplitud por clase
- Análisis frecuencial: FFT con scipy por clase
- Comparación señal original vs señal con ruido gaussiano (SNR = 10 dB)
- Pendiente: espectrogramas, filtros digitales, clasificador final

## Datos
Base de datos: UrbanSound8K
Fuente: https://urbansounddataset.weebly.com/urbansound8k.html
La dataset no esta en el repositorio por su tamaño (~6 GB).
Descargar desde el enlace y ubicar los folds en data/UrbanSound8K/

## Como ejecutar
pip install -r requirements.txt
Abrir notebooks/entrega2_frecuencial.ipynb en Google Colab.
Montar Google Drive y ajustar DATASET_PATH en la celda 3.

## Conceptos de Teoría de Señales aplicados
- Señal analógica x(t) a señal discreta x[n] por muestreo
- Teorema de Nyquist-Shannon: Fs >= 2 x Fmax
- Dominio del tiempo: energía RMS, tasa de cruces por cero, amplitud
- Dominio de la frecuencia: FFT con scipy.fft.rfft
- Ruido blanco gaussiano y relación señal-ruido SNR en dB

## Resultados

| Clase             | RMS media | ZCR media | Frecuencia dominante |
|-------------------|-----------|-----------|----------------------|
| siren             | 0.2038    | 0.1009    | 858 Hz               |
| engine_idling     | 0.3703    | 0.0248    | 26 Hz                |
| gun_shot          | 0.0548    | 0.0590    | 19 Hz                |
| children_playing  | 0.1461    | 0.1394    | 30 Hz                |

Ver graficas en results/graficas/

## Referencias
1. Salamon, J., Jacoby, C. y Bello, J. P. (2014). A dataset and taxonomy for urban sound research. ACM Multimedia, pp. 1041-1044.
2. Oppenheim, A. V. y Willsky, A. S. (1997). Signals and Systems. Pearson.
3. Proakis, J. G. y Manolakis, D. G. (2007). Digital Signal Processing. Pearson.
