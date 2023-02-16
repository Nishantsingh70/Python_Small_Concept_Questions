#install the module/package
#pip install pywhatkit

#import the module/package
import pywhatkit as kt
import getpass as gp

print("Let's Automate Whatsapp!!")

p_num = gp.getpass(prompt="PhoneNumber: ", stream=None)

msg = 'I love Python'

#time mention here
kt.sendwhatmsg(p_num, msg, 15 , 30)

