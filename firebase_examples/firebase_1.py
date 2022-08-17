from firebase import Firebase, firebase

firebaseConfig = {'apiKey': "apiKey",
                  'authDomain': "ronicubeperes.firebaseapp.com",
                  'databaseURL': "https://ronicubeperes-default-rtdb.europe-west1.firebasedatabase.app",
                  'projectId': "ronicubeperes",
                  'storageBucket': "ronicubeperes.appspot.com",
                  'messagingSenderId': "a_number",
                  'appId': "1:messagingSenderId:web:long_string",
                  'measurementId': "G-STRING"}

firebase_F = Firebase(firebaseConfig)

firebase_data = firebase.FirebaseApplication("https://ronicubeperes.firebaseio.com/", None)
data = {
    "Name": "Ron",
    "Email": "r@r.il",
    "Password": "123456"
}
user_name=firebase_data.get("https://ronicubeperes.firebaseio.com/users","ron")
eml = input("email? ")
pswrd = input("Password?")
print(eml, user_name['email'], pswrd, user_name['password'])
if eml == str(user_name['email']) and pswrd == str(user_name['password']):
    print("good")
else:
    print(firebase_data.get("https://ronicubeperes.firebaseio.com/users","ron"))
