#pyaudio wheel: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.clock import Clock
import speech_recognition as sr
class MoveBtn(App):

    def __init__(self):
        super(MoveBtn, self).__init__()
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening...")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try:
            print("recognizing...")
            text = r.recognize_google(audio)#, language="en-in")
            print(text)
            if text == "left":
                print("left")
                self.btn.pos = (self.btn.pos[0] - 5, self.btn.pos[1])
            elif text == "right":
                self.btn.pos = (self.btn.pos[0] + 5, self.btn.pos[1])
        except Exception as e:
            print("sorry sir i did not got that")
            print(e)

    def build(self):
        self.lay = FloatLayout()
        self.btn = Button(size_hint=(0.1,0.07), pos=(Window.size[0]/2,Window.size[1]/2), text="TALK!")
        self.lay.add_widget(self.btn)
        return self.lay

MoveBtn().run()