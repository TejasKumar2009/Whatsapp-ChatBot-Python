import pyautogui as pg
import time
import pyperclip

import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY_HERE") #configure api key.

client = genai.GenerativeModel('gemini-2.0-flash') #setup the model.

print("Shift to the whatsapp web window under 10 seconds")

time.sleep(10)



while True:
    time.sleep(3)
    pyperclip.copy('')
    pg.moveTo(762, 889)
    pg.doubleClick()
    pg.doubleClick()
    pg.hotkey("Ctrl", "c")
    message = pyperclip.paste()
    if message=="Stop" or message=="stop":
        break
    elif message != '':
        response = client.generate_content(message+" Don't answer in more than 50 words pls pls i am requesting u")
        time.sleep(1)
        pg.moveTo(851, 966)
        pg.click()
        pg.write(response.text)
        pg.press("enter")
    else:
        time.sleep(1)
        pg.moveTo(1826, 892 )
        pg.click()
