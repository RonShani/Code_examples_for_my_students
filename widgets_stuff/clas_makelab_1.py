from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
import random
colors = ["red", "green", "blue"]


class MySpecialButton(Button):
    def __init__(self,my_text, **kwargs):
        super(MySpecialButton, self).__init__(**kwargs)
        self.text = my_text
        print(len(self.text))
        self.size_hint = (0.1, 0.07)
        Clock.schedule_interval(self.happens_sometimes,0.5)

    def happens_sometimes(self,z):
        self.background_color = random.choice(colors)

class MyApp(App):
    def build(self):
        lay = FloatLayout()
        btn = MySpecialButton(my_text="this is the text parameter")
        lay.add_widget(btn)
        return lay

MyApp().run()