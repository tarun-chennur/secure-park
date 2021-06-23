from pyasn1.codec.ber.decoder import PrintableStringDecoder
import pyrebase
import time
from keys import config



firebase = pyrebase.initialize_app(config)
db=firebase.database()

userarr=["ADAD"]# cars that have entered 
# make queue for outbound cars








#db.child("user-db").child("UID0005").child("cost").set("0")
#smtp shizz

uid = "UID0001" #Inbound uid
#timestamp = time.time() 
#print(timestamp)
def check(): #this should recieve the uid, list and queue exceed it in terms of scope
    ids=db.child("user-db").shallow().get().val()
    print(ids)
    list_users=[]
    for i in ids:
        list_users.append(i)
    if (uid in list_users): # Car has just entered, confirm if valid user
        print("Valid User")
        if uid in userarr: # check in local hashset/array
        
            calcndel()

            #get starting time from daily report and timenow-starting time ,calc cost
            #delete this user
            # ignore this uid for like 5 mins
           
            #keep in hashset for 5mins
        else:  
            registration()
            
            # also put into the hashset
            # ignore this uid for like 5 mins
    

def calcndel():
   print("bleh")
   userarr.remove(uid)
   db.child("daily-report").child(uid).remove()
   # append to the outbound car queue
            


def registration():  
    if in blacklistqueue break
    db.child("daily-report").child(uid).set(time.time())
    userarr.append(uid) 
    print(userarr)



check()




