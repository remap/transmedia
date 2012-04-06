# runtime params

# debug param for testing data w/o lighting
# set to true, to send to light
light = False

# in seconds:
categoryWait = 0
yearWait = 3.0


xfTime = 3.0     # seconds for crossfade
xfStep = 0.005 # seconds per step in xf


SELF_IP = "131.179.141.34"
PDS_IP = "131.179.141.127"   # Broadcast on our subnet


# verbose data attributes below

# for GDP from 2005 to 2010
inflationFactor = 1.1068

dataFile = "data/cs_v6.csv"

years = ['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010']

categories = [
			'Advertising, market research and public opinion polling',
			'Research and Development',
			'Architectural, engineering and other technical services',
			'Personal, cultural and recreational services']
# commenting these out, as they're usually blank, and they are subset of above 'personal...' category
#			'Audiovisual and related services',
#			'Other other personal, cultural and recreational services']


# first four categories only
categorydescriptions = [
			'Advertising and market research services transacted between residents and non-residents cover the design, creation and marketing of advertisements by advertising agencies; media placement, including the purchase and sale of advertising space; exhibition services provided by trade fairs; the promotion of products abroad; market research; and public opinion polling abroad on various issues.',
			'Architectural, engineering and other technical services cover resident and non-resident transactions related to architectural design of urban and other development projects; planning and project design and supervision of dams, bridges, airports, turnkey projects, etc.; surveying, cartography, product testing and certification, and technical inspection services.',
			'Research and development services cover those services that are transacted between residents and non-residents and associated with basic research, applied research, and experimental development of new products and processes. In principle, such activities in the sciences, social sciences and humanities are covered; included is the development of operating systems that represent technological advances.',
			'Personal, cultural, and recreational services involving transactions between residents and non-residents are subdivided into two categories: (a) Audiovisual and related services, which comprises services and associated fees related to the production of motion pictures (on film or video tape), radio and television programs (live or on tape), and musical recordings. Included are receipts or payments for rentals; fees received by resident actors, directors, producers, etc. (or by non-residents in the compiling economy) for productions abroad; and fees for distribution rights sold to the media for a limited number of showings in specified areas. Fees to actors, producers, etc. involved with theatrical and musical productions, sporting events, circuses, etc. and fees for distribution rights (for television, radio, etc.) for these activities are included. (b) other personal, cultural and recreational services, which comprises other personal, cultural, and recreational services such as those associated with museums, libraries, archives, and other cultural, sporting, and recreational activities. Also included are fees for services, including provision of correspondence courses, rendered abroad by teachers or doctors.'			
			]

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