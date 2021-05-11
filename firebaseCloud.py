import pyrebase
import json

f = open('config.json','r')
config = json.load(f)



# firebase = pyrebase.initialize_app(config['firebase'])
# db = firebase.database()

from firebase import firebase
db = firebase.FirebaseApplication(config['firebase_url'], None)

db.put('', 'Train', {'name' : 'Rush'})
print(db.get("/Train", None))