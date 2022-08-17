from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.app import App




class LayoutsExmp(App):

    def build(self):
        self.layBig = FloatLayout()

        self.btn1 = Button(text="Hello World!", on_press=self.on_click, size_hint=(0.15,0.07))
        self.btn1.background_color = (1, 0.4, 0.8, 1)
        self.layBig.add_widget(self.btn1)

        self.btn2 = Button(text="Hello World!", on_press=self.on_click, size_hint=(0.15,0.07), pos=(50,50))
        self.layBig.add_widget(self.btn2)

        self.btn3 = Button(text="This is red!", on_press=self.on_click, size_hint=(0.15,0.07), pos=(350,350))
        self.btn3.background_color = (1, 0, 0, 1)
        self.layBig.add_widget(self.btn3)


        return self.layBig

    def on_click(self, instance):
        print("You Clicked")



if __name__ == '__main__':
    LayoutsExmp().run()
