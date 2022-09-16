import pyautogui # in terminal type "pip install pyautogui" and press enter
import time

time.sleep(5) # delaying time in seconds after running code

for x in range(5):
    pyautogui.typewrite("hi")    #this method will type hi automatically where mouse pointer is placed
    pyautogui.press("enter")     #if the message is sent by pressing enter, then this method will press enter automatically

