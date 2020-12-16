"""
Ejemplo de Audio

Reproducir sonido generado a partir de una Onda Senoidal.
No se guardan las muestras.

simpleaudio requiere dependencias de OS
sudo apt-get install -y python3-dev libasound2-dev
"""

import numpy as np
import simpleaudio as sa

frequency = 440  # Our played note will be 440 Hz
fs = 44100  # 44100 samples per second
seconds = 3  # Note duration of 3 seconds

# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
t = np.linspace(0, seconds, seconds * fs, False)

# Generate a 440 Hz sine wave: Sin(2*pi*ft)
note = np.sin(2 * np.pi * frequency * t)

# Ensure that highest value is in 16-bit range
audio = note * (2**15 - 1) / np.max(np.abs(note))
# Convert to 16-bit data
audio = audio.astype(np.int16)

# Start playback
print('Reproduciendo...')
play_obj = sa.play_buffer(audio, 1, 2, fs)
print('Bloqueando')
# Wait for playback to finish before exiting
play_obj.wait_done()
print('Fin')
