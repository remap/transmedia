import config
import csv
import math
from time import time, sleep 
import sys
from iColorFlex import IColorFlex
from KinetSender import KinetSender
from decimal import *

# floating point precision (to avoid scientific notation in output)
getcontext().prec = 18


csv.register_dialect('custom',
                     delimiter=',',
                     doublequote=True,
                     escapechar=None,
                     quotechar='"',
                     quoting=csv.QUOTE_MINIMAL,
                     skipinitialspace=True)

def buildCountries(year, category):
	print  ("building countries for ",  year, category)
    # build countries
	ifile = open(config.dataFile, "rU") 
	#data = csv.reader(ifile, dialect='custom')
	data = csv.DictReader(ifile, dialect='custom')
	gdpName =0
	catName = 0
	gdpVal = 0
	catVal = 0
	countries=[]
	for row in data:
		if(row['CATEGORY']==category):
			#print row['COUNTRY'] +" : "+row[year]
			catVal = row[year]
			catName = row['COUNTRY']
		if(row['CATEGORY']=="GDP Per Capita"):
			#print row['COUNTRY'] +" : "+row[year]
			gdpPPPVal = row[year]
			gdpPPPName = row['COUNTRY']
			#print row
		if(row['CATEGORY']=="GDP"):
			#print row['COUNTRY'] +" : "+row[year]
			gdpVal = row[year]
			gdpName = row['COUNTRY']
			#print row
		#now we've accumulated all necessary variables per-country... let's build the country list element:
		if(gdpName == catName and gdpName != 0):
			countries.append({'name':gdpName,'year':year, 'category':category, 'catValue': catVal,  'gdpValue': gdpVal, 'gdpPPPValue': gdpPPPVal, 'catGDP':makeCatGDPRatio(catVal,gdpVal), 'catGDPPPP':makeCatGDPPPPRatio(catVal,gdpPPPVal)})
			gdpName = catName = 0
	#print countries
	sys.exit(1)
	return countries

# this returns value for category : gdp per capita
# ie dollar amount of creative economy per person
def makeCatGDPPPPRatio(catVal, gdpPPPVal):
    #note GDP PPP value is in dollars, and the categories are in millions
    #so we just make everything dollars:
    # and GDP is in 2005, but other values in 2010, so we adjust for inflation
    ratio = ((float(catVal)*1000000)/(float(gdpPPPVal)*float(config.inflationFactor)))
    return ratio

# this returns value for category : gdp total
# ie percentage of GDP that is creative economy
def makeCatGDPRatio(catVal, gdpVal):
    #note GDP value is in billions, and the categories are in millions
    #so we just make everything dollars
    #and GDP is in 2005, but other values in 2010, so we adjust for inflation
    ratio = ((Decimal(catVal)*1000000)/(Decimal(gdpVal)*1000000000*Decimal(config.inflationFactor)))
    if(ratio == 0):
		ratio = 0
    print ratio
    return ratio

#any other derived methods should be placed here, and referred to above in 'buildcountry' list assignment, ie:

#def anotherAlgorithm(catVal, gdpVal):


# JB 
# 
def timedFade (xfTime, period, callback, cbargs):     
    tStart = time()
    t = tStart # ensure we start at 0 
    while (t < tStart + xfTime):        
        alpha = (t-tStart) / xfTime
        callback(alpha, cbargs)
        sleep(period) 
        t = time()               
    callback(1, cbargs) # ensure we finish at 1    


#
#  Value to light calculation
#
def updateLights( A, values ):   # A from 0..1;  assume values same size array
	V = []
	for i in range(0,len(values[0])):
		V.append(  (1-A)*float(values[0][i]['catGDP']) + A*float(values[1][i]['catGDP']) )
	h = []
	s = []
	l = []	
	for S in range(0,2):   # two strands per pair, fill them with the same thing
		for i in range(0,len(V)): 
			if V[i]==0:
				h.append(0)
				s.append(0.35)
				l.append(0.5)						
			else: 				
				h.append(V[i])
				s.append(0.35 + math.log10(V[i])/6)
				l.append(0.5)
			#print h[i],s[i],l[i], V[i], values[1][i]['name']
	if(config.light):
		strandPair.setHSLArray(h,s,l) 

 
# updateCountries
# triggers the crossfade every config.yearWait
#
lastCountries = [{'name':0,'year':0, 'category':0, 'catValue': 0,  'gdpValue': 0, 'gdpPPPValue':0, 'catGDP':0, 'catGDPPPP':0} for x in range(0,50)]

def updateCountries(catID, yearID, countries):
    global lastCountries 
    print "Fading to:", config.categories[catID], config.years[yearID]
    timedFade( config.xfTime, config.xfStep, updateLights, [lastCountries, countries])
    lastCountries = countries
#
# end JB
    
    
def mainLoop():
    catID = 0
    yearID = 0
    while(True):  # Run forever
        for cat in config.categories:
            sleep(config.categoryWait)
            for year in config.years:
                sleep(config.yearWait)
                updateCountries(config.categories.index(cat), config.years.index(year),buildCountries(year, cat))
            
         
if __name__ == "__main__":
	#Network configuration : for production system 
	#IP Address. . . . . . . . . . . . : 131.179.141.34
	#Subnet Mask . . . . . . . . . . . : 255.255.255.128
	#Default Gateway . . . . . . . . . : 131.179.141.1

	# Set up a single icolorflex sender 
	# and broadcast it to all strands
	#
	if(config.light):
		strandPair = IColorFlex(2) 
		kinetsender = KinetSender(config.SELF_IP, config.PDS_IP, 2, 150, None, False)  
		kinetsender.addPayloadObject(strandPair)
		strandPair.setHSL(0,0,0)  # Set initial payload to black
		kinetsender.start()
    
	print("generating values for lighting from GDP")
	mainLoop()
    
	# Wrap up finish.
	# TODO: Don't get here currently because we don't have a clean break
	kinetsender.stop = True
	kinetsender.complete.wait()			    
	    


	    
	    	
	
