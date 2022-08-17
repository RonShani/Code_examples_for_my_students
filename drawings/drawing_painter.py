from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ListProperty, NumericProperty
from kivy.graphics import *
from random import random


class MyWidget(Widget):
    wtd = NumericProperty(1)
    penrad = NumericProperty(10)
    pencolor = ListProperty([1, 0, 0, 1])  # Red

    def newclr(self, instance):
        print("Before Change@newclr: pencolor=", self.pencolor)
#        self.pencolor = instance.background_color
        self.pencolor = ([random(), random(), random(), 1])
        print("After Change@newclr: pencolor=", self.pencolor)

    def on_touch_move(self, touch):
        print("on_touch_move: touch=", touch)
        print("on_touch_move: pencolor=", self.pencolor)
        with self.canvas:
            Color(rgba=self.pencolor)
            if self.wtd == 1:
                Ellipse(pos=(touch.x, touch.y), size=(self.penrad, self.penrad))


class TestApp(App):
    title = "Kivy - Change Pen Colour"

    def build(self):
        return MyWidget()


if __name__ == "__main__":
    TestApp().run()