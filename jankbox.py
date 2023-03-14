#!/usr/bin/env python3

# IMPORTS
##################################
from pygame import mixer
from pathlib import Path
import os
import sys
from sys import exit
import signal
import time
import readline
##################################

os.system('clear')
base = os.path.expanduser('Music')


# Banner created here: http://patorjk.com/software/taag/#p=display&f=Graffiti&t=jankbox
BANNER = r"""

     __               __   ___.                 
    |__|____    ____ |  | _\_ |__   _______  ___
    |  \__  \  /    \|  |/ /| __ \ /  _ \  \/  /
    |  |/ __ \|   |  \    < | \_\ (  <_> >    < 
/\__|  (____  /___|  /__|_ \|___  /\____/__/\_ \
\______|    \/     \/     \/    \/            \/

   jankbox - the jankiest music player, ever?

"""
print(BANNER)

DIRS = ['Music', 'Songs', 'Jams']

def complete(text, state):
    for cmd in DIRS:
        if cmd.startswith(text):
            if not state:
                return cmd
            else:
                state -= 1

readline.parse_and_bind("tab: complete")
readline.set_completer(complete)

def player():
    music_dir = Path(str(input("Music libary: ")))
    types = ('*.mp3') #['*.mp3', '*.flac', '*.aac', '*.wav', '*.ogg']
    #plist = 
    dir_list = os.listdir(music_dir) 
    mixer.init()
    
    for fp in music_dir.glob(str(types)):
          mixer.music.load(str(fp))
          mixer.music.play()
          while mixer.music.get_busy():
                time.sleep(1)

def sigint_handler(signal, frame):
    print ('\nQuitting\n')
    print ('\nLong Live Jankbox\n')
    sys.exit(0)
signal.signal(signal.SIGINT, sigint_handler)

player()

