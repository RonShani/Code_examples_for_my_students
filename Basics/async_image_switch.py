from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.utils import *
from kivy.uix.image import AsyncImage


class LayoutsExmp(App):

    images = ['https://www.goodnet.org/photos/620x0/28590_hd.jpg','https://www.goodnet.org/photos/620x0/28594_hd.jpg']
    image_index = 0

    def build(self):
        self.layBig = FloatLayout(size=(300, 300))
        self.img = AsyncImage(source=self.images[self.image_index])
        self.layBig.add_widget(self.img)
        self.btn3 = Button(text="change image",size_hint=(0.2, 0.1),
                           pos=(50, 50),
                           on_press=self.change_image)
        self.layBig.add_widget(self.btn3)
        return self.layBig

    def change_image(self, instance):
        if self.image_index == 0:
            self.image_index = 1
        else:
            self.image_index = 0
        self.img.source = self.images[self.image_index]
        self.img.reload()

if __name__ == '__main__':
    LayoutsExmp().run()
