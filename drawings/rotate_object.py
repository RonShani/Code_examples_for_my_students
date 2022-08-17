from kivy.core.window import Window
from kivy.graphics import Rectangle, Rotate, PopMatrix, PushMatrix
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App

the_middle_of_the_screen = (Window.size[0]/2, Window.size[1]/2)

#this is a image class i create so i can rotate it
class RotatedImage(Image):
    def __init__(self):
        super(RotatedImage, self).__init__()
        self.color=(0,0,0,1) #just a black color for background
        with self.canvas:
            img = Image(source="patric.png", pos=the_middle_of_the_screen) #this is the image to rotate
        #here is the important lines:
        with self.canvas.before:
            PushMatrix() #befor rotation you must apply PushMatrix - to be able to rotate
            self.rotation = Rotate(angle=60, origin=the_middle_of_the_screen) #angle:angle of rotation. origin:the center of rotation (axis)
        with self.canvas.after:
            PopMatrix() #after rotation - PopMatrix

class Rotate_example(App):
    def build(self):
        lay = FloatLayout()
        img = RotatedImage()
        lay.add_widget(img)
        return lay

if __name__ == "__main__":
    Rotate_example().run()