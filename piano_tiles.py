from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1) #This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

x_coords = [550, 630, 710, 790]
color = (0, 0, 0)

click(672, 480)
time.sleep(0.5)
while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(550, 330)[0] == 0:
        click(550, 330)
    if pyautogui.pixel(630, 330)[0] == 0:
        click(630, 330)
    if pyautogui.pixel(710, 330)[0] == 0:
        click(710, 330)
    if pyautogui.pixel(790, 330)[0] == 0:
        click(790, 330)

#while not keyboard.is_pressed('q'):
#    picture = pyautogui.screenshot(region=(550, 330, 241, 1))
#    for x in x_coords:
#        if picture.getpixel((x - 550, 0))[0] == 0:
#            click(x, 330)
#            #mouse.move(x, 330)
#            #mouse.click('left')