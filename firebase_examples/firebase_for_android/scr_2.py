from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, WipeTransition
from kivy.uix.floatlayout import FloatLayout
import requests
import asynckivy as ak

class screen_1(Screen):
    __FIREBASE_USER_VERIFY_SERVICE = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword"
    __FIREBASE_API_KEY = "your api key"

    def __init__(self, manager, **kwargs):
        super(screen_1, self).__init__(**kwargs)
        self.sm = manager
        self.layBig = FloatLayout()
        self.btn1 = Button(text="log in", size_hint=(0.15, 0.15), pos_hint=({'x': 0.40, 'y': 0.40}),on_press=self.login_fnc)
        self.layBig.add_widget(self.btn1)

        self.btn2 = Button(text="sing up", size_hint=(0.15, 0.15), pos_hint=({'x': 0.40, 'y': 0.20}),on_press=self.signup_fnc)
        self.layBig.add_widget(self.btn2)

        self.password = TextInput(hint_text="password", pos_hint=({'x': 0.15, 'y': 0.60}), size_hint=(0.7, 0.07))
        self.layBig.add_widget(self.password)

        self.email = TextInput(hint_text="e-mail", pos_hint=({'x': 0.15, 'y': 0.80}), size_hint=(0.7, 0.07))
        self.layBig.add_widget(self.email)
        self.add_widget(self.layBig)

    async def user_login(self, email, passwd):
        url = "%s?key=%s" % (self.__FIREBASE_USER_VERIFY_SERVICE, self.__FIREBASE_API_KEY)
        data = {"email": email,
                "password": passwd,
                "returnSecureToken": True}
        try:
            result = await ak.run_in_thread(lambda: requests.post(url, json=data,timeout=2))
        except requests.Timeout:
            print("TIMEOUT!")
        else:
            print('RECEIVED:', result)
            if 'error' in result.text:
                print("bad")
            else:
                self.sm.transition = WipeTransition()
                self.sm.current = 'pass_ok'

    def login_fnc(self, instance):
        ml = str(self.email.text)
        ps = str(self.password.text)
        ak.start(self.user_login(ml,ps))

    def signup_fnc(self, instance):
        self.auth.create_user_with_email_and_password(self.email.text, self.password.text)
        print("succesfull!")
        self.sm.transition = WipeTransition()
        self.sm.current = 'pass_ok'
