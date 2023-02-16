#install the package
#pip install PyAutoGUI

#import the package/module
import pyautogui
import tkinter as tk

root = tk.Tk()
root.title('Sc Taker')

canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()

def myScreenshot():
   sc = pyautogui.screenshot()
   sc.save(r'C:\Users\Nishant Singh\Desktop\Python\Python_Video_Code\screenshot_code_output.png')
   
   myButton = tk.Button(root,text='Take Screenshot', command=myScreenshot, bg='red', fg='yellow', width = '30', height = '20')
   #canvas1.create_window(150,150, window= myButton)
   
root.mainloop()