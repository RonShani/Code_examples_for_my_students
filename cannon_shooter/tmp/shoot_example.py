import math
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Rectangle
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.clock import Clock
import time

class Cabbage(Widget):

    player_x=0
    player_y = 0
    enemy_x=0
    enemy_y = 0

    def __init__(self,lay, player_x, player_y, enemy_x, enemy_y, **kwargs):
        super(Cabbage, self).__init__(**kwargs)
        self.SPEED = 1
        self.lay=lay
        self.player_x = player_x
        self.player_y = player_y
        self.enemy_x = enemy_x
        self.enemy_y = enemy_y
        self.x_diff=self.enemy_x-self.player_x
        self.y_diff=self.enemy_y-self.player_y
        cbgt = Image(source="cabage.png").texture
        with self.canvas:
            self.moving_object = Rectangle(texture=cbgt, size=(25, 25),pos=(self.player_x, self.player_y))
        self.event = Clock.schedule_interval(self.moveit, 0.01)

    def moveit(self, inst):
        angle=math.atan2(self.y_diff,self.x_diff)
        change_x = math.cos(angle)*self.SPEED
        change_y = math.sin(angle)*self.SPEED
        self.player_x+=change_x
        self.player_y+=change_y
        if self.player_x > Window.size[0] or self.player_y > Window.size[1] or self.player_x < 0 or self.player_y < 0:
            Clock.unschedule(self.event)
            self.lay.remove_widget(self)
        self.moving_object.pos = (self.player_x, self.player_y)


class LayoutsExmp(App):

    last_shot_time = time.time()
    player=[Window.size[0]/2,Window.size[1]/2]
    enemy=[100,200]
    def build(self):
        self.layBig = FloatLayout()
        self.lbl = Button(text=str(self.enemy), size_hint=(0.12,0.08), pos=self.enemy)
        self.layBig.add_widget(self.lbl)
        Window.bind(on_key_down=self.key_action)
        return self.layBig

    def key_action(self, *args):
        if time.time()-self.last_shot_time > 0.2:
            self.layBig.add_widget(Cabbage(self.layBig, self.player[0],self.player[1], self.enemy[0], self.enemy[1]))
            self.last_shot_time = time.time()
        if args[1]==275:
            self.enemy[0]+=1
            self.lbl.pos=(self.enemy)
            self.lbl.text=str(self.enemy)
        elif args[1]==276:
            self.enemy[0]-=1
            self.lbl.pos = (self.enemy)
            self.lbl.text = str(self.enemy)


if __name__ == '__main__':
    LayoutsExmp().run()
