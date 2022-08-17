# -*- coding: utf-8 -*-

from kivy.uix.screenmanager import ScreenManager
from my_screen_widget import QuestionsScreen
from question_shuffler import QuestionShuffler
from menu_screen import MenuScreen

class MyScreenManager(ScreenManager):
    """
    הקלאס MyScreenManager
    הוא יורש את כל התכונות של ScreenManager
    כלומר - הוא מתנהג בדיוק כמו סקרין-מנג'ר, רק שהוספתי לו תכונות:

    1. הוא יוצר אובייקט מהקלאס QuestionShuffler ומצמיד אותו אליו

    *האובייקט הזה לוקח את הטקסט עם כל השאלות ומפריד אותו לרשימות מסודרות*
    *בנוסף - יש בו פונקציה שכל פעם שולפת שאלה אקראית ומעבירה אותה לסקרין-מנג'ר הזה כדי שהוא ייצר באמצעותה מסך חדש*
    *הסיבה שבגללה בחרתי ליצור את האובייקט הזה ולהצמיד אותו לסקרין-מנג'ר היא שאני רוצה שיהיה רק אחד כזה - *
    *כדי שיהיה רק מאגר שאלות אחד שממנו נוציא שאלה בכל פעם וכך נדע שלא נקבל אותה שאלה פעמיים - *
    *דבר אשר היה עשוי לקרות אם הייתי יוצר אובייקט חדש כזה בכל מסך חדש שאני יוצר. סקרין-מנג'ר יש רק אחד*

    2. הוספתי לקלאס הזה משתנה מספרי שעוזר לי לדעת מה המסך הנוכחי - screen_index

    3. יצרתי שני מסכים והוספתי אותם
    """
    def __init__(self, **kwargs):
        super(MyScreenManager, self).__init__(**kwargs)
        self.questioner = QuestionShuffler()
        self.screen_index = 1
        menu_screen = MenuScreen(name='menu', screen_manager=self)
        quizz_first_screen = QuestionsScreen(name='question_screen_1', screen_manager=self)
        """
        אלו שני מסכים שיצרתי - כל מסך חייב לקבל כמשתנה את השם שלו
        וגם, כיוון שזה ווידג'ט מסך שאני יצרתי, הוא חייב לקבל את הסקרין-מנג'ר שלו - כי כך יצרתי את הקלאס הזה.
        כיוון שזה הקלאס של הסקרין מנג'ר עצמו אז ניתן לשלוח את self
        """
        self.add_widget(menu_screen)
        self.add_widget(quizz_first_screen)
