#!/usr/bin/env python
# coding: utf8

import Skype4Py
import time
import sys
import signal

skype = Skype4Py.Skype()
skype.Attach()

def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)


while True:
    try:
        signal.signal(signal.SIGINT, signal_handler)
        today = time.strftime("%Y%m%d")
        skype.Profile('BIRTHDAY', Set=unicode(today))
        time.sleep(3600)
    except (KeyboardInterrupt, SystemExit):
        sys.exit(0)
