from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Rectangle, Rotate, PopMatrix, PushMatrix
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.button import Button
import time
import math

class Cannon(Widget):

    last_shot_time = time.time()
    angle=0
    radius=50
    cx = 150
    cy = 150
    px=0
    py=0
    def __init__(self,**kwargs):
        super(Cannon, self).__init__(**kwargs)
        self.txtr = Image(source="../cannon.png").texture
        with self.canvas:
            self.r=Rectangle(texture=self.txtr,pos_hint={'center_x': self.cx, 'center_y': self.cy}, pos=(100,100))
        with self.canvas.before:
            PushMatrix()
            self.rotation = Rotate(angle=self.angle, origin=(self.cx,self.cy))
        with self.canvas.after:
            PopMatrix()
        Window.bind(on_key_down=self.key_r)
        self.radius=self.r.size[1]/2
        self.cx=self.r.pos[0]+self.r.size[0]/2
        self.cy = self.r.pos[1] + self.r.size[1] / 2
        self.update_c_end()


    def update_c_end(self):
        self.angle = math.radians(90+self.rotation.angle)
        self.px = self.cx+(self.radius*math.cos(self.angle))
        self.py = self.cy+(self.radius*math.sin(self.angle))

    def key_r(self, *args):
        if time.time() - self.last_shot_time > 0.1:
            if args[1]==275:
                self.rotation.angle -= 1
                self.update_c_end()
            elif args[1]==276:
                self.rotation.angle += 1
                self.update_c_end()

class LayoutsExmp(App):

    last_shot_time = time.time()

    def build(self):
        self.layBig = FloatLayout()
        Window.bind(on_key_down=self.key_action)
        self.cannon = Cannon()
        self.layBig.add_widget(self.cannon)
        self.btn = Button(text=str(self.cannon.px)+','+str(self.cannon.py), size_hint=(0.05,0.05))
        self.layBig.add_widget(self.btn)
        self.a = Button(text=str(self.cannon.px)+','+str(self.cannon.py), size_hint=(0.05,0.05), pos=(400,400))
        self.layBig.add_widget(self.a)
        return self.layBig

    def key_action(self, *args):
        if time.time()-self.last_shot_time > 0.2:
            self.last_shot_time = time.time()
            self.btn.pos = (self.cannon.px, self.cannon.py)
            self.btn.text = str(self.cannon.px) + ',' + str(self.cannon.py)
            self.a.text=str(self.cannon.angle)+ ',' +str(self.cannon.rotation.angle)

if __name__ == '__main__':
    LayoutsExmp().run()
