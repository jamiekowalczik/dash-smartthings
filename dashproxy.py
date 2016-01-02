#!/usr/bin/env python

## DD-WRT IPTABLES COMMAND (assumptions: dash button's ip is 192.168.2.137 and the server running the
## xinetd service has an ip of 192.168.2.100)
## /usr/sbin/iptables -t nat -A PREROUTING -s 192.168.2.137 -p tcp -j DNAT --to 192.168.2.100:9999

import requests
import time
from datetime import datetime

#APITOKEN = "0f5e91a5-69c0-49b8-a9c2-d9547edd2480"
APITOKEN = "6bc6dd37-ae99-4bd8-92be-09191574d3ad"
#API_ENDPOINT = "https://graph.api.smartthings.com/api/smartapps/installations/ac728ae7-b89d-418d-b26e-ff4cbc951b63"
API_ENDPOINT = "https://graph.api.smartthings.com/api/smartapps/installations/c8b195b0-2679-4dc1-886f-97595c0860fb"
timeFile = "/usr/local/bin/lastdashpush.txt"

def toggle_st():
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

