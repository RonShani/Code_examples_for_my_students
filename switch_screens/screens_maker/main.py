# -*- coding: utf-8 -*-
"""
 דוגמה לאפליקציה שכתובה בצורה נכונה
 כל הפונקציות מחולקות לקלאסים ובתוכן תמצאו הסברים
"""
from kivy.app import App
from my_screen_manager import MyScreenManager


class QuizzApp(App):

    def build(self):
        """
        כל מה שהקלאס הראשי עושה זה
        ליצור אובייקט של MyScreenManager
        בתוך האפליקציה ולהחזיר אותו
        """
        screenmanager = MyScreenManager()
        return screenmanager

if __name__ == '__main__':
   QuizzApp().run()