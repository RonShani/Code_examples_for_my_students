from kivy.graphics import Rectangle, Color
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout

class FloatLayoutWithBackground(FloatLayout):
    """
    This class is a FloatLayout class with a color i chose.
    It's an example of how to make a custom object that can be used
    anywhere in your app.
    """
    def __init__(self, **kwargs):
        super(FloatLayoutWithBackground, self).__init__(**kwargs)
        with self.canvas:
            Rectangle(color=Color(0,0,0.2,1), size=Window.size)
