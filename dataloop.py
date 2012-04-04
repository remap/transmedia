import config
import csv
import time

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
    with open(config.dataFile, "rU") as ifile:
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
                gdpVal = row[year]
                gdpName = row['COUNTRY']
                #print row
            #now we've accumulated all necessary variables per-country... let's build the country list element:
            if(gdpName == catName and gdpName != 0):
                countries.append({'name':gdpName,'year':year, 'category':category, 'catValue': catVal,  'gdpValue': gdpVal, 'catGDP':makeCatGDPRatio(catVal,gdpVal)})
                gdpName = catName = 0
        return countries
                

def makeCatGDPRatio(catVal, gdpVal):
    #note GDP value is in dollars, and the categories are in millions
    #so we just make everything dollars:
    # and GDP is in 2005, but other values in 2010, so we adjust for inflation
    ratio = ((float(catVal)*1000000)/(float(gdpVal)*float(config.inflationFactor)))
    return ratio

#any other derived methods should be placed here, and referred to above in 'buildcountry' list assignment, ie:

#def anotherAlgorithm(catVal, gdpVal):


# JB 
# 
def timedFade (xfTime, period, callback, cbargs):     
    from time import time, sleep 
    tStart = time()
    t = tStart # ensure we start at 0 
    while (t < tStart + xfTime):        
        alpha = (t-tStart) / xfTime
        callback(alpha, cbargs)
        sleep(period) 
        t = time()               
    callback(1, cbargs) # ensure we finish at 1    
   
def updateLights( A, values ):   # A from 0..1;  assume values same size array
    print "---", A, 1-A
    for i in range(0,len(values[0])):
        print values[1][i]['name'], (1-A)*values[0][i]['catGDP'] + A*values[1][i]['catGDP']
    
lastCountries = [{'name':0,'year':0, 'category':0, 'catValue': 0,  'gdpValue': 0, 'catGDP':0} for x in range(0,50)]
xfTime = 4     # seconds
xfStep = 0.010 # seconds
def updateCountries(catID, yearID, countries):
    global lastCountries 
    print "    catID: ", config.categories[catID]
    print "   yearID: ", config.years[yearID]
    print "firstlist: ", countries[0]
    print "trade PPP: ", countries[0]['catGDP']  # this is the ratio! 
    timedFade( xfTime, xfStep, updateLights, [lastCountries, countries])
    lastCountries = countries
#
# end JB
    
    
def mainLoop():
    catID = 0
    yearID = 0
    while(True):
        for cat in config.categories:
            time.sleep(config.categoryWait)
            for year in config.years:
                time.sleep(config.yearWait)
                updateCountries(config.categories.index(cat), config.years.index(year),buildCountries(year, cat))
            
            
if __name__ == "__main__":
    print("generating values for lighting from GDP")
    mainLoop()