import pyautogui, time

time.sleep(3)

spam = open('spam', 'r')
for word in spam:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
spam.close()
