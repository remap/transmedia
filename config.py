# runtime params

# debug param for testing data w/o lighting
# set to true, to send to light
light = False

# in seconds:
categoryWait = 0
yearWait = 3


xfTime = 3.0     # seconds for crossfade
xfStep = 0.005 # seconds per step in xf


SELF_IP = "131.179.141.34"
PDS_IP = "131.179.141.127"   # Broadcast on our subnet


# verbose data attributes below

# for GDP from 2005 to 2010
inflationFactor = 1.1068

dataFile = "data/cs_v6.csv"

years = ['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010']

categories = ['Advertising, market research and public opinion polling',
			'Research and Development',
			'Architectural, engineering and other technical services',
			'Personal, cultural and recreational services']
# commenting these out, as they're usually blank, and they are subset of above 'personal...' category
#			'Audiovisual and related services',
#			'Other other personal, cultural and recreational services']

countries = ['Norway',
			'Ireland',
			'United States',
			'Sweden',
			'Australia',
			'Finland',
			'United Kingdom',
			'Belgium',
			'Japan',
			'Canada',
			'Germany',
			'France',
			'Italy',
			'Singapore',
			'Hong Kong',
			'Spain',
			'Greece',
			'Portugal',
			'South Korea',
			'Cyprus',
			'Malta',
			'Slovakia',
			'Czech Republic',
			'Hungary',
			'Croatia',
			'Mexico',
			'Lithuania',
			'Latvia',
			'Turkey',
			'Russian Federation',
			'Argentina',
			'Costa Rica',
			'Brazil',
			'Romania',
			'Bulgaria',
			'Colombia',
			'Kazakhstan',
			'Fiji',
			'Macedonia',
			'China',
			'Ukraine',
			'Egypt',
			'Philippines',
			'Senegal',
			'India',
			'Pakistan',
			'Kenya',
			'Kyrgyzstan',
			'Bangladesh',
			'Ethiopia']