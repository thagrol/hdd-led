#!/usr/bin/env python3

import argparse
import gpiozero
import logging
import time


STATSFILE = '/proc/diskstats'
FIELD = 12


# parse cmdline args
#    Default    Description
# -i 0.05       poll interval
# -g 21         gpio to use
# -l            active low
parser = argparse.ArgumentParser(description='Simple python3 script to monitor /proc/diskstats and flash an LED depending on activity indicated there in.',
                                 epilog='The shorter the poll interval the more responsive the LED will be but more CPU time will be used by the script.'
                                )
parser.add_argument('-i', '--interval',
                    action='store',
                    type=float,
                    default=0.05,
                    help='poll interval in seconds. Default: 0.05'
                   )
parser.add_argument('-g', '--gpio',
                    action='store',
                    type=int,
                    default=21,
                    help='GPIO pin to use. BCM numbering. Default: 21'
                   )
parser.add_argument('-l', '--active_low',
                    action='store_true',
                    default=False,
                    help='GPIO is active when low.'
                   )
parser.add_argument('-d', '--debug',
                    action='store_const',
                    const=logging.DEBUG,
                    default=logging.WARNING,
                    help='enable debug output.'
                   )
args = parser.parse_args()

logging.basicConfig(level=args.debug)
logging.debug(args)

INTERVAL = args.interval
GPIO = args.gpio
ACTIVE_HIGH = not(args.active_low)

led = gpiozero.LED(GPIO,
                   active_high=ACTIVE_HIGH,
                   )

logging.debug('Starting mian polling loop')
while True:
    try:
        with open(STATSFILE,mode='r') as s:
            stats = s.read()
            disc_active = False
        for l in stats.split('\n'):
            try:
                if int(l.split()[FIELD - 1]):
                    disc_active = True
                    break
            except IndexError:
                pass
        led.value = disc_active
        time.sleep(INTERVAL)
    except Exception:
        if args.debug:
            raise
        else:
            logging.exception('')
