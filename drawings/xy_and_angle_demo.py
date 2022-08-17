# -*- coding: utf-8 -*-
from kivy.core.window import Window
from kivy.graphics import Rectangle, Line, Ellipse, Color
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.text import LabelBase
LabelBase.register(name="Varela", fn_regular="VarelaRound-Regular.ttf")
import math

heb_inst="יש לכם כאן הדגמה שמראה לכם\nאיך למצוא נקודה מסויימת ואת הזוית של הוקטור שלה\nזה יעזור לכל מי שמתעסק במיקום של אובייקטים על המסך והזזה שלהם במשחקים\nהשתמשו בחיצים כדי להזיז את הנקודה"
heb_rvrs="\nהשתמשו בחיצים כדי להזיז את הנקודה"+"\nזה יעזור לכל מי שמתעסק במיקום של אובייקטים על המסך והזזה שלהם במשחקים"+"\nאיך למצוא נקודה מסויימת ואת הזוית של הוקטור שלה"+"\nיש לכם כאן הדגמה שמראה לכם"

class Bar_x(Widget):
    def __init__(self, h, width=10):
        super(Bar_x,self).__init__()
        with self.canvas:
            Color(1,0,0,1)
            Line(points=[0,h,width,h],width=1)
            Line(points=[width/2, h, width/2, h+5], width=1)

class Bar_y(Widget):
    def __init__(self, h, w):
        super(Bar_y,self).__init__()
        with self.canvas:
            Color(0,1,0,1)
            Line(points=[w,0,w,h],width=1)
            Line(points=[w, h/2, w+5, h/2], width=1)

class Rotation_XY(Widget):

    def __init__(self, x1=0, y1=0, x2=100, y2=100, angle_radius=100):
        super(Rotation_XY, self).__init__()
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        self.angle_radius = angle_radius
        self.middle = ((self.x1+self.x2)/2,(self.y1+self.y2)/2)
        self.angle = round(math.degrees(math.atan(self.y2/self.x2)),2)

        with self.canvas:
            Line(points=[self.x1,self.y1,self.x2,self.y2], width=1)
            Ellipse(angle_start=90-self.angle, angle_end=0, size=(self.angle_radius,self.angle_radius), pos=(-self.angle_radius/2,-self.angle_radius/2))
            self.lbl_zero = Label(text=str(self.x1)+" , "+str(self.y1), color=(1,0,0,1), size=(40,13))
            self.lbl_end = Label(text="("+str(self.x2) + "," + str(self.y2)+")", color=(1, 0, 0, 1), size=(40,13))
            self.lbl_angle = Label(text="tan\u0398 = y/x\natan(y/x) = \u0398\natan("+str(self.y2)+"/"+str(self.x2)+") = \u0398\n\u0398 = "+str(self.angle) + "\u00B0", color=(1, 0, 0, 1), size=(40,13))
            self.lbl_x = Label(text="x="+str(self.x2)+"\nx=cos\u0398\u2022C", color=(1,0,0,1), size=(40,13))
            self.bar_x = Bar_x(h=self.y2, width=self.x2)
            self.lbl_y = Label(text="y="+str(self.y2)+"\ny=sin\u0398\u2022C", color=(0,1,0,1), size=(40,13))
            self.bar_y = Bar_y(h=self.y2, w=self.x2)#Image(source="y-bar.png")
            self.lbl_c = Label(text="C=\u221A(x\u00B2+y\u00B2)\nC="+str(round(math.sqrt(self.y2**2+self.x2**2),2)), size=(40,13))
            self.lbl_instructions = Label(font_name="Varela",base_direction="weak_rtl",text=heb_rvrs[::-1])

        self.redraw_after_resize(Window,Window.size[0],Window.size[1])
        Window.bind(on_resize=self.redraw_after_resize)

    def redraw_after_resize(self, window, width, height):
        self.lbl_angle.pos = ((self.angle_radius+self.x2)/2,self.middle[1]/2)
        self.lbl_end.pos = (self.x2+15, self.y2+5)
        self.lbl_zero.pos = (self.x1, self.y1)
        self.lbl_x.pos = (self.x2/2-23,self.y2+17)
        self.bar_x.pos = (0,self.y2)
        self.lbl_y.pos = (self.x2+17,self.y2/2-3)
        self.bar_y.pos = (self.x2-40,0)
        self.bar_x.size = (self.x2,self.size[1])
        self.lbl_c.pos = (self.middle[0]-self.middle[0]/2,self.middle[1])
        self.lbl_instructions.pos=(window.size[0]-320,window.size[1]-100)

    def update_c_end(self):
        self.angle = math.radians(self.starting_angle + self.rotation.angle)
        self.px = self.cx + (self.radius * math.cos(self.angle))
        self.py = self.cy + (self.radius * math.sin(self.angle))
        self.target = [self.cx + ((self.radius + 5) * math.cos(self.angle)),self.cy + ((self.radius + 5) * math.sin(self.angle))]


class MainApp(App):
    def build(self):
        self.x = 400
        self.y = 400
        self.lay = FloatLayout()
        self.rtt = Rotation_XY(x2=self.x, y2=self.y)
        self.lay.add_widget(self.rtt)
        Window.bind(on_key_down=self.on_key_press)
        return self.lay

    def on_key_press(self, *args):
        if args[1]==275:
            self.x+=1
            self.lay.remove_widget(self.rtt)
            self.rtt = Rotation_XY(x2=self.x, y2=self.y)
            self.lay.add_widget(self.rtt)
        elif args[1]==276:
            self.x-=1
            self.lay.remove_widget(self.rtt)
            self.rtt = Rotation_XY(x2=self.x, y2=self.y)
            self.lay.add_widget(self.rtt)
        elif args[1]==274:
            self.y-=1
            self.lay.remove_widget(self.rtt)
            self.rtt = Rotation_XY(x2=self.x, y2=self.y)
            self.lay.add_widget(self.rtt)
        elif args[1]==273:
            self.y+=1
            self.lay.remove_widget(self.rtt)
            self.rtt = Rotation_XY(x2=self.x, y2=self.y)
            self.lay.add_widget(self.rtt)


if __name__ == "__main__":
    MainApp().run()