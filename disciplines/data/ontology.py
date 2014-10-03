# -*- coding: utf-8 -*-
#ontology.py
"""Defines ontology for the project

Disciplines are key object. Others are people, concepts, organizations, 
events, publications and citations

All of these variables are available to get relations between.
Not all objects are possible to related. While others have multiple-type
connections.

(person, concept, {used}) # used, was mentioned together. Primary source, secondary source.
(concept, person, {mention})

(person, organization, {member, chair}) # member, created. From CV of perosn, from organizations page, from publication. 
(organization, person, {delegated}). From website(ACLS).

(person, event, {particpated_in}) # Chaired, attended, described, reviewed, participated, criticised. Tweets, facebook, blogs, conference pages, event pages.
(event, person, {dedicated_to}) # From event description, person mentioned in name of event, person mentioned in session names.

(person, publications, {used}) # wrote, commented, cited, reviewed. 
(publication, person, {mentioned}) # 

(person, citation, {did}) # From publications
(citation, person, {mentioned})

(concept, organization, {uses}) From website of organization.
(organization, concept, {dedicated_to, uses})

(concept, event, {used}) From website of event, from blog of participant.
(event, concept, {used}) Event dedicated to concept. Event used concept.

(concept, publication, {used}) Concept appeared in publication. Concept was analyzed in publication. Concept appeard in publication. From publications and reviews. Primary and secondary.
(publication, concept, {used}) Publication used concept.

(concept, citation, {appeard}) Concept appeared in citation. Concept was defined in citation.
(citation, concept, {used}) Citation was about the concept.

(organization, event, {used}) Organization organized event. Organization supported event. Organization was dedicated to event.
(event, organization, {used}) Event was dedicated to organization. Event was organized by event

(organization, citation, {used}) Organization mentioned in citation. Publication
(citation, organization, {used}) Citation contained name of organization. Publication

(organization, publication, {used})   Organization released publication. Organization criticized publication.
(publication, organization, {used}) Publication mentioned organization. 

(publication, citation, {used}) Publication contained citation. Publication refered to citation.
(citation, organization, {used}) Citation named organization

(concept, concept) # concepts and concept cooapeared in. Concept and concept are synonimous. Concept and concept are antonymous. Concept and concept are both used by author.
(person, person) # coauthorship  # wight by whos first in publication name
(organization, organization) # organizations have similar causes. Are both related to.
(event, event) # Were organized side by side. Data
(citation, citation) # Citations appeared in same publication.

visokie = {
'when':'2001-05-06',
'where':'Kaunas, VU',
'who': 'Vardenis Pavardenis'}
'source': 'id'
"""

import networkx as nx

# This part could be useful for easier typing. But I still have doubts.
person = 'person'
publication = 'publication'
event = 'event'
organization = 'organization'
citation = 'citation'
concept = 'concept'

ntypes = [person, concept, organization, event, publication, citation]
etypes = ['wrote', 'used', 'participated', 'cited', 'coauthored'] # Deprecated, these should be included elsewhere.

g = nx.Graph() # di, multidi and others should be considered


nodes = [
	('Biglan', {'what':'person'}),
	('Kuhn', {'what':'person'}),
	('American Council of Learned Societies', {'what':'organization'}),
	('American Sociological Association', {'what':'learned society'}),
	('philosophy', {'what':'discipline'}),
	('Biglans classification', {'what':'classification'}),
	('Hollans classification', {'what':'classification'}),
	('Academic demarcations', {'what':'conference'}),
	('Lithuanian Society of Young Reseachers', {'what':'organization'}),
	('Interdisciplinarity: how to make it work', {'what':'conference'})]

edges = [('Biglan','classified', 'disciplines'),
	('Kuhn','wrote', 'Structure of scinetific revolutions'),
	('American Sociological Association', 'joined', 'American Council of Learned Societies'),
	('Someone', 'is delegetade to', 'American Council of Learned Societies'),
	('philosophy', 'is part of', 'Biglans classification'),
	('Biglan', 'created', 'Biglans classification')

	('Fuller', 'was a speaker in', 'Interdisciplinarity: how to make it work'),
	('Lyall', 'was a speaker in', 'Interdisciplinarity: how to make it work'),
	(u'Rūta Petrauskaitė', 'was a speaker in', 'Interdisciplinarity: how to make it work'),
	('Lithuanian Society of Young Reseachers', 'organized', 'Interdisciplinarity: how to make it work'),
	('Andrew Abbot', 'was a keyspeaker in', 'Academic demarcations'),
	('Rudolf Stichweht', 'was a keyspeaker in', 'Academic demarcations'),
	('Sheila Jasanoff', 'was a keyspeaker in', 'Academic demarcations'),
	('Lars Qvortrup', 'was a keyspeaker in', 'Academic demarcations')]

	('Sheila Jasanoff', 'is related to','Science and Technology Studies'),
	('Rudolf Stichweht', 'wrote', 'Differentiation of Scientific Disciplines. Causes and Consequences, in: Encyclopedia of Life Support Systems. Unesco 2003 (http://www.eolss.net/).'),
	('Rudolf Stichweht', 'wrote', 'Scientific Disciplines, History of.  Pp. 13727-13731 in: International Encyclopedia of the Social and Behavioral Sciences, Vol. 20. Oxford: Elsevier 2001.')]