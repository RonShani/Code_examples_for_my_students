#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import speech_recognition as sr
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.core.window import Window

# this is called from the background thread

class MoveBtn(App):

    def __init__(self):
        super(MoveBtn, self).__init__()
        r = sr.Recognizer()
        m = sr.Microphone()
        with m as source:
            r.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening

        # start listening in the background (note that we don't have to do this inside a `with` statement)
        r.listen_in_background(m, self.callback)

    def build(self):
        self.lay = FloatLayout()
        self.btn = Button(size_hint=(0.1, 0.07), pos=(Window.size[0] / 2, Window.size[1] / 2), text="TALK!")
        self.lay.add_widget(self.btn)
        return self.lay

    def callback(self, recognizer, audio):
        # received audio data, now we'll recognize it using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            text=recognizer.recognize_google(audio, language="he-IL")
            print(text)
            if "שמאלה" in text:
                print("שמאלה")
                self.btn.pos = (self.btn.pos[0] - 5, self.btn.pos[1])
            elif "ימינה" in text:
                self.btn.pos = (self.btn.pos[0] + 5, self.btn.pos[1])
            #print("Google Speech Recognition thinks you said " + recognizer.recognize_google(audio))
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))



# do some more unrelated things
#while True: time.sleep(0.1)  # we're not listening anymore, even though the background thread might still be running for a second or two while cleaning up and stopping

MoveBtn().run()