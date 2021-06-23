from pyasn1.codec.ber.decoder import PrintableStringDecoder
import pyrebase
import time
from keys import config


firebase = pyrebase.initialize_app(config)
db=firebase.database()

#uid = "UID0001"

def check(): #this should recieve the uid, list and queue exceed it in terms of scope
    while(1):
        uid = input("Enter uid ")
        

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
            
                calcndel(uid)
            else:  
                registration(uid)
        else:
            print("INVALID USER DETECTED")


def calctime(pt):
   timenow=time.time()
   diff=(timenow-pt)
   print("THE DIFFERENCE IN TIME IS",diff)
   return diff

def calcndel(uid):
   prkd_time=db.child("daily-report").child(uid).child("time-of-parking").get().val() 
   print("HHAHA")
   ishelessthanamin=calctime(prkd_time)
   if(ishelessthanamin<=120):
       return
   else:
        print("DELETE THIS")       
        db.child("outbound-cars").child(uid).child("Departure-time").set(time.time())
        park_time=db.child("daily-report").child(uid).child("time-of-parking").get().val()
        diff=time.time()-park_time
        cost= (diff) + float((db.child("user-db").child(uid).child("cost").get().val()))
        db.child("user-db").child(uid).child("cost").set(cost)

        db.child("daily-report").child(uid).remove()
        return
    
            

def registration(uid):  
    ids=db.child("outbound-cars").shallow().get().val()
    list_blklist=[]
    for i in ids:
        list_blklist.append(i)
    if uid in list_blklist:
        exit_time=db.child("outbound-cars").child(uid).child("Departure-time").get().val() 
        print(exit_time)
        ishelessthan5=calctime(exit_time)
        if(ishelessthan5<=300):
            print("PLEASE RETURN AFTER 5 MINS")
            return
        else:
            print("ITS been more than 5mins welcome back")
            db.child("daily-report").child(uid).child("time-of-parking").set(time.time())
            
            db.child("outbound-cars").child(uid).remove()  
            return
    
        
    else:
        print("IT SHOULD GET HERE")
        db.child("daily-report").child(uid).child("time-of-parking").set(time.time())
        return    

check()




