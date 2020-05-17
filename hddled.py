#!/usr/bin/env python3

import gpiozero
import time

STATSFILE = '/proc/diskstats'
FIELD = 12
INTERVAL = 0.01
GPIO = 21
ACTIVE_HIGH = True

led = gpiozero.LED(GPIO,
                   active_high=ACTIVE_HIGH,
                   )

try:
    while True:
        with open(STATSFILE,mode='r') as s:
            stats = s.read()
            ios = 0
        for l in stats.split('\n'):
            try:
                ios = ios + int(l.split()[FIELD - 1]) # split is 0 indexed
            except IndexError:
                pass
        led.value = ios
        time.sleep(INTERVAL)
except Exception:
    pass
