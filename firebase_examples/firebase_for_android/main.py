"""
an example for solving kivy screen freeze when authenticating google.auth on Android (threading problem)
"""
from kivy.uix.screenmanager import ScreenManager
from kivy.app import App
import scr_2
import scr_good

class LayoutsExmp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(scr_2.screen_1(name='log_scr', manager=sm))
        sm.add_widget(scr_good.screen_2(name='pass_ok', manager=sm))
        return sm

if __name__ == '__main__':
    LayoutsExmp().run()
