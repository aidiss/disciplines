#Teaching_academic_writing.py

'''Figure 3.1 A categorisation of disciplines and their typical written texts'''
columns = ('Sciences', 'Social Sciences', 'Humanities/Arts', 'Applied Disciplines')
table = {
	'Examples include': (
		('physics', 'chemistry', 'biology', 'geology'),       
		('sociology',  'geography', 'economics', 'politics', 'cultural and media studies',  'psychology'),
		('English', 'history',  'languages', 'classics', 'fine art', 'religious studies', 'nursing'),               
		('business and management', 'philosophy', 'music', 'engineering', 'health and social welfare')),
	            
	'Typical text types': (
		('laboratory reports', 'project proposals and reports', 'fieldwork notes', 'essays', 'dissertations'),
		('essays', 'project reports', 'fieldwork notes', 'dissertations' ),
		('essays', 'critical analysis', 'translations', 'projects'),
		('essays', 'case studies', 'dissertations', 'projects'))}

from pprint import pprint
pprint(table.keys())
pprint(table.values
	())

