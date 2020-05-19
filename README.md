Simple python3 script to monitor /proc/diskstats and flash an LED depending on activity indicated there in.

Requires gpiozero (sudo apt install pyton3-gpiozero)

    usage: hddled.py [-h] [-i INTERVAL] [-g GPIO] [-l] [-d]

    optional arguments:
      -h, --help            show this help message and exit
      -i INTERVAL, --interval INTERVAL
                            poll interval in seconds. Default: 0.05
      -g GPIO, --gpio GPIO  GPIO pin to use. BCM numbering. Default: 21
      -l, --active_low      GPIO is active when low.
  -d, --debug           enable debug output.
  
The shorter the poll interval the more responsive the LED will be but more CPU time will be used by the script.
Responsiveness will also drop on a heavily loaded system.
