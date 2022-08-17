# -*- coding: utf-8 -*-
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from float_layout_with_background import FloatLayoutWithBackground
from transitions import *

class MenuScreen(Screen):
    """
    זה קלאס שיורש את התכונות של Screen
    כלומר - יש לו את כל התכונות של הקלאס הזה ובנוסף הוספתי לו תכונות חדשות:
    1. כשיוצרים אותו הוא צריך לקבל את הסקרין-מנג'ר שלו כפרמטר -
     כי הוא צריך להיות מסוגל להחליף למסך אחר בעצמו וזאת פונקציה שקיימת רק בסקרין-מנג'ר
     2. הוא יוצר אוטומטית לייאאוט עם רקע (ווידג'ט שאני יצרתי) ומצמיד אותו למסך
     3. הוא מוסיף לו כפתור מעבר למסך שאלות וכפתור יציאה מהתוכנה
    """
    def __init__(self, screen_manager, **kwargs):
        """
        הפונקציה הזאת פועלת אוטומטית כאשר יוצרים את הקלאס הזה.
        היא מקבלת כפרמטר את screen_manager
        שזה האובייקט ששולט במעבר בין מסכים והצגתם
        *שימו לב* - כאשר מעבירים אובייקט קלאס כפרמטר הוא לא מועתק מחדש ונשלח לפונקציה, אלא רק מועבר אל הפונקציה
        הסמן שלו בזיכרון וכך ניתן לגשת אליו דרך הפונקציה.
        """
        super(MenuScreen, self).__init__(**kwargs)
        """
        'סופר' זו פקודה שפשוט אומרת שהאובייקט הזה הוא קודם הקלאס שהוא ירש (כלומר סוג של Screen)
        """
        self.screen_manager = screen_manager
        """
        קיבלנו את הפרמטר והצמדנו אותו לפונקציה ע"י הוספת self
        וזאת כדי שנוכל לגשת לאובייקט הזה גם דרך פונקציות אחרות בקלאס הזה
        """
        self.background_layout = FloatLayoutWithBackground()
        """
        יצרנו אובייקט לייאאוט עם רקע 
        """
        self.background_layout.add_widget(Button(text ='Goto questions',size_hint=(0.2,0.1), pos=(Window.size[0]*0.2,0), on_press = self.gotoquestions))
        self.background_layout.add_widget(Button(text='Quit', pos=(0,0), size_hint=(0.2,0.1), on_press = self.getout))
        """
        יצרנו כפתורים והצמדנו אותם לפונקציות שנרצה שהם יפעילו
        """
        self.add_widget(self.background_layout)
        """
        הצמדנו את הלייאאוט לקלאס הזה (כלומר למסך)
        """

    def gotoquestions(self, instance):
        """
        זאת פונקציה שמחליפה מסך
        היא מופעלת כאשר לוחצים על הכפתור המתאים שהגדרנו קודם
        """
        self.screen_manager.transition = give_me_random_transition()
        """
        ככה קבענו את סוג הטרנזישן (האופן שבו תתרחש האנימציה של שינוי המסך)
        """
        self.screen_manager.current = 'question_screen_1'
        """
        ופה נתנו פקודה לסקרין-מנג'ר לעבור למסך השאלות הראשון
        """

    def getout(self, instance):
        """
        כך נותנים פקודת יציאה/סגירה של האפליקציה
        """
        exit(1)
