from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from smo import SelfMovingObject
from scrolling_bakcground import Bak

class LayoutsExmp(App):

    def build(self):
        self.lay = FloatLayout()
        self.lay.add_widget(Bak())
        self.lay.on_touch_up = self.add_one
        self.lay.add_widget(SelfMovingObject(self.lay))
        return self.lay

    def add_one(self, instance):
        self.lay.add_widget(SelfMovingObject(self.lay))

if __name__ == '__main__':
    LayoutsExmp().run()