import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendencerealtime-d6444-default-rtdb.firebaseio.com/"
})
ref = db.reference('Employee')

data = {
    "123456":
        {
            "name": "Narendra Modi",
            "starting_year": 2017,
            "total_attendance": 7,
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "234567":
        {
            "name": "Taylor didi",
            "starting_year": 2017,
            "total_attendance": 7,
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "345678":
        {
            "name": "rapido driver",
            "starting_year": 2017,
            "total_attendance": 7,
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "456789":
        {
            "name": "Dalu didi",
            "starting_year": 2017,
            "total_attendance": 7,
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "567891":
        {
            "name": "Daidipya sisodiya",
            "starting_year": 2017,
            "total_attendance": 7,
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        }

}

for key, value in data.items():
    ref.child(key).set(value)

