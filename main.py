# !/usr/local/bin/python
# -*- coding: utf-8 -*-

import requests
import datetime
from time import sleep

from readthingspeak import *
from tank import *
from linenoti import *
from pumpctrl import *


# loop while
while True:
    now = datetime.datetime.now()
    t = datetime.time(now.hour, now.minute)

    # Read water level from ThingSpeak
    pond_level = channel.get_field_last(field="field1")
    tank_level = channel.get_field_last(field="field2")

    # display water level info
    print('\n' + 'at ' + str(t) + '\n' + 'pond_level is ' + \
        str(pond_level) + '\n' + 'tank_level is ' + str(tank_level))

    # send alert
    alert_info()

    # condition checking
    tank_level = int(tank_level)
    pond_level = int(pond_level)

    if tank_level >= 80:
        msg = 'Almost full tank'
        r = requests.post(url, headers=headers, data={'message': msg})
        # continue
    elif tank_level >= 50:
        msg = 'more than 1/2 tank'
        r = requests.post(url, headers=headers, data={'message': msg})
        # continue
    elif tank_level >= 25:
        msg = 'quiet low'
        r = requests.post(url, headers=headers, data={'message': msg})
        if pond_level >= 8:
            msg = 'start pump 5 mins'
            r = requests.post(url, headers=headers, data={'message': msg})
            pt = 300
        elif pond_level >= 5:
            msg = 'start pump 5 mins'
            r = requests.post(url, headers=headers, data={'message': msg})
            pt = 300
        elif pond_level >= 2:
            msg = 'start pump 2 mins'
            r = requests.post(url, headers=headers, data={'message': msg})
            pt = 120
        else:
            msg = 'pond water not enough'
            r = requests.post(url, headers=headers, data={'message': msg})
            pt = 0
    else:
        if pond_level >= 8:
            msg = 'start pump 10 mins'
            r = requests.post(url, headers=headers, data={'message': msg})
            pt = 600
        elif pond_level >= 5:
            msg = 'start pump 5 mins'
            r = requests.post(url, headers=headers, data={'message': msg})
            pt = 300
        elif pond_level >= 2:
            msg = 'start pump 2 mins'
            r = requests.post(url, headers=headers, data={'message': msg})
            pt = 120
        else:
            msg = 'pond water not enough'
            r = requests.post(url, headers=headers, data={'message': msg})
            pt = 0

    if pt > 0:
        print(pt)
        relayon()
    else:
        print('wait a moment')

    update_tank()
    sleep(7200)

# END of main
