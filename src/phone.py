import phonenumbers as call  
import time as t

def callbomb(number):
    num=call.parse(number)
    print(num)