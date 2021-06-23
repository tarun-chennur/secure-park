import time
from firebase import Firebase
import keys


firebase = Firebase(keys.config)
db = firebase.database()


def calculate(enter,exit):
    return (exit-enter)/60000.0

def runner(id):
    users = db.child('users').get().val()
    for i in range(len(users)):
        user=list(users.values())[i]
        # Check if user is registered
        if user['uuid'] == id:
            curr = db.child('parked').get().val()
            #No one is parked
            if curr:
                for j in range(len(curr)):
                    #User is exiting
                    if id == list(curr.values())[j]['uuid']:
                        nowtime=time.time()
                        print(user['name'],' has a bill of Rs.', calculate(list(curr.values())[j]['entertime'],nowtime))
                        db.child('history').push({
                            'uuid':id,
                            'entertime':list(curr.values())[j]['entertime'],
                            'exittime':nowtime,
                        })
                        db.child('parked').child(list(curr.keys())[j]).remove()
                        return
            #User is entering
            db.child('parked').push({
                'uuid':id,
                'entertime':time.time(),
            })
            return
    print("User does not exist in system")


# New id recieved
# runner('UUID123456')


# Add user to the user table
# user = {'uuid':'','name':''}
# db.child('users').push(user)