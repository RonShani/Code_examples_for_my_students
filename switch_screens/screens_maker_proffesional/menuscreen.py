# -*- coding: utf-8 -*-
import random

from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window

from floatlayoutwithbackground import FloatLayoutWithBackground
from transitions import *


class MenuScreen(Screen):

    def __init__(self, screen_manager, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        self.screen_manager = screen_manager
        self.blay = FloatLayoutWithBackground()
        self.blay.add_widget(Button(text ='Goto questions',size_hint=(0.2,0.1), pos=(Window.size[0]*0.2,0), on_press = self.gotoquestions))
        self.blay.add_widget(Button(text='Quit', pos=(0,0), size_hint=(0.2,0.1), on_press = self.getout))
        self.add_widget(self.blay)

    def gotoquestions(self, instance):
        self.screen_manager.transition = give_me_random_transition()
        self.screen_manager.current = 'question_screen_1'

    def getout(self, instance):
        exit(1)
