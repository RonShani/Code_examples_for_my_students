from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.animation import Animation

class ScrollApp(App):

    layouts_index = 2
    def build(self):
        self.lay = FloatLayout()
        self.btn2 = Button(text="Switch Layout", size_hint=(0.2, 0.1))
        self.btn2.bind(on_press=self.Btn_onpress)
        self.lay.add_widget(MyLayout_2())
        self.lay.add_widget(self.btn2)
        return self.lay

    def Btn_onpress(self, instance):
        if self.layouts_index == 1:
            self.lay.canvas.remove(self.lay.canvas.children[1])
            self.lay.add_widget(self.lay.canvas.children[1], len(self.lay.children))
            self.layouts_index = 2
            self.lay.canvas.ask_update()
        elif self.layouts_index == 2:
            self.animate(instance=self.lay.canvas.children[0])
            self.lay.canvas.remove(self.lay.canvas.children[0])
            self.lay.add_widget(MyLayout_1(), len(self.lay.children))
            self.layouts_index = 1
    def animate(self, instance):
        # create an animation object. This object could be stored
        # and reused each call or reused across different widgets.
        # += is a sequential step, while &= is in parallel
        animation = Animation(pos =(100, 100), t ='out_bounce')
        animation += Animation(pos =(200, 100), t ='out_bounce')
        animation &= Animation(size =(500, 500))
        animation += Animation(size =(100, 50))
        animation.start(instance)

class MyLayout_1(Widget):

    def __init__(self, **kwargs):
        super(MyLayout_1, self).__init__(**kwargs)
        with self.canvas:
            Image(source="road.png", size=Window.size).texture
        self.btn = Button(text="First layout", pos=(110, 100), size=(100, 50), background_color=(0, 0, 1))#, on_press=self.animate)
        self.add_widget(self.btn)
    #def build(self):
        #self.btn.on_press=self.animation

    def animation(self, instance):
        ani = Animation(pos_hint=(0.4,0.7))
        ani.start(instance)

    def animate(self, instance):
        # create an animation object. This object could be stored
        # and reused each call or reused across different widgets.
        # += is a sequential step, while &= is in parallel
        animation = Animation(pos =(100, 100), t ='out_bounce')
        animation += Animation(pos =(200, 100), t ='out_bounce')
        animation &= Animation(size =(500, 500))
        animation += Animation(size =(100, 50))
        animation.start(instance)

class MyLayout_2(Widget):

    def __init__(self, **kwargs):
        super(MyLayout_2, self).__init__(**kwargs)
        #self.pos_hint = (0.4, 0)
        with self.canvas:
            Image(source="intro.png", pos=(0, 0), size=Window.size).texture
            Button(text="Second layout", pos=(110, 100), size=(100,50), background_color=(0,1,0))

ScrollApp().run()