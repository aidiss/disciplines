#conference.py
"""This gets info about conferences"""

listings = ['grc', 'faseb', 'all_conferences', 'conference_alerts', 'wikicfp']


thedict = [{
	'name':'grc',
	'url': 'https://www.grc.org/meetings.aspx ',
	'disciplines': ['biology', 'chemistry',	'physics'],
	'things available': ['Conference names',
						 'Conference database',
						 'Conference disciplines',
						 'Conference site'],

	'Categories' : [
		'biophisics',
		'astrophysics',
		'atomic physics',
		'biological chemistry',
		'computation',
		'condesned matter phsyics and nanostructures',
		'developmental systems',
		'environment and evolution',
		'inorganic chemistry',
		'instrumentation',
		'materials',
		'microbes and viruses',
		'molecular cell biology',
		'neurobiology',
		'optical physics',
		'organic chemistry',
		'other',
		'pathology',
		'pharmacology and therapeutics',
		'science education',
		'science policy'],
	"'Possibility to show only new meeting's": 'True'},
	
	{'name':'faseb',
	'url': 'http://www.faseb.org/science-research-conferences.aspx',
	'xml': True,
	'xml_url': 'http://www.faseb.org/ListXML.aspx?Type=rss&Content=EventsSRC',
	'structure': ['Title', 'Link', 'Description', 'Startdate'],
	'url1' : 'https://secure.faseb.org/FASEB/meetings/summrconf/selecttopic.aspx'},

	{'name': 'all_conferences',
	'url': 'http://www.allconferences.com/Science/Research',
	'structure': ['Name', 
		'Venue',
		'Location',
		'Logo',
		'Begins',
		'Ends',
		'Description'],

		'Categories':['Arts', 'business', 'computers', 'consumers', 'education', 'geographical', 'health', 'law', 'medical', 'news', 'nursing', 'recreation', 'reference', 'science', 'society']}]

def conference_alerts():
	""" Conference alerts

	http://www.conferencealerts.com/

	By:
		topic, country, city
	"""
	tree = [
	{'Social Sciences and Humanities':
		['Anthropology'	,	
		'Art History',
		'Arts'		,
		'English',
		'History'		,
		'Information science',
		'Interdisciplinary studies'		,
		'Islamic Studies',
		'Language'		,
		'Linguistics',
		'Literature'	,	
		'Local Government',
		'Multidisciplinary Studies'	,	
		'Museums and heritage',
		'Music'		,
		'Occupational Science',
		'Philosophy'	,
		'Poetry',
		'Politics'		,
		'Popular Culture',
		'Psychology'	,	
		'Religious studies',
		'Social Sciences',
		'Sociology',
		"Women's history"]},
	
	{'Interdisciplinary': 
		['Children and Youth',
		'Communications and Media',
		'Complex Systems',
		'Conflict resolution',
		'Creativity	',
		'Culture',
		'Disaster Management',
		'Discourse',
		'Film studies',	
		'GLBT Studies',
		'Gender studies',
		'Globalization',
		'HIV/AIDS'	,
		'Human Rights',
		'Identity',
		'Leadership',
		'Memory',
		'Poverty',
		'Public Policy'	,
		'Security',
		'Sexuality and eroticism',
		'Spirituality',
		'Sport science'	,	
		'Sustainable development',
		'Tourism',
		'Urban studies',
		'Violence',
		"Women's studies"]},
	
	{'Regional Studies':
		['African Studies',	
		'American Studies',
		'Asian Studies',	
		'European Studies']},
	
	{'Mathematics and statistics ':
		['Mathematics',		
		'Statistics']},
	
	{'Business and Economics': 
		['Banking and finance',	
		'Business',
		'Business Ethics',	
		'E-commerce',
		'Economics'	,
		'Human Resources',
		'Management',		
		'Marketing']},

### other part

	{'Physical and life sciences':
		['Agriculture',		
		'Aquaculture',
		'Archaeology',		
		'Astronomy',
		'Biodiversity',		
		'Biology',
		'Chemistry'	,	
		'Earth Sciences',
		'Ecology'		,
		'Environment',
		'GIS'		,
		'Genetics',
		'Meteorology'	,	
		'Oceanography',
		'Physics'		,
		'Soil',
		'Waste Management'	,	
		'Water']},

	{'Engineering and Technology  ':[
		'Architecture',
		'Artificial Intelligence',
		'Bioinformatics',
		'Biomedical Engineering',
		'Biotechnology',
		'Computer software and applications',
		'Computing'
		'Data Mining',
		'Design',
		'Energy',
		'Engineering'	,	
		'Forestry',
		'Image Processing'	,	
		'Information Technology',
		'Internet and World Wide Web'	,	
		'Manufacturing',
		'Military',
		'Mining',
		'Nanotechnology and Smart Materials	',	
		'Networking',
		'Polymers and Plastics'	,	
		'Renewable Energy',
		'Robotics',
		'Space Environment and Aviation Technology',
		'Systems Engineering',
		'Transport']},

	{'Education' : [
		'Distance Education	',	
		'E-learning',
		'Higher Education'	,	
		'Lifelong Learning',
		'Teaching and Learning	']},

	{'Law'  :[
		'Justice and legal studies']},

	{'Health and Medicine':[
		'Alternative Health',	
		'Cardiology',
		'Dentistry',
		'Dermatology',
		'Disability and Rehabilitation	'	,
		'Family Medicine',
		'Food Safety',
		'Gastroenterology',
		'Gerontology'	
		'Health',
		'Infectious diseases',		
		'Medical ethics',
		'Medicine and Medical Science'	,	
		'Neurology',
		'Nursing',
		'Nutrition and Dietetics',
		'Oncology',
		'Palliative Care',
		'Psychiatry'	,	
		'Public Health',
		'Radiology',
		"Reproductive Medicine and Women's Health",
		'Social Work',
		'Surgery']},

	{'Animal Sciences':['Veterinary Science']}]

def wikicfp():
	url = 'http://www.wikicfp.com/cfp/call?conference=databases'
	return