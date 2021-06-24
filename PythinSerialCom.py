import urllib.request
import keys

def get_data():
	global data

	n = urllib.request.urlopen(keys.url).read() # get the raw html data in bytes (sends request and warn our esp8266)
	n = n.decode("utf-8") 		# convert raw html bytes format to string :3
	
	data = n
	
#	data = n.split() 			#To split data we got.

while True:
	get_data()
	print(data)
