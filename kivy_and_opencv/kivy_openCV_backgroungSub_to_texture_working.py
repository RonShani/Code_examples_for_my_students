from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import numpy as np
import cv2

class CamApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.backSub = cv2.createBackgroundSubtractorMOG2()
    def build(self):
        self.img1=Image(size_hint=(1, 1))
        layout = FloatLayout()
        layout.add_widget(self.img1)
        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.update, 1.0/33.0)
        return layout

    def update(self, dt):
        ret, frame = self.capture.read()
        cv2.waitKey(10)
        fgMask = self.backSub.apply(frame)
        cv2.cvtColor(fgMask,cv2.COLOR_GRAY2BGR,frame)
        buf1 = cv2.flip(frame, 0)
        buf = buf1.tostring()
        texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        self.img1.texture = texture1
        print(self.img1.texture.width)

if __name__ == '__main__':
    CamApp().run()