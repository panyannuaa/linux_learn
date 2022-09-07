#!/usr/bin/env python3

import signal
import sys
import time

def signal_handler(sig, frame):
    print(sig)
    #print(type(sig))
    print('You pressed Ctrl+C!')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C')
signal.pause()



