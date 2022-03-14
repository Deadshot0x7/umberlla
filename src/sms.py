
load json data from source
import  requests , json
import time as t 
import sys as s
import phonenumbers

def sendsms(number):
   # mention url
   url = "https://www.fast2sms.com/dev/bulk"
   # create a dictionary
   my_data = {
       
	  # Your default Sender ID
	  'sender_id': 'FSTSMS',
	  # Put your message here!
	 'message': 'This is a test message',
	
	'language': 'english',
	'route': 'p',
	
	# You can send sms to multiple numbers
	# separated by comma.
	'numbers': number
}

# create a dictionary
headers = {
	'authorization': 'a2cudzRO1pSqXo0Dk7vAQ6yK4sLYUNhFgVjC3t9Zm8IWrfTJHnhcYwSk6AimxPogVCnelbjGzQv20aKd',
	'Content-Type': "application/x-www-form-urlencoded",
	'Cache-Control': "no-cache"
}

# make a post request
response = requests.request("POST",
							url,
							data = my_data,
							headers = headers)
#

returned_msg = json.loads(response.text)

# print the send message
print(returned_msg['message'])

 