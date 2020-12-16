import os
import math
import numpy as np
from scipy.io import wavfile

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.path.join(BASE_DIR, 'audio1.wav')

FS = 41100  # Frecuencia de muestreo
DURACION = 1  # segundos

# Total de muestras =  FS * DURACION

# Generar muestras aletareas
# Parametros amplitud min, max y total de muestras
# data = np.random.uniform(0, 2**16, FS * DURACION)

data = list()
for i in range(FS * DURACION):
    # data.append(2**16 * math.cos(i * 481.0 * 2 * math.pi / FS) + 1024)
    data.append(1024 * math.cos(2 * math.pi * i * 1000 / FS))

# Escalando para ser compatible con .wav
# 2^16=65536 --> [-32768, 32767]
normalized = np.int16(data / np.max(np.abs(data)) * 32767)
wavfile.write(os.path.join(BASE_DIR, 'audio1.wav'), FS, normalized)
