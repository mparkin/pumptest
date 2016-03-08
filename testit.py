#! /usr/bin/python

import serial
import telnetlib as Tnet
import time
loop = 10
Hostaddress = "192.168.0.110"
try:
    tn=Tnet.Telnet(Hostaddress,23, timeout = 1)
except:
    raise Error("No Connect")
tn.set_debuglevel(5)
print "pc init"   
#try:
#    tn.write("vt100\n")
#except:
#    raise Error("No Write")
#time.sleep(1)
#data = tn.read_very_eager()
try:
    tn.write("G")
except:
    raise Error("No Write")
time.sleep(1)
data = tn.read_very_eager()
while loop >0:
    tn.write("X")
    time.sleep(1)
    data = tn.read_very_eager()
    print(data)
tn.close()



