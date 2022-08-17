from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition, SlideTransition, CardTransition, FallOutTransition
from kivy.core.window import Window
from kivy.graphics import *


class MenuScreen(Screen):

    def __init__(self, parent, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        self.blay = FloatLayout()
        with self.blay.canvas:
            self.bak=Rectangle(texture=Image(source="starry_night.png").texture, size=Window.size)
        self.blay.add_widget(Button(text ='Goto settings',size_hint=(0.2,0.1), pos=(Window.size[0]*0.2,0), on_press = self.gotosettings))
        self.blay.add_widget(Button(text='Quit', pos=(0,0), size_hint=(0.2,0.1), on_press = self.getout))
        Window.bind(on_resize=self.redraw_after_resize)
        self.add_widget(self.blay)

    def gotosettings(self, instance):
        self.parent.transition = FallOutTransition()
        self.parent.current = 'settings'

    def getout(self, instance):
        exit(1)

    def redraw_after_resize(self, window, width, height):
        self.bak.size=Window.size


class SettingsScreen(Screen):

    def __init__(self, parent, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
        self.blay = FloatLayout()
        with self.blay.canvas:
            self.bak=Rectangle(texture=Image(source="intro.png").texture, size=Window.size)
        self.blay.add_widget(Button(text ='My settings button',size_hint=(0.2,0.1), pos=(Window.size[0]*0.2,0), on_press = self.gotomenu))
        self.blay.add_widget(Button(text='Back to menu', size_hint=(0.2,0.1), pos=(0,0)))
        Window.bind(on_resize=self.redraw_after_resize)
        self.add_widget(self.blay)

    def gotomenu(self, instance):
        self.parent.transition = CardTransition()
        self.parent.current = 'menu'

    def redraw_after_resize(self, window, width, height):
        self.bak.size=Window.size
class TestApp(App):

    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu', parent=sm))
        sm.add_widget(SettingsScreen(name='settings', parent=sm))
        return sm

if __name__ == '__main__':
    TestApp().run()