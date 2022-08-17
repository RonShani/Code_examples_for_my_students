from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.core.window import Window
from cabbage_shooter import Cabbage
from rotating_cannon import Cannon
import time

class LayoutsExmp(App):

    def build(self):
        self.layBig = FloatLayout()
        Window.bind(on_key_down=self.key_action)
        self.cannon = Cannon(center_pos=(250,250), cannon_starting_angle=90, shooting_angle=90, radius=40)
        self.layBig.add_widget(self.cannon)
        self.last_shot_time = time.time()
        return self.layBig

    def key_action(self, *args):
        if time.time()-self.last_shot_time > 0.2:
            self.layBig.add_widget(Cabbage(self.layBig, self.cannon.px, self.cannon.py, self.cannon.target[0], self.cannon.target[1], speed=5))
            self.last_shot_time = time.time()

if __name__ == '__main__':
    LayoutsExmp().run()
