# dash-smartthings

## Dash Button IP Address
## Obtain the MAC address of the Dash Button and
## create a DHCP reservation for it on your DHCP Server/router
192.168.2.137

## Server running the xinetd dashproxy service
192.168.2.100

## IP Address to conifgure DDWRT router to forward traffic
## from one dash button to the server
/usr/sbin/iptables -t nat -A PREROUTING -s 192.168.2.137 -p tcp -j DNAT --to 192.168.2.100:9999

## Using the SmartThings web IDE create a SmartApp using the groovy file.
## Create a device in the simulator to obtain an API Token and API Endpoint address
## and add them to the dashproxy.py file
