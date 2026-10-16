import librosa
import numpy as np
import scipy.fft as fft

FRAME_LEN = 512
HOP_LEN   = 128

def calcular_rms(y):
    return librosa.feature.rms(y=y, frame_length=FRAME_LEN, hop_length=HOP_LEN)[0]

def calcular_zcr(y):
    return librosa.feature.zero_crossing_rate(y, frame_length=FRAME_LEN, hop_length=HOP_LEN)[0]

def calcular_fft(y, sr):
    N        = len(y)
    Y        = fft.rfft(y)
    freqs    = fft.rfftfreq(N, d=1/sr)
    magnitud = np.abs(Y) / N
    return freqs, magnitud

def caracterizar(y, sr, clase):
    rms = calcular_rms(y)
    zcr = calcular_zcr(y)
    return {
        "clase"      : clase,
        "duracion_s" : round(len(y) / sr, 3),
        "n_muestras" : len(y),
        "fs_Hz"      : sr,
        "min"        : round(float(np.min(y)), 4),
        "max"        : round(float(np.max(y)), 4),
        "amplitud"   : round(float(np.max(y) - np.min(y)), 4),
        "rms_media"  : round(float(np.mean(rms)), 4),
        "rms_std"    : round(float(np.std(rms)), 4),
        "zcr_media"  : round(float(np.mean(zcr)), 4),
    }
