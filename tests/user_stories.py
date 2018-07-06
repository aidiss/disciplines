class Tester_robot(object):
	"""docstring for Tester_robot"""
	def __init__(self, name= None, discipline = None):
		super(Tester_robot, self).__init__()
		self.name = name
		self.discipline = discipline

TESTERS_WITH_BEHAVIOUR = {
	'John': {'discipline': 'Scientometrics'},
	'Fleck': {'discipline': 'Philosophy of science'},
	'Merton': {'discipline': 'Sociology of science'},
	'Historian': {'discipline': 'history of science'},
	'Jeila': {'discipline': 'STS scholar'}}

John = Tester_robot(name='John', discipline='Scientometrics')
Fleck = Tester_robot(name='Fleck', discipline='Philosophy of science')
Merton = Tester_robot(name='Merton', discipline='Sociology of science')
Historian = Tester_robot(name='Historian', discipline='history of science')
Historian = Tester_robot(name='Jeila', discipline='STS scholar')




'Meet John John. John John is second year student and some university.'
'He got interested in science studies. He had to do a study that requires data about researchers.'
'Using disciplinary aspect might be interesting, he thought, therefore he decided to look into this aspect.'
'He googled for some'


'Meet, Jim. Jim is a doctoral student studying in Portugal. Over his studies he did obtain a lot of data regarding his research.'
'Currently his data is a mess of spreadsheets, word documents, drafts and collection of articles. he thought of that he could organize this whole data into something.'
'He was contacted by AA through mailing list, the offer was, to help him to manage data.'


'I am student of scientometrics, having access to data and formal implementations of theories is very important to me.'

'''
#I am DATA SEEKER type of user I want this package to retrieve data.
disciplines.theory.data.sources()

#I would like to implement my thoughts and my articles into the system.
#I am IMPLEMENTER I like theory to be implemented in a formal way.
disciplines.theory.implement()

#I am COLLABORATOR, I want software that will enable me to efficiently share data.
disciplines.share()
disciplines.publish()

#I am teaching Science studies, I would like my students to have efficient access to data, theories and work together.
disciplines.download()
disciplines.list_data()
disciplines.list_theories()
disciplines.list_methods()

#I would like to get a description of an article
disciplines.describe('consensus map of science')

#I would like to compare two articles.
disciplines.compare(['consensus map of science', 'hyland 2000'])



'''