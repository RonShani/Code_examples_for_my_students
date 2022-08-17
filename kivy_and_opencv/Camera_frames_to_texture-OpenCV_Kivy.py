from kivy.support import install_twisted_reactor
install_twisted_reactor()
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import cv2

class CamApp(App):

    def build(self):
        self.img1=Image(size_hint=(1, 1))
        layout = FloatLayout()
        layout.add_widget(self.img1)
        self.btn = Button(text="Click", size_hint=(0.1,0.1), on_press=self.sendTest, pos=(100,150))
        layout.add_widget(self.btn)
        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.update, 1.0/33.0)
        return layout

    def update(self, dt):
        ret, frame = self.capture.read()
        cv2.waitKey(10)
        buf1 = cv2.flip(frame, 0)
        buf = buf1.tostring()
        texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        self.img1.texture = texture1

    def sendTest(self, dt):
        print("try")

if __name__ == '__main__':
    CamApp().run()