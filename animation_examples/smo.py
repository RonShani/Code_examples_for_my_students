from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.clock import Clock
import random

class SelfMovingObject(Widget):

    is_bak = False
    up = random.randint(0,1)
    left = random.randint(0, 1)
    screen_height = Window.size[1]
    screen_width = Window.size[0]
    obj_h = screen_height / 16
    obj_w = screen_width / 12

    def __init__(self, parent_lay, **kwargs):
        super(SelfMovingObject, self).__init__(**kwargs)
        self.parent_lay = parent_lay
        Window.bind(on_resize=self.on_window_resize)
        self.xpos = random.SystemRandom().randint(0, self.screen_width)
        self.ypos = random.SystemRandom().randint(0, self.screen_height)
        self.rgb=(random.SystemRandom().random(),random.SystemRandom().random(),random.SystemRandom().random())
        with self.canvas:
            self.btn = Button(text="BOX", pos=(self.xpos, self.ypos), size=(self.obj_w,self.obj_h), background_color=self.rgb)
        self.event1 = Clock.schedule_interval(self.moveit1, 0.01)


    def on_window_resize(self, window, width, height):
        self.screen_height = Window.size[1]
        self.screen_width = Window.size[0]
        self.obj_h = self.screen_height / 16
        self.obj_w = self.screen_width / 12

    def moveit1(self, inst):
        for i in self.parent_lay.children:
            if i.is_bak == True:
                continue
            elif i.btn.pos == self.btn.pos:
                continue
            elif self.btn.collide_widget(i.btn):
                if self.left == 1:
                    self.left = 0
                elif self.left == 0:
                    self.left = 1
                if self.up == 1:
                    self.up = 0
                elif self.up == 0:
                    self.up = 1
        if self.up == 1:
            self.ypos += 1
            if self.ypos > self.screen_height - self.obj_h:
                self.up = 0
        elif self.up == 0:
            self.ypos -= 1
            if self.ypos < 0:
                self.up = 1
        if self.left == 1:
            self.xpos += 1
            if self.xpos > self.screen_width - self.obj_w:
                self.left = 0
        elif self.left == 0:
            self.xpos -= 1
            if self.xpos < 0:
                self.left = 1
        self.btn.pos=(self.xpos, self.ypos)