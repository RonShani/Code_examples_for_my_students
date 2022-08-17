from kivy.core.window import Window
from kivy.graphics import Rectangle, Line, Ellipse, Color
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
import math


def center_to_bot_left(px,py):
    return (px-Window.size[0]/2,py-Window.size[1]/2)


class Rotation_XY(App):

    def __init__(self, r):
        super(Rotation_XY, self).__init__()
        self.x1=0
        self.y1=0
        self.x2=100
        self.y2=250
        self.middle = ((self.x1+self.x2)/2,(self.y1+self.y2)/2)
        self.angle = round(math.degrees(math.atan(self.y2/self.x2)))

    def build(self):
        self.lay = FloatLayout()
        self.lay.canvas.add(Line(points=[self.x1,self.y1,self.x2,self.y2], width=1))
        self.elps = Ellipse(angle_start=90-self.angle, angle_end=0, size=(200,200), pos=(-100,-100))
        self.lay.canvas.add(self.elps)

        self.lbl_zero = Label(text=str(self.x1)+" , "+str(self.y1), color=(1,0,0,1))
        self.lay.add_widget(self.lbl_zero,len(self.lay.children))
        self.lbl_zero.pos = center_to_bot_left(self.x1+20, self.y1+20)

        self.lbl_end = Label(text=str(self.x2)+" , "+str(self.y2), color=(1,0,0,1))
        self.lay.add_widget(self.lbl_end,len(self.lay.children))
        self.lbl_end.pos = center_to_bot_left(self.x2, self.y2)

        self.lbl_angle = Label(text=str(self.angle)+"\u00B0", color=(1,0,0,1))
        self.lay.add_widget(self.lbl_angle,len(self.lay.children))
        self.lbl_angle.pos = center_to_bot_left(self.middle[0]/2+70,self.middle[1]/2)

        print("x=cos "+str(self.x2))
        print("y=sin " + str(self.y2))
        print("? = "+str(self.angle))

        Window.bind(on_resize=self.redraw_after_resize)
        return self.lay

    def redraw_after_resize(self, window, width, height):
        self.lbl_angle.pos = center_to_bot_left(self.middle[0]/2+70,self.middle[1]/2)
        self.lbl_end.pos = center_to_bot_left(self.x2, self.y2)
        self.lbl_zero.pos = center_to_bot_left(self.x1+20, self.y1+20)

    def update_c_end(self):
        self.angle = math.radians(self.starting_angle + self.rotation.angle)
        self.px = self.cx + (self.radius * math.cos(self.angle))
        self.py = self.cy + (self.radius * math.sin(self.angle))
        self.target = [self.cx + ((self.radius + 5) * math.cos(self.angle)),self.cy + ((self.radius + 5) * math.sin(self.angle))]

if __name__ == "__main__":
    Rotation_XY(r=100).run()