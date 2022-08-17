from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.core.window import Window

# -*- coding: utf-8 -*-
class Sheilta(Widget):
    def __init__(self, **kwargs):
        super(Sheilta, self).__init__(**kwargs)
        with self.canvas:
            Rectangle(texture=Image(source="ask_0.png").texture, size=(615/2,425/2))

    def check_word(self, wrd:str):


class BonusApp(App):

    def build(self):
        x = -170
        y = -150

        self.layBig = FloatLayout()
        self.sqrs=[]
        i=0
        for r in range(10):
            for c in range(10):
                self.sqrs.append(Image(source="bonus_sqr.png", pos=(x,y)))
                self.layBig.add_widget(self.sqrs[i])
                i+=1
                x+=34
            x = -170
            y += 30
        self.layBig.add_widget(Sheilta())
        return self.layBig

class verbs_checker():

    perfixes=['א','ל','י','ת','מ','נ']
    def __init__(self):
        f = open("words.txt", "r+")
        self.words_list = str(f.read())
        f.close()

    def suspected_as_verb(self,wrd:str):
        for i in self.perfixes:
            if wrd.startswith(i):
                return True
        return False

    def get_list_of_verbs(self,wrd:str):
        vrbs = []
        for w in self.perfixes:
            vrbs.append(w+wrd[1:])
        return vrbs

    def check_if_in_list(self, wrd: str):
        if wrd in self.words_list:
            return True
        return False
"""
vc = verbs_checker()
x = input("enter a word:")
if vc.check_if_in_list(x):
    print("exist")
if vc.suspected_as_verb(x):
    verbs_list=vc.get_list_of_verbs(x)
    for v in verbs_list:
        if vc.check_if_in_list(v):
            print(v)
"""
if __name__ == '__main__':
    BonusApp().run()