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
storage = firebase.storage()

#Auth

def login_fnc(email, password):
    try:
        auth.sign_in_with_email_and_password(email, password)
        print("succesfull!")
        return True
    except Exception as inst:
        print("not valid")
        print(inst)
        return False

def signup_fnc(email, password):
    auth.create_user_with_email_and_password(email, password)

#Storage

def upload_to_db(filename, cloudfilename):
    storage.child(cloudfilename).put(filename)

def download_from_db(cloudfilename, localfilename):
    storage.child(cloudfilename).download("/user",localfilename)

download_from_db("t.txt","t.txt")
def get_url(cloudfilename):
    url = storage.child(cloudfilename).get_url(None)
    print(url)
    f = urllib.request.urlopen(url).read()
    print(f)

# DataBase

def push_to_db(data):
    #data={'age': 40, 'address':'hapardes', 'employed': True, 'name': 'Ron Shani'}
    db.push(data)




class LayoutsExmp(App):

    def build(self):
        win = Window
        w=win.width
        h=win.height
        prop_w = 0.25
        prop_h = 0.07
        obj_w = prop_w*w
        obj_h = prop_h*h
        xpos = w/2-(obj_w/2)
        ypos = h-100
        self.layBig = FloatLayout()
        self.btn_auth = Button(text="OK", pos=(xpos,ypos), size_hint=(prop_w, prop_h), on_press=self.gobtn)
        self.input_user = TextInput(pos=(xpos,(ypos-(obj_h*1))), size_hint=(prop_w, prop_h), multiline=False)
        self.lbl_usr = Button(text="uername", pos=(xpos,ypos-(obj_h*2)), size_hint=(prop_w, prop_h), background_color=(1,0,0,0))
        self.input_pass = TextInput(pos=(xpos, ypos-(obj_h*3)), size_hint=(prop_w, prop_h), multiline=False)
        self.lbl_pas = Button(text="password", pos=(xpos, ypos-(obj_h*4)), size_hint=(prop_w, prop_h), background_color=(1, 0, 0, 0))
        self.layBig.add_widget(self.btn_auth)
        self.layBig.add_widget(self.input_user)
        self.layBig.add_widget(self.input_pass)
        self.layBig.add_widget(self.lbl_usr)
        self.layBig.add_widget(self.lbl_pas)
        return self.layBig

    def gobtn(self, inst):
        usr = self.input_user.text
        pas = self.input_pass.text
        if login_fnc(usr, pas):
            self.lbl_usr.text="success!"

#if __name__ == '__main__':
#    LayoutsExmp().run()
