import time
import datetime
from firebase import Firebase
import keys

firebase = Firebase(keys.config)
db = firebase.database()

def check(outime, intime):
    if outime-intime<300:
        print("Duplicate")
        return 0
    return 1


def calculate(enter,exit):
    bill = 0 
    diff = (exit-enter)/3600.0
    if diff>=0 and diff <=4:
        bill += diff*10
    if diff>4 and diff<=14:
        diff -= 4
        bill += diff*9
    if diff>14:
        diff -=10
        bill += diff*8
        
    return bill

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
                        #Duplicate check
                        if check(nowtime, list(curr.values())[j]['entertime'] ):
                            bill = calculate(list(curr.values())[j]['entertime'],nowtime)
                            print(user['name'],' has a bill of Rs.', bill)
                            db.child('history').push({
                                'uuid':id,
                                'entertime':list(curr.values())[j]['entertime'],
                                'exittime':datetime.datetime.now().strftime("%H:%M:%S"),
                                'bill': bill,
                            })
                            db.child('users').child(list(users.keys())[i]).update({'total_bill':user['total_bill']+bill})
                            db.child('parked').child(list(curr.keys())[j]).remove()
                        return
            #User is entering
            db.child('parked').push({
                'uuid':id,
                'entertime':time.time(),
                'time': datetime.datetime.now().strftime("%H:%M:%S")
            })
            print(user['name'], " has enetered parking at ", datetime.datetime.now().strftime("%H:%M:%S"))
            return
    print("User does not exist in system")


# New id recieved
# runner('UUID654321')


# Add user to the user table
# user = {'uuid':'UUID654321',
    # 'name':'Tarun',
    # 'company_name':'IBM',
    # 'phone_no':'235423423',
    # 'email_id':'tarun@ibm.com',
    # 'vehicle_no':'KA23424',
    # 'vehicle_type':'car',
    # 'total_bill':'0'
    # }
# db.child('users').push(user)