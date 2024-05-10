
import pywhatkit as kit
import time

phonenumbers = ['phno','phno',]

# Message to be sent
message = "Auto generated meassage \n www.google.com"


for i,number in enumerate(phonenumbers):
    try:
        kit.sendwhatmsg_instantly(f"+{number}", message, wait_time=15,tab_close=True,close_time=5)
        # kit.sendwhats_image(number,"C:\\Users\\Avinash\\Downloads\\image-PsVOkM5mC70yIrht.jpg",tab_close=True)
    except:
        print('Not Found:',)

# Wait for messages to be sent (adjust sleep time according to your needs)
time.sleep(len(phonenumbers) * 15)