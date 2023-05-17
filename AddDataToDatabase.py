import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-bd7e6-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "321654":
        {
            "name": "Murtaza Hassan",
            "major": "Robotics",
            "starting_year": 2017,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "852741":
        {
            "name": "Emly Blunt",
            "major": "Economics",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "221155":
        {
            "name": "Hassan Zidan",
            "major": "Bioinformatics",
            "starting_year": 2019,
            "total_attendance": 1,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-4-14 00:54:34"
        },
    "231245":
        {
            "name": "Hossam El-Shahawy",
            "major": "Bioinformatics",
            "starting_year": 2019,
            "total_attendance": 3,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-4-14 00:54:34"
        },
    "112255":
        {
            "name": "Ahmed Ramadan",
            "major": "Bioinformatics",
            "starting_year": 2019,
            "total_attendance": 5,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-4-14 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)
