# -*- coding: utf-8 -*-
"""
בקובץ הזה יצרתי קלאס של מסך (יורש מ Screen)
*יש פה קוד שכתוב בצורה שגויה בכוונה - *
* וזה מתייחס למספר פונקציות שנמצאות מחוץ לקלאס*
*כלומר - הן פשוט קיימות כפונקציות כלליות שלא משוייכות לקלאס הזה*
*באופן תקין הפונקציות הללו היו אמורות להיכלל בקלאס*
*מכיוון שהן יוצרות עבורו כפתורים ומנהלות את החלפת המסך כאשר עונים תשובה נכונה*
*הן נכתבו מחוץ לקלאס לשם הבהירות של הקוד בלבד*
*כי אם הייתי מכניס את המילה self בכל מקום היה קשה לקרוא את זה*

שימו לב שאנחנו צריכים לטעון פונטים בעברית - מכיוון שהן לא חלק מברירת המחדל של סביבת העבודה
"""
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.core.text import LabelBase
from float_layout_with_background import FloatLayoutWithBackground
from transitions import *
LabelBase.register(name="Varela", fn_regular="VarelaRound-Regular.ttf")

class QuestionsScreen(Screen):
    """
    זה הקלאס שמייצר מסכים של שאלות
    הוא יורש מ Screen והוא מאד דומה
    לקלאס בקובץ menu_screen ושם גם תמצאו הסברים מקיפים
    """
    def __init__(self, screen_manager, **kwargs):
        """
        הפונקציה הזאת פועלת בכל פעם שאני יוצר אובייקט מהקלאס הזה
        היא מפעילה פונקציות שפונות לאובייקט של יצירת השאלות (questioner)
        הן מקבלות ממנו את השאלה שנשלפה אקראית (וגם את התשובות השגויות והתשובה הנכונה) ויוצרות כפתורים בהתאם
        """
        super(QuestionsScreen, self).__init__(**kwargs)
        self.background_layout = FloatLayoutWithBackground()
        self.screen_manager = screen_manager
        """
        בשורות מטה, לפי הסדר:
         1. קריאה לפונקציה ששולפת שאלה ותשובות
         2. פונקציה שמקבלת ליסט של טקסטים (שאלה ותשובות) ומחזירה ליסט של כפתורים שהיא יצרה
         3. פונקציה שפשוט מצמידה את הכפתורים ללייאאוט
        """
        question_and_answers = get_question_and_answers_list_from_questioner(self)
        buttons = take_questions_list_and_make_a_buttons_of_them(self, question_and_answers)
        put_the_buttons_on_the_layout(self, buttons)

        self.add_widget(self.background_layout)

    def button_pressed(self, instance):
        """
        זאת הפונקציה שמופעלת כשלוחצים על כפתור
        כשיצרנו את הכפתור נתנו אינדקס מיוחד לתשובה הנכונה - 10
        הפונקציה הזאת פשוט בודקת אם באמת לחצנו על התשובה הנכונה, לפי האינדקס
        ומעבירה אותנו מסך אם כן
        אם לא - היא מדפיסה הודעה "fail"
        """
        if instance.index == 10:
            """
            יצרתי פונקציה שכל מה שהיא עושה זה ליצור מחרוזת עם השם של המסך הבא
            """
            next_screen_name = get_next_screen_name(self.screen_manager)
            """
            בשורות מטה, לפי הסדר:
            1. יוצרים מסך חדש (באמצעות הווידג'ט בקובץ הזה) ומוסיפים אותו לסקרין-מנג'ר
            2. אומרים לסקרין-מנג'ר שיוציא טרנזישן אקראי
            3. אומרים לסקרין-מנג'ר שיעבור למסך הבא שיצרנו הרגע
            """
            self.screen_manager.add_widget(QuestionsScreen(name=next_screen_name, screen_manager=self.screen_manager))
            self.screen_manager.transition = give_me_random_transition()
            self.screen_manager.current = next_screen_name
        else:
            print("fail")

def get_question_and_answers_list_from_questioner(self):
    """
    פונקציה שפשוט מקבלת רשימה של מחרוזות: שאלה ותשובות מהאובייקט של הסקרין-מנג'ר
    ומחזירה אותה
    """
    questions_and_answers_list = self.screen_manager.questioner.get_questions()
    return questions_and_answers_list

def take_questions_list_and_make_a_buttons_of_them(self, questions_and_answers_list):
    """
    זאת פונקציה שמקבלת רשימה של מחרוזות ויוצרת מכל אחת כפתור בהתאם
    את מחרוזת התשובה שמסומנת באות v היא הופכת לכפתור עם אינדקס מיוחד - 10, כדי שנדע שזו התשובה הנכונה
    *שימו לב שהיא קודם כל מעיפה את הסימון הזה מהמחרוזת כדי שלא יופיע כפתור עם האות v*

    כל כפתור מקבל גודל ומיקום ומונח עליו הטקסט. בנוסף הוא מקבל פרמטר שאין לכפתורים - index
    *מותר להוסיף איזה פרמטר שרוצים כל עוד השם חוקי*
    """
    btns = []
    pos_x = 0.4
    pos_y = 0.8
    i=0
    for q in questions_and_answers_list:
        if 'v' in q:
            """
            ככה מוציאים משהו ממחרוזת - פשוט מחליפים אותו בכלום
            """
            q = q.replace("v", "")
            btn = Button(text = q, size_hint=(0.2,0.1), pos_hint=({'x': pos_x, 'y': pos_y}), on_press = self.button_pressed, font_name="Varela")
            btn.index = 10
        else:
            btn = Button(text=q, size_hint=(0.2, 0.1), pos_hint=({'x': pos_x, 'y': pos_y}), on_press=self.button_pressed, font_name="Varela")
            btn.index = i
            i += 1
        btns.append(btn)
        pos_y -= 0.12
    return btns

def get_next_screen_name(screen_manager):
    """
    זאת פונקציה שעוזרת לנהל את המסכים
    היא מעלה את ה screen_index באחד (כי היא מופעלת כאשר עונים תשובה נכונה)
    ואז יוצרת באמצעותו את המחרוזת שמהווה את השם של המסך הבא
    """
    screen_manager.screen_index += 1
    next_screen_name = 'question_screen_' + str(screen_manager.screen_index)
    return next_screen_name

def put_the_buttons_on_the_layout(self, btns):
    """
    זאת פשוט פונקציה ששמה את הכפתורים על הלייאאוט
    """
    background_layout = self.background_layout
    for b in btns:
        background_layout.add_widget(b)


