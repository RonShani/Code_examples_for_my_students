from kivy.uix.screenmanager import ScreenManager
from kivy.app import App
import guler_signin

class Haguse(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(guler_signin.screen_1(name='home_scr', manager=sm))
        return sm

if __name__ == '__main__':
    Haguse().run()