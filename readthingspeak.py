#!/usr/bin/env python

import thingspeak

channel_id = XXXXXX  # PUT CHANNEL ID HERE
read_key = 'read_apikey' 

# channel = thingspeak.Channel(id=channel_id, api_key=read_key)

# If you want text output instead of json try this
channel = thingspeak.Channel(id=channel_id, api_key=read_key, fmt='txt')

try:
    tsk_conn = channel.get_field_last(field="field1")
    if tsk_conn != None:
        print("ThinkSpeak connection OK")
except:
    raise
    print("ThinkSpeak connection failed")


