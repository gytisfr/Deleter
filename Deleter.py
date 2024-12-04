import pyautogui, time
print("Time to begin >:D")
while True:
    time.sleep(0.5)
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('up')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    pyautogui.press('enter')
    pyautogui.press('enter')