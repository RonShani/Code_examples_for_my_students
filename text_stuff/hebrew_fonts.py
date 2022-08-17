from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.app import App
from kivy.core.text import LabelBase
from kivy.uix.textinput import TextInput

LabelBase.register(name="Varela", fn_regular="VarelaRound-Regular.ttf")

def inverse_text(txt):
    txt = list(txt)
    invrs = []
    l = len(txt)
    for i in range(0, l):
        invrs.append(txt[l-i-1])
    return "".join(invrs)
def inverse_input_text(txt, k):
    txt = list(txt)
    invrs = []
    l = len(txt)
    if l<2:
        for i in range(0, l):
            invrs.append(txt[l-i-1])
    else:
        invrs.append(k)
        for i in range(0, l):
            invrs.append(txt[l-i-1])
    return "".join(invrs)
class MyTextInput(TextInput):
    def __init__(self,**kwargs):
        super(MyTextInput, self).__init__(**kwargs)

    def keyboard_on_key_up(self, window, keycode):
        print(keycode)
        x = self.text
        self.text = inverse_input_text(x,keycode)
        print(x)

    def build(self):
        return TextInput()

class LayoutsExmp(App):

    def build(self):
        kaf = (inverse_text("זה כפתור"))
        layBig = FloatLayout()
        btn1 = Button(text=kaf, font_name="Varela", size_hint=(0.17,0.1), pos=(300,300))
        layBig.add_widget(btn1)
        txtinput = MyTextInput(font_name="Varela",base_direction="weak_rtl",size_hint=(0.17,0.1),pos=(300,200))
        layBig.add_widget(txtinput)
        return layBig

    def onkey(window, keycode, text, modifiers):
        print(keycode)



if __name__ == '__main__':
    LayoutsExmp().run()
