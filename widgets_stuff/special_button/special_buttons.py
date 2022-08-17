# -*- coding: utf-8 -*-
"""
הקוד הזה מדגים את מה שניסיתי ללמד בכיתה:
איך יוצרים קלאסים של אובייקטים משל עצמכם
"""
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App


class SpecialButton(Button):
    """
זה קלאס של כפתור מותאם אישית
    בסוגריים יש את השם של הקלאס שהוא יורש ממנו
    """
    def __init__(self, the_text_on_the_button, **kwargs):
        """
        זאת הפונקציה שיוצרת את האובייקט
        בדוגמה העברנו פרמטר לפונקציה הזאת (טקסט שיהיה כתוב על הכפתור)
        """
        super(SpecialButton, self).__init__(**kwargs)
        """
        ה"סופר" הזה זאת שורה שמאפשרת לנו לרשת את כל הפונקציות של הקלאס שירשנו - ואף לשנות אותן
        למשל בדוגמה הזאת אפשר לראות למטה שכתבנו את הפונקציה on_press
        וזאת תהיה התנהגות ברירת המחדל של הקלאס הזה כאשר לוחצים עליו
        """
        self.text = the_text_on_the_button
        self.size_hint = (0.3, 0.07)
        self.pos_hint = ({'x': 0.35, 'y': 0.465})
        self.background_color = "red"
        """
        למעלה קבענו את הטקסט שכתוב על הקלאס הזה כברירת מחדל,
        את הגודל שלו, את המיקום ואת הצבע.
        הפרמטרים הללו ניתנים לשינוי - פשוט כשיוצרים אובייקט חדש מהקלאס הזה יש לו כבר הגדרות ברירת מחדל,
        בדיוק כפי שכשיוצרים אובייקט מקלאס Button
        ברירת המחדל היא שלא כתוב עליו כלום. 
        """

    def on_press(self):
        """
        פה הגדרנו פוקציית ברירת מחדל לon_press
        """
        self.background_color = "blue"

    def on_release(self):
        """
        פה הגדרנו פוקציית ברירת מחדל on_release
        """
        self.background_color = "red"


class Main(App):
    def build(self):
        lay = FloatLayout()
        """
        כעת כשאנחנו יוצרים אובייקט מקלאס SpecialButton
        יש לו כבר את כל הגדרות הקלאס שכתבנו
        ובנוסף יש לו התנהגות של כפתור - כי הקלאס הזה ירש את Button
        """
        btn = SpecialButton("This is the text on the button")
        lay.add_widget(btn)
        return lay

Main().run()
