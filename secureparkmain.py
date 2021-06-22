from pyasn1.codec.ber.decoder import PrintableStringDecoder
import pyrebase
import time
import keys.py



firebase = pyrebase.initialize_app(config)
db=firebase.database()

userarr=["ADAD"]# make queue for outbound cars








#db.child("user-db").child("UID0005").child("cost").set("0")
#smtp shizz

uid = "UID0001" #Inbound uid
#timestamp = time.time() 
#print(timestamp)
def check():
    
    if uid == db.child("user-db").child(uid).get().key(): # Car has just entered, confirm if valid user
        print("Valid User")
        if uid in userarr: # check in local hashset/array
        
            

            #get starting time from daily report and timenow-starting time ,calc cost
            #delete this user
            # ignore this uid for like 5 mins
            print("bleh")
            userarr.remove(uid)
            db.child("daily-report").child(uid).remove()
            
            #keep in hashset for 5mins
        else:  
            db.child("daily-report").child(uid).set(time.time())
            userarr.add(uid) 
            print(userarr)
            
            # also put into the hashset
            # ignore this uid for like 5 mins
    

def calcndel():
def registration():  





