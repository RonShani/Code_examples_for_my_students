from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.app import App

class LayoutsExmp(App):

    def build(self):
        layBig = FloatLayout()
        btn1 = Button(text="Hello World!", background_normal="../imgs/btnBlue.png", background_down="../imgs/btnRed.png", size_hint=(0.40,0.50))
        layBig.add_widget(btn1)
        return layBig


if __name__ == '__main__':
    LayoutsExmp().run()
