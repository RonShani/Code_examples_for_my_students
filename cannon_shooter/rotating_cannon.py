from kivy.core.window import Window
from kivy.graphics import Rectangle, Rotate, PopMatrix, PushMatrix
from kivy.uix.image import Image
from kivy.uix.widget import Widget
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
    target=[0,0]

    def __init__(self, center_pos=(Window.size[0]/2,Window.size[1]/2),cannon_starting_angle = 0, shooting_angle=0, radius = 0, **kwargs):
        super(Cannon,self).__init__(**kwargs)
        self.txtr = Image(source="cannon.png").texture
        with self.canvas:
            self.r=Rectangle(texture=self.txtr,pos_hint={'center_x': self.cx, 'center_y': self.cy}, pos=center_pos)
        if radius == 0:
            self.radius=self.r.size[1]/2
        else:
            self.radius = radius
        self.cx = self.r.pos[0] + (self.r.size[0]/2)
        self.cy = self.r.pos[1] + (self.r.size[1] / 2)
        self.starting_angle = 90-shooting_angle+cannon_starting_angle
        self.angle=-cannon_starting_angle
        with self.canvas.before:
            PushMatrix()
            self.rotation = Rotate(angle=self.angle, origin=(self.cx,self.cy))
        with self.canvas.after:
            PopMatrix()
        self.update_c_end()
        Window.bind(on_key_down=self.key_r)



    def update_c_end(self):
        self.angle = math.radians(self.starting_angle+self.rotation.angle)
        self.px = self.cx+(self.radius*math.cos(self.angle))
        self.py = self.cy+(self.radius*math.sin(self.angle))
        self.target=[self.cx+((self.radius+5)*math.cos(self.angle)),self.cy+((self.radius+5)*math.sin(self.angle))]

    def key_r(self, *args):
        if time.time() - self.last_shot_time > 0.1:
            if args[1]==275:
                self.rotation.angle -= 1
                self.update_c_end()
            elif args[1]==276:
                self.rotation.angle += 1
                self.update_c_end()