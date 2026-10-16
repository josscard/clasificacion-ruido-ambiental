import librosa
import numpy as np
import os

TARGET_SR = 22050
DATASET_PATH = "/content/drive/MyDrive/Señales/UrbanSound8K"

def cargar_audio(filename, fold):
    ruta = os.path.join(DATASET_PATH, f"fold{fold}", filename)
    y, sr = librosa.load(ruta, sr=TARGET_SR, mono=True)
    y = y / (np.max(np.abs(y)) + 1e-9)
    return y, sr
