#!/usr/bin/env python

## DD-WRT IPTABLES COMMAND (assumptions: dash button's ip is 192.168.2.137 and the server running the
## xinetd service has an ip of 192.168.2.100)
## /usr/sbin/iptables -t nat -A PREROUTING -s 192.168.2.137 -p tcp -j DNAT --to 192.168.2.100:9999

import requests
import time
from datetime import datetime

timeFile = "/usr/local/bin/lastdashpush.txt"

def toggle_st():
    APITOKEN = "11111111-2222-3333-4444-555555555555"
    API_ENDPOINT = "https://graph.api.smartthings.com/api/smartapps/installations/66666666-7777-8888-9999-000000000000"

    ENDPOINTSUFFIX = "switches"
    url = "%s/%s" % (API_ENDPOINT,ENDPOINTSUFFIX)
    print url
    headers = {"Authorization": "Bearer %s" % APITOKEN}
    data = '{"command":"toggle"}'
    r = requests.put(url, data=data, headers=headers)

f = open(timeFile, 'r')
lastPushTime = f.readline()
f.close
print lastPushTime

timeFormat = "%H:%M:%S"
curTime = time.strftime(timeFormat)
print curTime

tdelta = datetime.strptime(curTime, timeFormat) - datetime.strptime(lastPushTime, timeFormat)
print tdelta

if tdelta.seconds > 10:
   f = open(timeFile, 'w')
   f.write(curTime)
   f.close

   toggle_st()
else:
   print "Wait a bit"

