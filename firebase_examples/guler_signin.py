from kivy.uix.button import Button
#from olol import Bak
import threading
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, WipeTransition, ScreenManager
from kivy.uix.floatlayout import FloatLayout
from firebase import Firebase

firebaseConfig = {'apiKey': "apiKey",
                  'authDomain': "ronicubeperes.firebaseapp.com",
                  'databaseURL': "https://ronicubeperes-default-rtdb.europe-west1.firebasedatabase.app",
                  'projectId': "ronicubeperes",
                  'storageBucket': "ronicubeperes.appspot.com",
                  'messagingSenderId': "a_number",
                  'appId': "1:messagingSenderId:web:long_string",
                  'measurementId': "G-STRING"}

firebase = Firebase(firebaseConfig)
auth = firebase.auth()

class screen_1(Screen):

    def __init__(self, manager, **kwargs):
        super(screen_1, self).__init__(**kwargs)
        self.sm = manager
        self.layBig = FloatLayout()
        #self.layBig.add_widget(Bak())
        self.btn1 = Button(text="log in", size_hint=(0.15, 0.15), pos_hint=({'x': 0.40, 'y': 0.20}),on_press=self.start_second_thread)
        self.layBig.add_widget(self.btn1)

        self.btn2 = Button(text="sing up", size_hint=(0.15, 0.15), pos_hint=({'x': 0.40, 'y': 0.40}),on_press=self.signup_fnc)
        self.layBig.add_widget(self.btn2)

        self.password = TextInput(hint_text="password:", pos_hint=({'x': 0.15, 'y': 0.60}), size_hint=(0.7, 0.07))
        self.layBig.add_widget(self.password)

        self.email = TextInput(hint_text="email:", pos_hint=({'x': 0.15, 'y': 0.80}), size_hint=(0.7, 0.07))
        self.layBig.add_widget(self.email)
        self.add_widget(self.layBig)

    def start_second_thread(self, ins):
        threading.Thread(target=self.login_fnc).start()

    def login_fnc(self):
        print("try")
        try:
            x=auth.sign_in_with_email_and_password(self.email.text, self.password.text)
            auth.refresh(x['refreshToken'])
            print("success!",x)
        except:
            print("failed")
        print("ended")
        self.sm.transition = WipeTransition()
        self.sm.current = 'home_scr'

    def signup_fnc(self, instance):
        auth.create_user_with_email_and_password(self.email.text, self.password.text)
        print("succesfull!")
        self.sm.transition = WipeTransition()
        self.sm.current = 'home_scr'