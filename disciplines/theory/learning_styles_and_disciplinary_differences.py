# -*- coding: utf-8 -*-
# learning_styles_and_disciplinary_differences.py
""" Learning styles and disciplinary differences by Kolb

Theory:
	Later...

Vars:
	author
	concepts
	data
	claim
	theory
	approach
	reading

Analysis:
	inuiry strategy - hard, what are the evidence for those
	basic inquiry question - might be easy to find, by simple text analysis.
	basic unit of knowledge - might be easy to medium
	how knowledge is portrayed - 
	typical inquiry method - possible to get from methodological and theoretical books, but also from broader literature

Notes:
	functions have to be able to turn strings to lists. Because of some entries are lists.
	
Other:
	discipline_type
	social_professions
	based_professions
	natural_science_and_mathematics
	humanities_and_social_science

"""
author = 'Kolb'
authors = author
concepts = [
	'inquiry strategy', 
	'basic inquiry question', 
	'basic unit of knowledge', 
	'typical inquiry method']
data = []
claim = []
theory = '''
    '''
approach = []
reading = []
reference = '''	KOLB, D.A. (1981) Learning styles and disciplinary differencesin: A. CHICKErUNG (Ed.) 77~e Modern American College (San Francisco, 
	CA, Jossey Bass). url: http://www.ltsn-01.ac.uk/static/uploads/workshop_resources/178/178_Learning_styles_and_disciplinary_difference.pdf'''



discipline_type = [
	'inquiry strategy', 
	'dominant philosophy', 
	'theory of truth', 
	'basic inquiry question', 
	'basic unit of knowledge', 
	'how knowledge is portrayed', 
	'typical inquiry method']

social_professions = [
	'discrete synthesis', 
	'pragmatism', 
	'workability', 
	'how', 
	'events', 
	'actions', 
	'case study']

science-based_professions = [
	'discrete analysis', 
	'empiricism', 
	'correspondance', 
	['when', 'where'], 
	['natural laws', 'empirical uniformities'], 
	'things', 
	'classical experiment']

natural_science_and_mathematics = [
	'integrative analysis', 
	'structuralism', 
	'correlation of structure with secondary qualities', 
	'what', 
	'structures', 
	'symbols', 
	'model building']

humanities_and_social_science =  [
	'integrative synthesis', 
	'organicism', 
	'coherence', 
	'why', 
	'processes', 
	'images', 
	['historical analysis', 'field study', 'clinical observations']]

columns = [discipline_type, 
	social_professions,
	based_professions,
	natural_science_and_mathematics, 
	humanities_and_social_science]