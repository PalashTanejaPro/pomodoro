#!/usr/bin/env python3
import time
from tinydb import TinyDB
import os
import wikiquote
import random
from datetime import datetime

db = TinyDB('db.json')

def beep():
    print ('\a')
    time.sleep(1)
    print ('\a')
    time.sleep(1)
    print ('\a')

for i in range(5):
    os.system("clear")
    t = input("Time of the session: ")
    start = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    time.sleep(int(t)*60)
    end = datetime.now().strftime('%Y-%m-%d %H:%M:%S')   
    beep()
    print (random.choice(wikiquote.quotes('Work', lang='en'))) 
    log = input("What did you do in this session? ")
    db.insert({'start': str(start), 'end': str(end), 'log': log})

