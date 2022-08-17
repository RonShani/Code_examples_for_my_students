# -*- coding: utf-8 -*-
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Rectangle, Color
from kivy.core.window import Window

class SpecialButton(Button):

    cat_index = 1
    cat_image = "cat_"
    cat_image_extension = ".png"

    def __init__(self, **kwargs):
        super(SpecialButton, self).__init__(**kwargs)
        self.size_hint = (0.25,0.175)
        self.pos_hint = ({'x': 0.45, 'y': 0.465})
        self.event1 = Clock.schedule_interval(self.run_cat, 0.05)

    def get_cat_image_name(self):
        img_name = self.cat_image + str(self.cat_index) + self.cat_image_extension
        self.cat_index += 1
        if self.cat_index > 13:
            self.cat_index = 1
        return img_name

    def run_cat(self, instance):
        self.background_normal = self.get_cat_image_name()


class WhiteScreenFloatLayout(FloatLayout):
    def __init__(self, **kwargs):
        super(WhiteScreenFloatLayout, self).__init__(**kwargs)
        self.canvas.add(Rectangle(size=Window.size, color=Color(1,1,1)))


class Main(App):
    def build(self):
        lay = WhiteScreenFloatLayout()
        btn = SpecialButton()
        lay.add_widget(btn)
        return lay

Main().run()

