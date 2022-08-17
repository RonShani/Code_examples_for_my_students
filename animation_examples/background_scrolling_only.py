from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics import *
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window

class Bak(Widget):

    is_bak = True
    def __init__(self,**kwargs):
        super(Bak,self).__init__(**kwargs)
        txtr = Image(source='../imgs/stars.jpg').texture
        with self.canvas:
            Bak.bkgrnd = Rectangle(texture=txtr, pos=self.pos, size=(Window.size[0],Window.size[1]))
            Bak.bkgrnd2 = Rectangle(texture=txtr, pos=(Window.size[0],self.pos[1]), size=(Window.size[0], Window.size[1]))

    def update(self):
        Bak.bkgrnd.pos = (Bak.bkgrnd.pos[0]-10, 0)
        Bak.bkgrnd2.pos = (Bak.bkgrnd2.pos[0] - 10, 0)
        if Bak.bkgrnd.pos[0]*(-1) >= Window.size[0]:
            Bak.bkgrnd.pos = (Window.size[0], 0)
        if Bak.bkgrnd2.pos[0]*(-1) >= Window.size[0]:
            Bak.bkgrnd2.pos = (Window.size[0], 0)
    Clock.schedule_interval(update,0.025)

class ScrollApp(App):
    def build(self):
        lay = FloatLayout()
        lay.add_widget(Bak())
        return lay


if __name__=='__main__':
    ScrollApp().run()