#!  /usr/bin/python
 
import datetime
import serial
import sys

class SensorRead():
    data = "none "
    filename = " "
    ser = 0
    time = 500
    def open(self,filename):
        self.ser = serial.Serial('/dev/ttyACM0',38400)
        self.filename = "{0}_{1}.csv".format(filename,datetime.datetime.now().strftime('%d%m%y_%H%M%S'))

    def getData(self):
	self.data = self.ser.readline()

    def setPeriod(self,newtime):
	if newtime:
	   self.time = newtime
	t = "T"+self.time
	print t
	self.ser.write(t);

    def writeData(self,value):
        f = open(self.filename, "a");
        print self.data
	print datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S.%f')[:-3]
	f.write("{0},{1},{2}".format(datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S.%f')[:-3],value,self.data))
        f.close()

    
    def close(self):
        self.ser.close()
    

if __name__ == '__main__':
	tst = SensorRead()
	tst.open("test")
 	tst.setPeriod(raw_input("Period : "))       
       	while(1):
	    while(1):
	        try:
                    tst.getData()
                    tst.writeData()
	        except KeyboardInterrupt:
		    break
	    tst.setPeriod(raw_input("Period (ms): "))
	tst.close()
	
