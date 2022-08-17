from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout

class screen_2(Screen):

    def __init__(self, manager, **kwargs):
        super(screen_2, self).__init__(**kwargs)
        self.layBig = FloatLayout()
        self.btn = Button(text="GOOD", size_hint=(0.15, 0.07), pos_hint=({'x': 0.35, 'y': 0.80}), on_press=self.im_out)
        self.layBig.add_widget(self.btn)
        self.sm = manager
        self.add_widget(self.layBig)

    def im_out(self,ins):
        exit(1)
