# -*- coding: utf-8 -*-
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.clock import Clock


class SpecialButton(Button):

    def __init__(self, **kwargs):
        super(SpecialButton, self).__init__(**kwargs)
        self.original_text = "Click!"
        self.size_hint = (0.1,0.07)
        self.pos_hint = ({'x': 0.45, 'y': 0.465})
        self.background_color = "red"
        self.event1 = Clock.schedule_interval(self.scroll_text, 0.2)

    def scroll_text(self, instance):
        self.original_text = self.original_text[1:]+self.original_text[0]
        tmp_txt = list(self.original_text)
        self.text = " ".join(tmp_txt)


class Main(App):
    def build(self):
        lay = FloatLayout()
        btn = SpecialButton()
        lay.add_widget(btn)
        return lay

Main().run()

