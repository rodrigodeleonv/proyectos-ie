"""
Grabar audio

pyaudio requiere dependencias del OS
sudo apt-get install -y python3-dev portaudio19-dev
"""

import os
import pyaudio
import wave

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
DURATION = 5

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(BASE_DIR, 'grabacion.wav')


audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
print('Inicial grabación....')
frames = list()
for i in range(0, int(RATE/CHUNK * DURATION)):
    data = stream.read(CHUNK)
    frames.append(data)
print(f'Grabacion finalizada. Archivo: {filename}')
stream.stop_stream()
stream.close()
audio.terminate()

# Casting: List a binary string. Preparando muestras para almacenar
data_bin = b''.join(frames)  # de lista a texto binario

# # Guardar de forma 1
# wav = wave.open(filename, 'wb')
# wav.setnchannels(CHANNELS)
# wav.setsampwidth(audio.get_sample_size(FORMAT))
# wav.setframerate(RATE)
# wav.writeframes(data_bin)
# wav.close()

# Guardar forma 2
with wave.open(filename, 'wb') as wav:
    wav.setnchannels(CHANNELS)
    wav.setsampwidth(audio.get_sample_size(FORMAT))
    wav.setframerate(RATE)
    wav.writeframes(data_bin)
