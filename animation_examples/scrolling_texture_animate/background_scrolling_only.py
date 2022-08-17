from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics import *
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window

class Enemy_Snake(Widget):

    is_bak = True
    def __init__(self,**kwargs):
        super(Enemy_Snake,self).__init__(**kwargs)
        self.txtr_name = "Snake_walk_"
        self.txtr_index = 1
        txtr = Image(source='Snake_walk_1.png').texture
        with self.canvas:
            self.bkgrnd = Rectangle(texture=txtr, pos=self.pos, size=(Window.size[0]/6,Window.size[1]/6))
        Clock.schedule_interval(self.update, 0.12)

    def update(self,dt):
        tmpname=self.txtr_name+str(self.txtr_index)+".png"
        self.bkgrnd.texture = Image(source=tmpname).texture
        self.txtr_index += 1
        if self.txtr_index == 5:
            self.txtr_index = 1


class ScrollApp(App):
    def build(self):
        lay = FloatLayout()
        lay.add_widget(Enemy_Snake())
        return lay


if __name__=='__main__':
    ScrollApp().run()