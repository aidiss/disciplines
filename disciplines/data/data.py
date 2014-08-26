# -*- coding: utf-8 -*-
#data.py
"""This package deals with number of data issues

Getting data
Formatting data
Collecting urls

A number of functions are created to get data from online repositories. These functions are in two profession_types:
ready data - one that is formated well and prepared for usage, like CSV, XML and etc. And scrapping techniques.
Data is being transformed into one of our 

The data is stored and manipulated in three data types:
	SQL (sqlite) is used for storing large quantities of that have well defined form and structure.
	Pandas powered arrays and dataframes.


Dependencies:
sqlite3
pandas
networkx


"""
datatypes = ['person', 'profession' 'event', 'publication', 'concept', 'definition', 'organization', 'disciplines']
profession_types = ['researcher', 'technician'] #more in one theorie covered by Vinck
event_types = ['conference', 'workshop', 'summerschool']
publication_types = ['book', 'blog', 'article', 'proceeding']
concept_types = ['who uses']
definition_types = ['who defined']
organization_types = ['learned society', 'publisher']
disciplines_types = [] # According to other

def populate_db(reqs):
	"""Populates database

	Args:
		reqs : requirements for populating. Gives specific instructions which part to populate.
	"""


	return db 

def create_db(reqs):
	"""Creates database

	Creates fields, connections and etc.

	Args:
		reqs : requirements for creating. Gives specific instructions which part to create.

	Returns:
		database

	Notes:
		Can be done by using names found in theory"""
	return database

def update_db(reqs):
	"""Updates database

	Args:
		reqs : requirements for creating. Gives specific instructions which part to create.

	Returns:
		database
		
	Notes:
		"""
	return database 

def create_ontology(reqs):
	"""Creates ontology by given requirements.

	Args:
		reqs : 

	Returns:
		ontology (networkx object) 

	Notes:
		"""
	return ontology

def create_pandas(reqs):
	"""Creates pandas object by given requirements.

	Args:
		reqs : 

	Returns:
		dataframe or an array (pandas object) 

	Notes:
		"""
	return dataframe

