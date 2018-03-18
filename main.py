import time
import os
import wikiquote
import random

def beep():
    print ('\a')
    time.sleep(1)
    print ('\a')
    time.sleep(1)
    print ('\a')

for i in range(5):
    os.system("clear")
    t = input("Time of the session:")
    time.sleep(int(t)*60)
    beep()
    print (random.choice(wikiquote.quotes('Work', lang='en'))) 

