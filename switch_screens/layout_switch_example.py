from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition, SlideTransition, CardTransition, FallOutTransition
from kivy.core.window import Window
from kivy.graphics import *
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
class FloatLayoutWithBackground(FloatLayout):
    def __init__(self, **kwargs):
        super(FloatLayoutWithBackground, self).__init__(**kwargs)
        with self.canvas:
            Color(.234, .456, .678, .8)

    def build(self):
        self = FloatLayout()
        return self

class MenuScreen(Screen):

    def __init__(self, parent, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        self.blay = FloatLayoutWithBackground()
        self.blay.add_widget(Button(text ='Goto settings',size_hint=(0.2,0.1), pos=(Window.size[0]*0.2,0), on_press = self.gotosettings))
        self.blay.add_widget(Button(text='Quit', pos=(0,0), size_hint=(0.2,0.1), on_press = self.getout))
        self.add_widget(self.blay)

    def gotosettings(self, instance):
        self.parent.transition = FallOutTransition()
        self.parent.current = 'settings'

    def getout(self, instance):
        exit(1)


class SettingsScreen(Screen):

    def __init__(self, parent, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
        self.blay = FloatLayoutWithBackground()
        self.blay.add_widget(Button(text ='My settings button',size_hint=(0.2,0.1), pos=(Window.size[0]*0.2,0), on_press = self.gotomenu))
        self.blay.add_widget(Button(text='Back to menu', size_hint=(0.2,0.1), pos=(0,0)))
        self.add_widget(self.blay)

    def gotomenu(self, instance):
        self.parent.transition = CardTransition()
        self.parent.current = 'menu'

class TestApp(App):

    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu', parent=sm))
        sm.add_widget(SettingsScreen(name='settings', parent=sm))
        return sm

if __name__ == '__main__':
    TestApp().run()