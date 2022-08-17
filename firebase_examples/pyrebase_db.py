from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.app import App
import pyrebase
import urllib

firebaseConfig = {'apiKey': "apiKey",
                  'authDomain': "ronicubeperes.firebaseapp.com",
                  'databaseURL': "https://ronicubeperes-default-rtdb.europe-west1.firebasedatabase.app",
                  'projectId': "ronicubeperes",
                  'storageBucket': "ronicubeperes.appspot.com",
                  'messagingSenderId': "a_number",
                  'appId': "1:messagingSenderId:web:long_string",
                  'measurementId': "G-STRING"}

firebase = pyrebase.initialize_app(firebaseConfig)
db=firebase.database()
auth = firebase.auth()
user = auth.sign_in_with_email_and_password("ron@ronmail.com","123456")
#auth.set_custom_user_claims(auth, {'admin': True})
# DataBase
user = auth.sign_in_with_email_and_password("ron@ronmail.com", "123456")
print(user['idToken'])
data={"test": "ok"}
results = db.child("users").set(data, user['idToken'])

def push_to_db(data):
    #data={'age': 37, 'address':'hapardes', 'employed': True, 'name': 'Ron Shani'}
    #db.child("users").push(data)
    user = auth.sign_in_with_email_and_password("ron@ronmail.com", "123456")
    results = db.child("users").set(data, user['idToken'])
    #db.push(data)



class LayoutsExmp(App):

    def build(self):
        self.layBig = FloatLayout()
        self.te = TextInput(pos=(Window.size[0]/2-100,Window.size[1]/2),size_hint=(0.3,0.07))
        self.btn = Button(text="ok",pos=(Window.size[0]/2-100,Window.size[1]/2-80),size_hint=(0.1,0.1), on_press=self.on_ok)
        self.layBig.add_widget(self.te)
        self.layBig.add_widget(self.btn)
        return self.layBig

    def on_ok(self, instance):
        data_te = self.te.text
        print(data_te)
        push_to_db(data_te)

if __name__ == '__main__':
    LayoutsExmp().run()
