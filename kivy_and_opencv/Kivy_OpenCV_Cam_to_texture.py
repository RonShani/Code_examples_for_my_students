from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.graphics.texture import Texture

import cv2

class CamApp(App):

    def build(self):
        #create empty Image object
        self.img1=Image()
        #create Layout
        layout = FloatLayout()

        btn2 = Button(text="Also Btn", size_hint=(0.07,0.13), pos=(35,50))
        layout.add_widget(btn2)
        # lets create a button, just for fun
        self.btn = Button(text="OK", size_hint=(0.07,0.13), pos=(350,500))
        # and add it to the layout
        layout.add_widget(self.btn)
        #add the image to the layout [index=1 means the image will be behind the button (change it to 0 to understand)]
        layout.add_widget(self.img1, index=2)
        #open camera
        self.capture = cv2.VideoCapture(0)
        #tells the app to take a frame and update the background every 30 miliseconds
        Clock.schedule_interval(self.update, 0.030)
        return layout

    def update(self, dt):
        # get frame
        ret, frame = self.capture.read()
        # flip the frame (like mirror) because the texture turns it upside down
        buf1 = cv2.flip(frame, 0)
        # get the image bits data (take every pixel bits - r,g,b and convert to long string)
        # example: 101,64,85 ==> "e@U" (link to ascii table if you want to understand: https://www.asciitable.com/)
        buf = buf1.tostring()
        #create a texture object
        texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        # use the image string as texture
        texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        # display image from the texture
        self.img1.texture = texture1

if __name__ == '__main__':
    CamApp().run()
    cv2.destroyAllWindows()