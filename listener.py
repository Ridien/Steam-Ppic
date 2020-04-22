import time
from savefile import downloadImage
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from steam import updatePicture
from tagrandomizer import getRandomImage
import difflib

def read_file():
    with open("C:/Program Files (x86)/Steam/steamapps/common/Counter-Strike Global Offensive/csgo/test.log", "r", encoding="utf8") as f:
        SMRF1 = f.readlines()


    return SMRF1

    
def checkMessage(message):
    if "(Terrorist)" in message or "(Counter-Terrorist)" in message:
        print(message)
        if "-danbooru" in message:
            print('this is a valid command:' + message)
            
            command = message.split('-danbooru ', 1)[1]
            print('the command is:' + command)
            command = str(command)
            command = command.strip()
            if command.isdigit():
                downloadImage(command)
            elif command == "force":
                updatePicture()
            else:
                getRandomImage(command)

            updatePicture()

            
            
                       
            
    
    




initial = read_file()
while True:
    current = read_file()
    if initial != current:
        checkMessage(current[-1])
        initial = current