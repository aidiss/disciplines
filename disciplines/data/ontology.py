
"""Defines ontology for the project

Disciplines are key object. Others are people, concepts, organizations, 
events, publications and citations

All of these variables are available to get relations between.
Not all objects are possible to related. While others have multiple-type
connections.




(person, concept, {used}) # used, was mentioned together
(concept, person, {mention})
(person, organization, {member, chair}) # member, 
(organization, person, {delegated})
(person, event, {particpated_in}) # participated in
(event, person, {dedicated_to})
(person, publications, {used}) # wrote, was mentioned
(publication, person, {mentioned})
(person, citation, {did}) #
(citation, person, {mentioned})
(concept, organization, {uses})
(organization, concept, {dedicated_to, uses})
(concept, event, {used})
(event, concept, {used})
(concept, publication, {used})
(publication, concept, {used})
(concept, citation, {used})
(citation, concept, {used})
(organization, event, {used})
(event, organization, {used})
(organization, citation, {used})
(citation, organization, {used})
(organization, publication, {used})
(publication, organization, {used})
(publication, citation, {used})
(citation, organization, {used})

(concept, concept)
(person, person) # coauthorship  # wight by whos first in publication name
(organization, organization)
(event, event)
(citation, citation)

visokie = {
'when':'2001-05-06',
'where':'Kaunas, VU',
'who': 'Vardenis Pavardenis'}
"""
import networkx as nx

person = 'person'
publication = 'publication'
event = 'event'
organization = 'organization'
citation = 'citation'
concept = 'concept'

ntypes = [person, concept, organization, event, publication, citation]
etypes = ['wrote', 'used', 'participated', 'cited', 'coauthored']

g = nx.Graph()

cnt = 0
for x in ntypes:
	for y in range(10):
		cnt += 1
		g.add_node(cnt, {'dtype':x}) 

nx.draw(g)


'''
person, wrote, book
person, participated, event
person, chaired, event
book, quoted, person
concepts, used_together, book
'''

