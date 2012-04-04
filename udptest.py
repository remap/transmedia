from iColorFlex import IColorFlex
from KinetSender import KinetSender
import sys, random, time
import math


if __name__ == '__main__':  
    
	SELF_IP = "131.179.141.34"
	PDS_IP = "131.179.141.127"   # Broadcast on our subnet 


	strandPair = IColorFlex(ports=2, portstart=1) 
	kinetsender = KinetSender(SELF_IP, PDS_IP, 2, 150, None, False)  

	kinetsender.addPayloadObject(strandPair)

	# start the thing  (hops to black if we haven't set the payload)
	kinetsender.start()

	h = []
	s = []
	l = []

	# HUE RANGE 
	# H = 220 to 340
	
	# AND FOR NOW, 
	# S = 1
	# L = 0.5		
	
	hstep = 120.0 / 50.0  # hues are 0 to 360, this does 0 to 225, stepping through for each light

	for k in range (0,2):
		for i in range (0,50):
			h.append(i*hstep + 220)
			s.append(1)
			l.append(.5)

	strandPair.setHSLArray(h,s,l)

	raw_input("Press Enter to continue...")

	strandPair.setHSL(0,0,0)	
	time.sleep(0.250)
	kinetsender.stop = True
	kinetsender.complete.wait()			
