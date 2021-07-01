import pyautogui, time

time.sleep(3)

dreamcast = open('dreamcast', 'r')
for word in dreamcast:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
dreamcast.close()
