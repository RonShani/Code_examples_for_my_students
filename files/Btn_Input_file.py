from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.app import App




class LayoutsExmp(App):

    def build(self):
        layBig = FloatLayout()

        self.btn1 = Button(text="Hello World!", on_press=self.on_click)
        layBig.add_widget(self.btn1)
        # create a text input
        self.textinput = TextInput(text='Hello world', multiline=False, size_hint=(1, 0.3))
        self.textinput.bind(on_text_validate=self.on_enter)
        layBig.add_widget(self.textinput)
        self.btn1.background_color = (1, 0.4, 0.8, 1)
        return layBig

    def on_enter(instance, value):
        x = value.text
        print(x)

    def on_click(self, instance):
        x=self.textinput.text
        print(x)
        f = open("roni.txt", "a")
        f.write(x)
        f.close()



if __name__ == '__main__':
    LayoutsExmp().run()
