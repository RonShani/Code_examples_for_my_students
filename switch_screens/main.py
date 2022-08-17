from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition, SlideTransition, CardTransition, FallOutTransition

""""
    NoTransition - switches screens instantly with no animation
    SlideTransition - slide the screen in/out, from any direction
    CardTransition - new screen slides on the previous or the old one slides off the new one depending on the mode
    SwapTransition - implementation of the iOS swap transition
    FadeTransition - shader to fade the screen in/out
    WipeTransition - shader to wipe the screens from right to left
    FallOutTransition - shader where the old screen ‘falls’ and becomes transparent, revealing the new one behind it.
    RiseInTransition - shader where the new screen rises from the screen centre while fading from transparent to opaque.
"""
class MyFloatLayout(FloatLayout):
    def __init__(self,what_image, **kwargs):
        super(MyFloatLayout, self).__init__(**kwargs)
        with self.canvas:
            Image(source=what_image, size=Window.size)

class screen_1(Screen):
    def __init__(self,manager, **kwargs):
        super(screen_1, self).__init__(**kwargs)
        self.layBig = FloatLayout()
        img = Image(source="../imgs/cat.jpg")
        self.layBig.add_widget(img)
        self.btn = Button(text="switch",size_hint=(0.15,0.07), pos=(300, 300), on_press=self.switch_screen)
        self.layBig.add_widget(self.btn)
        self.add_widget(self.layBig)

    def switch_screen(self, instance):
        self.manager.transition = CardTransition()
        self.manager.current = 'scr2'

class screen_2(Screen):
    def __init__(self,manager, **kwargs):
        super(screen_2, self).__init__(**kwargs)
        self.layBig = MyFloatLayout(what_image="../imgs/cat2.jpg")
        self.btn = Button(text="switch",size_hint=(0.15,0.07), pos=(300, 300), on_press=self.switch_screen)
        self.layBig.add_widget(self.btn)
        self.add_widget(self.layBig)
    def switch_screen(self, instance):
        self.manager.transition = WipeTransition()
        self.manager.current = 'scr3'

class screen_3(Screen):
    def __init__(self,manager, **kwargs):
        super(screen_3, self).__init__(**kwargs)
        self.layBig = FloatLayout()
        img = Image(source="../imgs/starry_night.png")
        self.layBig.add_widget(img)
        self.btn = Button(text="switch",size_hint=(0.15,0.07), pos=(300, 300), on_press=self.switch_screen)
        self.layBig.add_widget(self.btn)
        self.add_widget(self.layBig)

    def switch_screen(self, instance):
        self.manager.transition = CardTransition()
        self.manager.current = 'scr1'

class LayoutsExmp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(screen_1(name='scr1', manager=sm))
        sm.add_widget(screen_2(name='scr2', manager=sm))
        sm.add_widget(screen_3(name='scr3', manager=sm))
        return  sm

if __name__ == '__main__':
    LayoutsExmp().run()