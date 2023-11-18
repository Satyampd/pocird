import pyautogui
import time
import cv2
screenWidth, screenHeight = pyautogui.size()
pyautogui.hotkey('win', '2')
time.sleep(5)
pyautogui.write("https://vahan.parivahan.gov.in/vahan4dashboard/vahan/vahan/view/reportview.xhtml")
pyautogui.press("enter")
time.sleep(5)
for i in range(1,36):
    for j in range(0 , 21):
        pyautogui.hotkey("ctrl" , "r")
        time.sleep(5)
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        for _ in range(0 , i):
            time.sleep(0.5)
            pyautogui.press("down")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("up")
        pyautogui.press("tab")
        pyautogui.press("m")
        time.sleep(0.5)
        pyautogui.press("tab")
        for _ in range(0 , j):
            time.sleep(0.5)
            pyautogui.press("down")
        pyautogui.press("tab")
        pyautogui.press("enter")
        time.sleep(5)
        r = None
        while r == None:
            time.sleep(0.5)
            print("Finding")
            r = pyautogui.locateCenterOnScreen('Reference Images\Excel.png'  , confidence=0.99)
            pyautogui.click(r)
        print("Found")
        pyautogui.moveTo(screenWidth/2, screenHeight/2)
        time.sleep(5)
        print( i , j)
Collapse
