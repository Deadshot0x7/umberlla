try:
    from src import sms
    from src import phone
    import time as t 
    import pyfiglet as p 
    import sys as s 
    import logging
    import os as o 
except ImportError as e:
    print("Some Header  are missing, yep they are missing")


def printbanner():
    banner= p.figlet_format("Umberlla",font="bulbhead")
    print(banner)




if __name__ == "__main__":
    print("Deadshot0x7  is not responsible for  the loos you have made by any means ")
    a=str(input(">>>>\t\t"))
    if a=="yes" or a =="y":
        logging.info("I'm responsible fot the loss I've made ")
    else:
        exit
    
    printbanner()
    while(True):
        try:
            if s.argv[1]=="help":
                t.sleep(10)
                print("Command            Usage                                    description ")
                print("sms               start phone number and numbers of threads     Start the sms bombing  ith giving threads       ")
                print("ph                start phone number and numbers of threads     Start the phone bombing  ith giving threads")
                break
            elif s.argv[1]=="sms":
                sms.sendsms(s.argv[2])
                break
            elif s.argv[1]=="ph":
                phone.callbomb(s.argv[2])
                
        except KeyboardInterrupt as e:
            print("Unexception Key closing the program ")
            t.sleep(1)
            break
        
        except Exception as e:
            print("Unknow command")
            t.sleep(1)
            break

        
