import pyautogui
import time
import pyperclip

def main():
    # while(True):
    #     print(pyautogui.position()) 
    
    pyautogui.click(1050, 1049)
    time.sleep(1)
    
    pyautogui.moveTo(713, 122)
    pyautogui.dragTo(834, 990, duration=1.0, button='left')
    
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    
    text = pyperclip.paste()
    print(text)
    
if __name__ == "__main__":
    main()