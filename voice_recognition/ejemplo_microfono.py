"""
pip install SpeechRecognition

Depencencias
pyaudio (microfono)

Idiomas soportados si se usa Google
https://cloud.google.com/speech-to-text/docs/languages
"""

import speech_recognition as sr

r = sr.Recognizer()


mic = sr.Microphone()

# sr.Microphone.list_microphone_names()

with mic as source:
    print('Ajustando ruido ambiental')
    r.adjust_for_ambient_noise(source)
    print('Grabando audio...')
    audio = r.listen(source)
    print('Audio grabado')

r.recognize_google(audio, language='es-GT')
