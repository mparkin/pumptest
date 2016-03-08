#! /usr/bin/python

import serial
import telnetlib as Tnet
import time

Hostaddress = "192.168.0.110"

class pumpControl():

    Hostaddress = "192.168.0.110"
    tn=Tnet.Telnet() 
    print "pc init"  
    data = "" 
    debug = False
    tn.set_debuglevel(5)
    def ComInit(self,address):
        self.Hostaddress = address
	print self.Hostaddress
        self.tn.open(self.Hostaddress,23)

    def init(self):
	self.tn.write("I\n")
        self.readit()

    def speed(self,nspeed):
	self.write_data("S",str(nspeed))

    def fast(self,nspeed):
	self.write_data("F",str(nspeed))

    def radian(self,count):
	self.write_data("R",str(count))

    def winding(self,count):
	self.write_data("W",str(count))

    def duration(self,count):
	self.write_data("D",str(count))

    def turn(self,turns):
	self.tn.write("L\n")

    def timed(self,turns):
	self.tn.write("T\n")

    def home(self,turns):
	self.tn.write("H\n")

    def direction(self,dir):
 	if dir == 'C':
	    self.tn.write("C\n")
        else:
            self.tn.write("A\n")
        self.readit()

    def normal(self):
	self.tn.write("N\n")
        self.readit()

    def pulse(self):
	self.tn.write("P\n")
        self.readit()

    def brake(self,dir):
 	if dir == 'B':
	    self.tn.write("B\n")
        else:
            self.tn.write("U\n")
        self.readit()

    def stop(self):
	self.tn.write("E\n")
        self.readit()

    def start(self):
	self.tn.write("G\n")
        self.readit()

    def quit(self):
	self.tn.write("Z\n")
        self.readit()

    def info(self):
	self.tn.write("X\n")
        self.readit()

    def readit(self):
        time.sleep(1)
	self.data = self.tn.read_very_eager()
	if self.debug:
            print(self.data)

    def velocity(self,settings):
	self.write_data("V",settings)
        self.readit()

    def timing(self,settings):
	self.write_data("Q",settings)
        self.readit()

    def write_data(self,command,data):
	strings = [command,data]
        #print '\n'.join(strings)
	self.tn.write('\n'.join(strings))
        self.readit()

def runit():
    p = pumpControl()
    p.debug = True
    p.ComInit("192.168.0.110")
    p.info()
    p.quit()


if __name__ == '__main__':
    runit()
