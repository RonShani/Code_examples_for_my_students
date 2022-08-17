from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.app import App

class LayoutsExmp(App):

    def build(self):
        self.layBig = FloatLayout(size=Window.size)
        self.get_all_scales()
        self.btn = Button(text="Dynamic Button", size_hint=(1/6,1/10), pos=self.button_position)
        self.layBig.add_widget(self.btn)
        Window.bind(on_resize=self.on_window_resize)
        return self.layBig

    def get_all_scales(self):
        print(Window.size)
        self.screen_height = Window.size[1]
        self.screen_width = Window.size[0]
        self.btn_width = self.screen_width/8
        self.btn_height = self.screen_height/12
        self.button_position = [(self.screen_width-self.btn_width)/2, (self.screen_height-self.btn_height)/2]

    def on_window_resize(self, window, width, height):
        self.get_all_scales()
        self.btn.pos = self.button_position

if __name__ == '__main__':
    LayoutsExmp().run()