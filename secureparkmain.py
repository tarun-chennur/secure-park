from pyasn1.codec.ber.decoder import PrintableStringDecoder
import pyrebase
import time
from keys import config


firebase = pyrebase.initialize_app(config)
db=firebase.database()


uid = "UID0001"

def check(): #this should recieve the uid, list and queue exceed it in terms of scope
    ids=db.child("user-db").shallow().get().val()
    prkd=db.child("daily-report").shallow().get().val()
    print(ids)
    list_users=[]
    for i in ids:
        list_users.append(i)
    list_parked=[]
    for i in prkd:
        list_parked.append(i)    
    if (uid in list_users): # Car has just entered, confirm if valid user
        print("Valid User")
        if uid in list_parked: # check in local hashset/array
        
            calcndel()
        else:  
            registration()
    else:
        print("INVALID USER DETECTED")


def calctime(pt):
   timenow=time.time()
   diff=(pt-timenow)
   return diff

def calcndel():
   prkd_time=db.child("daily-report").child(uid).get().val() 
   ishelessthanamin=calctime(prkd_time)
   if(ishelessthanamin<=120):
       return
   else:
  
        db.child("outbound-cars").child("uid").set("x")
        park_time=db.db.child("daily-report").child(uid).child("time-of-parking").get().val()
        diff=time.time()-calctime(park_time)
        cost= (diff*1) + (db.child("user-db").child("uid").child("cost"))
        db.child("user-db").child("uid").child("cost").set(cost)

        db.child("daily-report").child(uid).remove()
        return
    
            

def registration():  
    ids=db.child("outbound-cars").shallow().get().val()
    list_blklist=[]
    for i in ids:
        list_blklist.append(i)
    if uid in list_blklist:
        exit_time=db.child("outbound-cars").child(uid).get().val() 
        ishelessthan5=calctime(exit_time)
        if(ishelessthan5<=300):
            return
        else:
            db.child("daily-report").child(uid).child("time-of-parking").set(time.time())
            
            db.child("outbound-cars").child(uid).remove()  
            return
    
        
    else:
        db.child("daily-report").child(uid).child("time-of-parking").set(time.time())
        return    

check()




