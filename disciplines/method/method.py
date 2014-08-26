# -*- coding: utf-8 -*-
""" Main method of module

Enables to assess fitneess of data for paricular theory.
Looks for what kind of data is required for investigation of particular theory.
Checks overall fitness of data for all theories.

Vars:
	None
"""

def assess_data_fitness(data, theory):
	""" Checks fitness of available data for a particular theory

	Args:
		data - link to database, dataframe or to ontology (networkx) object.
		theory - name of module that will be investigated.

	Return:
		fitness (float(0,1)) : where 1 represents complete fitness

	"""
	theory_requirements = ""
	#theory_requirements = help(theory)
	theory_requirements = theory.__doc__
		re.find("\nArgs:\n")


def get_data_requirements(theory):
	"""
	Args:
		dataname (string) : name of data.

	Returns:
		dataname (list) : (people, events, citation network)
	"""

	if True:
		result.append(dataname)

def check_overall_fitness(data, complete=False):
	"""Checks health of all theory based on available data.

	Args:
		data : link to database, dataframe or to ontology (networkx) object.
		complete (Boolean) : returns detailed assessment of fitness of each dataname.
		for example. 

	Returns:
		result (dictionary) : {theory: value}"""
		for theory in all_theories():
			data_fitness = assess_data_fitness(assess_data_fitness)
			mydict[theory] = data_fitness

def is_datatype_required(data, datatype, theory, complete=False):
	"""Checks whether datatype is 

	Args:
		data : link to database, dataframe or to ontology (networkx) object.
		datatype (: (persons, events, texts, citations ) # Or combined
		complete (Boolean) : True for complete info.

	Returns:
		result (int[0:5]) : where the higher int the bigger importance """

	for data in theory:
		if is_required(data) == True:
			result[data] = True # Or details
			if complete == True:
				result[data] = "more info about how it is required"
	return result
