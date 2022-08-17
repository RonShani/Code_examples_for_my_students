from kivy.uix.floatlayout import FloatLayout
from kivy.app import App

class LayoutsExmp(App):

    def build(self):
        layBig = FloatLayout()
        return layBig


if __name__ == '__main__':
    LayoutsExmp().run()
