import pyautogui, time
import pyperclip as clip

def CopyPasteTypeWrite(Text, times=1, delay=0, EnterAfter=False):
    Befor_Copied = clip.paste()
    clip.copy(Text)
    time.sleep(delay)

    for i in range(times):
        pyautogui.hotkey("ctrl", "v")

        if EnterAfter:
            pyautogui.press("enter")

    clip.copy(Befor_Copied)

    
    


CopyPasteTypeWrite("لگ", 5, 1,True)


