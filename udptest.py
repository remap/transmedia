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

	hstep = 225.0 / 50.0

	for k in range (0,2):
		for i in range (0,50):
			h.append(i*hstep)
			s.append(0.9)
			l.append(0.75)

	strandPair.setHSLArray(h,s,l)

	raw_input("Press Enter to continue...")

	strandPair.setHSL(0,0,0)	
	time.sleep(0.250)
	kinetsender.stop = True
	kinetsender.complete.wait()			
