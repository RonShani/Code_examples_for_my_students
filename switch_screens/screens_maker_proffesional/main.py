# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from screen_widget import QuestionsScreen
from question_shuffler import QuestionShuffler
from menuscreen import MenuScreen

class QuizzApp(App):

    def build(self):
        # Create the screen manager
        screenmanager = ScreenManager()
        questioner = QuestionShuffler()
        menu_screen = MenuScreen(name='menu', screen_manager=screenmanager)
        quizz_first_screen = QuestionsScreen(name='question_screen_1', screen_index=1, screen_manager=screenmanager, questioner=questioner)
        screenmanager.add_widget(menu_screen)
        screenmanager.add_widget(quizz_first_screen)
        return screenmanager

if __name__ == '__main__':
    QuizzApp().run()