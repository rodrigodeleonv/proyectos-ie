"""
Basado en el ejemplo de clase
Solución LAB1
"""

import os
import numpy as np
from matplotlib import pyplot as plt
from scipy.io.wavfile import write as write_wav
from scipy.fft import fft, fftfreq
from scipy.fft import rfft, rfftfreq, irfft


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
audio_filename = os.path.join(BASE_DIR, 'SUCIA.wav')

FS = 44100  # Frecuencia de muestreo
DURATION = 3  # segundos

TONE = 440                 # Tono
NOISE = 3200               # Ruido
muestras_grafica = 1000    # Cantidad de muestras a graficar


def generate_sine_wave(freq, sample_rate=FS, duration=DURATION):
    """Genera una onda senoidal con frecuencia freq
    con una cantidad de muestras = sample_rate * duration"""
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    frequencies = x * freq
    # Sin(wt), w = 2pi*f
    y = np.sin((2 * np.pi) * frequencies)
    return x, y


# Generando tono deaseado
x, y = generate_sine_wave(TONE)
x_limited = x[:muestras_grafica]
y_limited = y[:muestras_grafica]
plt.plot(x_limited, y_limited)
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.title('Señal pura con frecuencia f')
plt.show()
# Tono Deseado
tone = y

# Generando ruido
_, noise1 = generate_sine_wave(NOISE, FS, DURATION)
mixed_tone = tone + noise1
normalized =  np.int16((mixed_tone / mixed_tone.max()) * 32767)
print('Generando audio con ruido')
write_wav(audio_filename, FS, normalized)
plt.plot(normalized[:muestras_grafica])
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.title('Señal Tono + Ruido')
plt.show()

# FFT
# Note the extra 'r' at the front
N = FS * DURATION
yf = rfft(normalized)
xf = rfftfreq(N, 1 / FS)
plt.plot(xf, np.abs(yf))
plt.xlabel('Frecuencia')
plt.title('Cuadrante positivo')
plt.show()

# Filtrando la señal
# The maximum frequency is half the sample rate
points_per_freq = len(xf) / (FS / 2)
print(f'points_per_freq {points_per_freq}')
# Our target frequency is noise freq in  Hz
target_idx = int(points_per_freq * NOISE)
yf[target_idx - 1:target_idx + 2] = 0
plt.plot(xf, np.abs(yf))
plt.xlabel('Frecuencia')
plt.title('Filtrado Ruido')
plt.show()

# FFT Inversa
new_sig = irfft(yf)
plt.plot(new_sig[:muestras_grafica])
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.title('Señal filtrada')
plt.show()

# Generando audio filtrado (limpio)
norm_new_sig = np.int16(new_sig * (32767 / new_sig.max()))
write_wav(
    os.path.join(BASE_DIR, 'LIMPIA.wav'),
    FS, norm_new_sig
)