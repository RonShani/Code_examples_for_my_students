from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
import random

def create_random_positioned_buttons(list_of_texts_for_buttons,x_btns,y_btns, btns_w=100, btns_h=50):
    number_of_answers = len(list_of_texts_for_buttons)
    y_positions_of_answer_buttons = []

    btns = []

    for ys in range(number_of_answers):
        y_btns -= 50
        y_positions_of_answer_buttons.append(y_btns)
    for a in list_of_texts_for_buttons:
        random_y = y_positions_of_answer_buttons.pop(
            random.SystemRandom().randint(0, len(y_positions_of_answer_buttons) - 1))
        btns.append(Button(text=a, size=(btns_w, btns_h), pos=(x_btns, random_y)))
    return btns


class QuestionScreen(Widget):
    def __init__(self, question, answers, btns_width=100, btns_height=50, x=350, y=450, **kwargs):
        super(QuestionScreen, self).__init__(**kwargs)
        self.add_widget(Button(text=question, size=(btns_width, btns_height), pos=(x, y)))
        btns = create_random_positioned_buttons(answers, x, y, btns_width, btns_height)
        btns[0].on_press=self.right_ans
        for b in btns:
            self.add_widget(b)

    def right_ans(self):
        print('true')


class WidgetsExmp(App):
    list_of_questions=["which?", "what?", "where?"]
    list_of_answers=[["this","that","there"],["bird","dog","cat"],["Turkey","Fiji","Israel"]]
    def build(self):
        lay = FloatLayout()
        widg = QuestionScreen("what?",["this","that","there"])
        lay.add_widget(widg)
        return lay

WidgetsExmp().run()