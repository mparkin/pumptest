#! /usr/bin/python


import datetime
import serial
import pump
import senscollect
import time

flowrate = 205
FastFlow = 3500
T1 = 0.15
T2 = 0.30
T3 = 0.40
T4 = 0.55
T5 = 0.70
S1 = .25
S2 = .50
S3 = 1.00
S4 = .5
S5 = .25
r_change = [171,173,175,177,179]
#f_change = [171,173,175,177,179]
Radians = 175 
Sampleperiod = 60000
SampleRate = 50
#do not change from here
ppump = pump.pumpControl()
flow = senscollect.SensorRead()	
ppump.ComInit("192.168.0.101")
#end do not change
flow.open("runData")
flow.setPeriod(str(SampleRate))
ppump.init()
ppump.radian(Radians)
ppump.speed(flowrate)
ppump.fast(FastFlow)
ppump.velocity(str(S1)+","+str(S2)+","+str(S3)+","+str(S4)+","+str(S5)+","+str(S5))
ppump.timing(str(T1)+","+str(T2)+","+str(T3)+","+str(T4)+","+str(T5))
ppump.start()
#Change Here 
for i, val in enumerate(r_change): #change to f_change
    timeout = Sampleperiod
    ppump.radian(val) #comment this with "#" in front of ppump to do fast change values
   # ppump.fast(val)  #remove "#" in front to change fastspeed value
    while timeout >0:
        try:
            flow.getData()
            flow.writeData(val)
        except KeyboardInterrupt:
 	    break
        time.sleep(SampleRate*.001)
	timeout = timeout - SampleRate
ppump.stop()	
ppump.quit()
flow.close()
