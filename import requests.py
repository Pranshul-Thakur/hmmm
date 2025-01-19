#for discord
import requests 

payload = {
    'content' : ''''''
}

header = {
    'authorization' : '' #insert api here

}

for i in range(100000):
    r = requests.post('', data = payload, headers = header)


#for instagram (doesnt need api and dm url)
'''import pyautogui
import time

time.sleep(3)

post_link = "" 

repeat_count = 10000

delay = 1



for _ in range(repeat_count):
   pyautogui.typewrite(post_link) 
   pyautogui.press("enter") 
   time.sleep(delay) '''
