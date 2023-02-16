#install the module/package
#pip install pyautogui

#import the module/package
import pyautogui
import time

text = 'I love python \n'

counter = 3
#while True:
while counter>0:
   time.sleep(3)
   pyautogui.typewrite(text)
   time.sleep(2)
   pyautogui.press("Enter")
   counter -= 1