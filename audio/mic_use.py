#pyaudio wheel: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    # read the audio data from the default microphone
    print("Recognizing...")
    audio_data = r.listen(source, timeout=1, phrase_time_limit=1)#, duration=5)
    # convert speech to text
    text = r.recognize_google(audio_data)
    print(text)