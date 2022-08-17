# -*- coding: utf-8 -*-
from kivy.graphics import Rectangle, Color
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout

class FloatLayoutWithBackground(FloatLayout):
    """
    זה קלאס שיורש מ FloatLayout
    זה אומר שיש לו את כל התכונות של FloatLayout
    רק שהוספתי לו תכונה אחת - יש לרקע שלו צבע כחול כהה
    """
    def __init__(self, **kwargs):
        super(FloatLayoutWithBackground, self).__init__(**kwargs)
        with self.canvas:
            """
            כך נותנים רקע לקנווס:
            יוצרים אובייקט של ריבוע בגודל של כל המסך
            ונותנים לו את ההוראות הגרפיות (במקרה זה נתתי לו רק צבע)
            """
            Rectangle(color=Color(0,0,0.2,1), size=Window.size)
