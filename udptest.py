from iColorFlex import IColorFlex
from KinetSender import KinetSender
import sys, random, time
import logging
from BeaconLogging import BeaconLogging
from BeaconUDPServer import BeaconUDPServer
import math
from cue import Cue

    
def trans_GO(self): 
	Cue.trans_GO(self)
	self.Ha = 92  #320
	self.Hb = 220  #170
	self.Hc = 200      #40

	sat_mult = 1.5
	bri_mult = 0
	for k in xrange(len(self.lanterns)):
		#for n in xrange(len(lanterns[k])):

		# 'stripes'
		self.lanterns[k].setHSL( self.Ha,0.25*sat_mult,0.75*bri_mult, range(0,34) )
		self.lanterns[k].setHSL( self.Hb,0.35*sat_mult,0.75*bri_mult, range(34,67) )
		self.lanterns[k].setHSL( self.Hc,0.65*sat_mult,0.75*bri_mult, range(67,100) )

		#saturated caps
		self.lanterns[k].setHSL( self.Hc,1*sat_mult,0.75*bri_mult, range(94,100) )
		self.lanterns[k].setHSL( self.Ha,1*sat_mult,0.75*bri_mult, range(0,6) )

		# middle whites
		self.lanterns[k].setHSL( self.Hc,1*sat_mult,1*bri_mult, range(64,70) )
		self.lanterns[k].setHSL( self.Hc,1*sat_mult,1*bri_mult, range(31,37) )

def exec_FADE_IN(self, deltat):
	complete = Cue.exec_FADE_IN(self,deltat)  # this handles transitions for us
	if complete: return complete     
	for L in self.lanterns:
		L.setHSL(None,None,math.log10(1+9*self.p_fi)*0.75, range(0,100,3))
		L.setHSL(None,None,math.log10(1+9*self.p_fi)*0.55, range(1,100,3))
		L.setHSL(None,None,math.log10(1+9*self.p_fi)*0.25, range(2,100,3))
	return False


# Possibly do this asynchronously and then do the update in exec_RUN?
def process_pingback(self, q1, q2, q3, id, iphash):
	log.log(logging.INFO, "TestCue:process_pingback","%0.3f, %0.3f, %0.3f, %i, %s" % (q1, q2, q3, id, iphash))
	for k in xrange(len(self.lanterns)):
		self.lanterns[k].setHSL( 180*0.5*(q1+1),None,None, range(0,34) )
		self.lanterns[k].setHSL( 180*0.5*(q2+1),None,None, range(34,67) )
		self.lanterns[k].setHSL( 180*0.5*(q3+1),None,None, range(67,100) )

def doSet(D):
	log.log(logging.INFO, "TestCue:doSet","%s" % (D))
	for k in xrange(len(self.lanterns)):
		self.lanterns[k].setHSL(float(D['h']), float(D['s']), float(D['l']))
            
    
if __name__ == '__main__':  
    
    log = BeaconLogging("Beacon-beta", "BeaconControlTest", "BeaconControlTest.log", logging.INFO,logging.INFO, None)
    
    
    # Subnet configuration : for test
    #IP Address. . . . . . . . . . . . : 131.179.141.34
	#Subnet Mask . . . . . . . . . . . : 255.255.255.128
 	#Default Gateway . . . . . . . . . : 131.179.141.1
 
    SELF_IP = "131.179.141.34"
    PDS_IP = "131.179.141.127"   # Broadcast on our subnet 
    
    log.log(logging.INFO,"udptest:__main__", "Startup")
    
    strand = IColorFlex(ports=2, portstart=1) 
    
    # Create but don't start the sender so we can fill its first buffer w/color
    # and prevent a drop to black.
    kinetsender = KinetSender(SELF_IP, PDS_IP, 2, 150, log, False)  
    
    kinetsender.addPayloadObject(strand)
        
    # start the thing  (hops to black if we haven't set the payload)
    kinetsender.start()
    
    
    
           
    k = -1     
    
    while (True): 
    	k = k+1 
    	if k == 50: k = 0
        try:
            time.sleep(0.5)  
            strand.setHSL(0,0,0)
            strand.setHSL(k*3, 0.75, 0.75, channels=[k,k+50])
        except KeyboardInterrupt, k:
            break
    
    	
    # Wrap up finish.
    kinetsender.stop = True
    kinetsender.complete.wait()			
    sys.exit(1)