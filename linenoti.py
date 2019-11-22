import requests
import datetime

from readthingspeak import *

url = 'https://notify-api.line.me/api/notify'
token = 'yourtoken' # yourtoken here
headers = {'content-type': 'application/x-www-form-urlencoded',
            'Authorization': 'Bearer '+token}

def alert_info():
    now = datetime.datetime.now()
    t = datetime.time(now.hour, now.minute)

    # Read water level from ThingSpeak
    pond_level = channel.get_field_last(field="field1")
    tank_level = channel.get_field_last(field="field2")

    # notify water level info
    msg = '\n' + str(t) + \
        '\n' 'pond_level is ' + str(pond_level) + \
        '\n' + 'tank_level is ' + str(tank_level)
    r = requests.post(url, headers=headers, data={'message': msg})
