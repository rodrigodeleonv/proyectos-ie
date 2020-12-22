"""
pip install SpeechRecognition

Depencencias
pyaudio (microfono)

Idiomas soportados si se usa Google
https://cloud.google.com/speech-to-text/docs/languages
"""

import speech_recognition as sr

r = sr.Recognizer()

# Ingrese path de archivo de audio con voz
filepath = ''

harvard = sr.AudioFile(filepath)
with harvard as source:
    print('Ajustando ruido ambiental')
    r.adjust_for_ambient_noise(source)
    audio = r.record(source, offset=0, duration=4)

data = r.recognize_google(audio)
print(data)
