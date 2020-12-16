"""
Transformada de Fourier Discreta
"""

import os
import numpy as np
from matplotlib import pyplot as plt
from scipy.io.wavfile import write as write_wav
from scipy.fft import fft, fftfreq
from scipy.fft import rfft, rfftfreq, irfft

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SAMPLE_RATE = 44100  # Hertz
DURATION = 5  # Seconds


def generate_sine_wave(freq, sample_rate=SAMPLE_RATE, duration=DURATION):
    """Genera una onda senoidal con frecuencia freq
    con una cantidad de muestras = sample_rate * duration"""
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    frequencies = x * freq
    # Sin(wt), w = 2pi*f
    y = np.sin((2 * np.pi) * frequencies)
    return x, y


# Generar una onda senoidal con frecuencia freq en hz que dura Duration en s
x, y = generate_sine_wave(2)
plt.plot(x, y)
plt.show()


# Mezclando las señales de audio, superponiendolas
_, nice_tone = generate_sine_wave(400, SAMPLE_RATE, DURATION)
_, noise_tone = generate_sine_wave(4000, SAMPLE_RATE, DURATION)
noise_tone = noise_tone * 0.3  # atenuar 30%
mixed_tone = nice_tone + noise_tone
normalized_tone = np.int16((mixed_tone / mixed_tone.max()) * 32767)
plt.plot(normalized_tone[:1000])
plt.show()

# Guardando las muestras generadas en un archivo de audio
wav_path = os.path.join(BASE_DIR, 'signals_mixed.wav')
write_wav(wav_path, SAMPLE_RATE, normalized_tone)


# Usando FFT
# Number of samples in normalized_tone
N = SAMPLE_RATE * DURATION
yf = fft(normalized_tone)
xf = fftfreq(N, 1 / SAMPLE_RATE)
plt.plot(xf, np.abs(yf))
plt.xlabel('Frecuencia')
plt.title('Resultado FFT, reflejo en y=0')
print('FFT con reflejo en y=0')
plt.show()


# Volviendo la FFT mas rapida calculado solo la mitad positiva
# Note the extra 'r' at the front
yf = rfft(normalized_tone)
xf = rfftfreq(N, 1 / SAMPLE_RATE)
plt.plot(xf, np.abs(yf))
plt.xlabel('Frecuencia')
plt.title('Calculado solo la mitad positiva')
print('FFT más rápida calculado solo la mitad positiva con rfft() ')
plt.show()

# Filtrando la señal
# The maximum frequency is half the sample rate
points_per_freq = len(xf) / (SAMPLE_RATE / 2)
# Our target frequency is 4000 Hz
target_idx = int(points_per_freq * 4000)
yf[target_idx - 1:target_idx + 2] = 0
plt.plot(xf, np.abs(yf))
plt.xlabel('Frecuencia')
plt.title('Filtrado frecuencias de ruido')
plt.show()


# FFT Inversa
new_sig = irfft(yf)
plt.plot(new_sig[:1000])
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.title('Resultado de aplicar FFT inversa')
plt.show()


# Generando audio filtrado (limpio)
norm_new_sig = np.int16(new_sig * (32767 / new_sig.max()))
write_wav(
    os.path.join(BASE_DIR, 'signal_filtered.wav'),
    SAMPLE_RATE, norm_new_sig
)