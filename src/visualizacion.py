import matplotlib.pyplot as plt
import numpy as np
import librosa
import os

FRAME_LEN = 512
HOP_LEN   = 128

def graficar_formas_onda(audios, clases, colores, output_path):
    SEG_MUESTRAS = int(2.0 * 22050)
    fig, axs = plt.subplots(len(clases), 1, figsize=(12, 10))
    fig.suptitle("Comparacion de formas de onda - Segmentos de 2s por clase", fontsize=13)
    for i, clase in enumerate(clases):
        y, sr = audios[clase]
        seg = y[:SEG_MUESTRAS]
        t   = np.linspace(0, 2.0, len(seg))
        axs[i].plot(t, seg, linewidth=0.5, color=colores[i])
        axs[i].set_title(clase.replace("_", " ").title())
        axs[i].set_ylabel("Amplitud")
        axs[i].set_ylim(-1.1, 1.1)
        axs[i].grid(True, alpha=0.3)
    axs[-1].set_xlabel("Tiempo (s)")
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.show()

def graficar_fft(audios, clases, colores, calcular_fft, output_path):
    fig, axs = plt.subplots(len(clases), 1, figsize=(12, 10))
    fig.suptitle("Analisis frecuencial - FFT por clase", fontsize=13)
    for i, clase in enumerate(clases):
        y, sr = audios[clase]
        freqs, mag = calcular_fft(y, sr)
        mascara    = freqs <= 8000
        pico_freq  = freqs[np.argmax(mag)]
        axs[i].plot(freqs[mascara], mag[mascara], linewidth=0.7, color=colores[i])
        axs[i].set_title(f"{clase.replace('_',' ').title()} | Frecuencia dominante = {pico_freq:.0f} Hz")
        axs[i].set_ylabel("Magnitud")
        axs[i].grid(True, alpha=0.3)
    axs[-1].set_xlabel("Frecuencia (Hz)")
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.show()
