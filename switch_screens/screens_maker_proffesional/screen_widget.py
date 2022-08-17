from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.core.text import LabelBase
from floatlayoutwithbackground import FloatLayoutWithBackground
from transitions import *

LabelBase.register(name="Varela", fn_regular="C:\\Users\\ronic\\PycharmProjects\\Teaching_kivy_projects\\text_stuff\\VarelaRound-Regular.ttf")

class QuestionsScreen(Screen):

    def __init__(self, screen_index, screen_manager, questioner, **kwargs):
        super(QuestionsScreen, self).__init__(**kwargs)
        self.screen_manager = screen_manager
        self.questioner = questioner
        questions_and_answers_list = self.questioner.get_questions()
        self.screen_index = screen_index
        self.blay = FloatLayoutWithBackground()
        self.take_questions_list_and_make_a_buttons_of_them(questions_and_answers_list)
        self.put_the_buttons_on_the_layout()
        self.add_widget(self.blay)

    def put_the_buttons_on_the_layout(self):
        for b in self.btns:
            self.blay.add_widget(b)

    def take_questions_list_and_make_a_buttons_of_them(self,questions_and_answers_list:list):
        self.btns = []
        pos_x = 0.4
        pos_y = 0.8
        i=0
        for q in questions_and_answers_list:
            if 'v' in q:
                q = q.replace("v", "")
                btn = Button(text = q, size_hint=(0.2,0.1), pos_hint=({'x': pos_x, 'y': pos_y}), on_press = self.button_pressed, font_name="Varela")
                btn.index = 10
            else:
                btn = Button(text=q, size_hint=(0.2, 0.1), pos_hint=({'x': pos_x, 'y': pos_y}), on_press=self.button_pressed, font_name="Varela")
                btn.index = i
                i += 1
            self.btns.append(btn)
            pos_y -= 0.12

    def button_pressed(self, instance):
        if instance.index == 10:
            self.screen_index += 1
            next_screen_name = 'question_screen_'+str(self.screen_index)
            self.screen_manager.add_widget(QuestionsScreen(name=next_screen_name, screen_manager=self.screen_manager, screen_index=self.screen_index, questioner=self.questioner))
            self.screen_manager.transition = give_me_random_transition()
            self.screen_manager.current = next_screen_name
        else:
            print("fail")
