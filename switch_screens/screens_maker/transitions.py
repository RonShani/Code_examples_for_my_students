# -*- coding: utf-8 -*-
"""
זה קובץ שמכיל רשימה של כל המעברי מסך (טרנזישנס) ופונקציה שמגרילה כל פעם מעבר אחר באופן אקראי.
מלבד הבידור אין בזה צורך אמיתי, אבל יש בזה דוגמה לאופן שבו ניתן ליצור מבנה קריא של הקוד
וגם ארכיטקטורה נכונה -
  הפונקציה הזאת נכתבה בקובץ נפרד מכיוון שגם menu_screen וגם my_screen_widget עושים בה שימוש
  ואנחנו ל-ע-ו-ל-ם לא נרצה לקחת את אותו קוד ולהעתיק אותו פעמיים
"""

from kivy.uix.screenmanager import WipeTransition, SlideTransition, CardTransition, FallOutTransition
import random
Transitions = [WipeTransition(), SlideTransition(), CardTransition(), FallOutTransition()]

def give_me_random_transition():
    return random.choice(Transitions)
