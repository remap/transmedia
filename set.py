# uses 
# http://code.google.com/p/python-colormath/w/list

import sys, socket, random, math, time
from colormath.color_objects import HSLColor
from ctypes import *

# KINET Tier 1 Protocol spec 7/6/2009
class KINETDMXOut(LittleEndianStructure): 
	_fields_ = [("magic", c_ulong), 
				("version", c_short), 
				("type", c_short), 
				("seqnum", c_int),
		       	("port", c_ubyte), 
		       	("flags", c_ubyte), 
		       	("timerval", c_short), 
		       	("universe", c_int),
		       	("dmxstart", c_ubyte), 
		       	("payload", c_ubyte * 511)]
	def __init__(self): 
		self.magic = 0x4ADC0104
		self.version = 0x0002
		self.type = 0x0101
		self.universe = 0xFFFFFFFF
	def setall(self, R, G, B):
		for i in range(0, 510, 3):
			self.payload[i]=R
			self.payload[i+1]=G
			self.payload[i+2]=B
	def settest(self, R,G,B):
		for i in range(0, 510, 3):
			self.payload[i]=min(int((R+1)*random.uniform(0.9, 1.1)), 255)
			self.payload[i+1]=min(int((G+1)*random.uniform(0.9, 1.1)), 255)
			self.payload[i+2]=min(int((B+1)*random.uniform(0.9, 1.1)), 255)

class KINETPortOut(LittleEndianStructure): 
	_fields_ = [("magic", c_int), 
				("version", c_short), 
				("type", c_short), 
				("seqnum", c_int),
		       	("universe", c_int),
		       	("port", c_ubyte), 
		       	("pad", c_ubyte), 
		       	("flags", c_short), 
		       	("length", c_short), 
		       	("startcode", c_short),
		       	("payload", c_ubyte * 512)]
	def __init__(self): 
		self.magic = 0x4ADC0104
		self.version = 0x0002
		self.type = 0x0108
		self.universe = 0xFFFFFFFF
		self.seqnum = 0x0000
		self.universe = 0xFFFFFFFF
		self.length=512  # probably could do this dynamically
		self.startcode = 0x0FFF		
	def setall(self, R, G, B):
		for i in range(0, 510, 3):
			self.payload[i]=R
			self.payload[i+1]=G
			self.payload[i+2]=B
	def settest(self, R,G,B):
		for i in range(0, 510, 3):
			self.payload[i]=int(random.uniform(0.8,1.1)*R)
			self.payload[i+1]=int(random.uniform(0.8,1.1)*G)
			self.payload[i+2]=int(random.uniform(0.8,1.1)*B)
	def rampall(self, R,G,B):
		for i in range(0, 510, 3):
			self.payload[i]=R*int(i)
			self.payload[i+1]=G*int(i)
			self.payload[i+2]=B*int(i)

class KINETSyncOut(LittleEndianStructure): 
	_fields_ = [("magic", c_int), 
				("version", c_short), 
				("type", c_short), 
				("seqnum", c_int),
		       	("pad", c_int)]
	def __init__(self): 
		self.magic = 0x4ADC0104
		self.version = 0x0002
		self.type = 0x0108
		self.seqnum = 0x0000
		
def main():	
	target = sys.argv[1]   # target IP
	(R,G,B) = (int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
	print "Setting target %s to R=%i G=%i B=%i" % (target, R,G,B)	
	S = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

	packet1 = KINETPortOut()
	packet2 = KINETPortOut()

	while(True):
		for H in range(0,360):
			#print H
			time.sleep (.001)
			packet1.port = 0x01
			for i in range(0,50,2):
				hsl = HSLColor(H,.5+.5/360,float(i)/100.0)
				rgb = hsl.convert_to('rgb')
				packet1.payload[3*i] = rgb.rgb_r
				packet1.payload[3*i+1] = rgb.rgb_g
				packet1.payload[3*i+2] = rgb.rgb_b

			packet2.port = 0x02
			for i in range(0,50,2):
				hsl = HSLColor(H,.5,float(i)/100.0+.5)
				rgb = hsl.convert_to('rgb')
				packet2.payload[3*i] = rgb.rgb_r
				packet2.payload[3*i+1] = rgb.rgb_g
				packet2.payload[3*i+2] = rgb.rgb_b

			for i in range(1,49,2):
				hsl = HSLColor(H+50,.5,float(i)/100.0)
				rgb = hsl.convert_to('rgb')
				packet1.payload[3*i] = rgb.rgb_r
				packet1.payload[3*i+1] = rgb.rgb_g
				packet1.payload[3*i+2] = rgb.rgb_b

			for i in range(1,49,2):
				hsl = HSLColor(H+50,.5+.5/360,float(i)/100.0+.5)
				rgb = hsl.convert_to('rgb')
				packet2.payload[3*i] = rgb.rgb_r
				packet2.payload[3*i+1] = rgb.rgb_g
				packet2.payload[3*i+2] = rgb.rgb_b

			N = int(random.uniform(0,49))
			packet2.payload[3*N] = 255
			packet2.payload[3*N+1] = 100
			packet2.payload[3*N+2] = 100

			packet1.payload[3*N] = 255
			packet1.payload[3*N+1] = 100
			packet1.payload[3*N+2] = 100

			S.sendto(packet1, (target, 6038));
			S.sendto(packet2, (target, 6038));

			syncpacket = KINETSyncOut()
			S.sendto(syncpacket, (target, 6038));

	S.close

if __name__ == "__main__":
    main()
