from rdflib import Graph, URIRef
'''
This module is dedicated to getting data from dbpedia

The data we get is based about few cattegories: learned societies, 
membership of learned societies, academic disciplines and many more.
This is done by using rdflib
'''

learned_societies = ''
members_of_learned_societies = ''
academic_disciplines = ''
'''
url = 'http://dbpedia.org/page/Category:Learned_societies'
urls = ['http://dbpedia.org/page/Category:Learned_societies',
	'http://dbpedia.org/resource/Category:Learned_societies']
not_interesting_urls = []

g = Graph()
g.parse(url)
mylist = []
for x in g:
    cond1 = 'http://dbpedia.org/' in x[0]
    cond2 = 'Category:Learned_societies' in x[2]
    cond3 = 'Category:' not in x[0]
    if (cond1) and (cond2) and (cond3):
        stringed = str(x[0])
        striped = stringed.lstrip('http://dbpedia.org/resource/')
        replaced = striped.replace('_', ' ')
        mylist.append(replaced)
    

[x for x in mylist]


url = 'http://dbpedia.org/page/Category:Members_of_learned_societies'
g = Graph()
url = 'http://dbpedia.org/page/Category:Academic_disciplines'
g.parse(url)
'''

'''
Other:
category:Biblical_studies
category:Education_by_subject
category:Production_economics
category:Applied_disciplines
category:Subfields_by_academic_discipline
category:Academic_studies_of_ritual_and_magic
category:Environmental_science
category:Humanities
category:Jurisprudence
category:Science
category:Architectural_theory
category:Development_studies
category:Environmental_studies
category:Communication_studies
'''
