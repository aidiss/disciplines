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
#	theory_requirements = theory.__doc__
#		re.find("\nArgs:\n")


def get_data_requirements(theory):
	"""
	Args:
		dataname (string) : name of data.

	Returns:
		dataname (list) : (people, events, citation network)
	"""
	dataname = ['John']
	result = []
	if True:
		result.append(dataname)
	return "This is the required data"

def check_overall_fitness(data, all_theories, complete=False,):
	"""Checks health of all theory based on available data.

	Args:
		data : link to database, dataframe or to ontology (networkx) object.
		complete (Boolean) : returns detailed assessment of fitness of each dataname.
		for example. 

	Returns:
		result (dictionary) : {theory: value}"""
	all_theories = [1,2,3]
	result = ''
	data_fitness = ''
	mydict = {}
	for theory in all_theories:
		data_fitness = assess_data_fitness(assess_data_fitness, 'd')
		mydict[theory] = data_fitness
	return "The overal fitness is ..."

def is_datatype_required(data, datatype, theory, complete=False):
	"""Checks whether datatype is 

	Args:
		data : link to database, dataframe or to ontology (networkx) object.
		datatype (: (persons, events, texts, citations ) # Or combined
		complete (Boolean) : True for complete info.

	Returns:
		result (int[0:5]) : where the higher int the bigger importance """
	result = ''
	def is_required(data):
		return
	for data in theory:
		if is_required(data):
			result[data] = True # Or details
			if complete == True:
				result[data] = "more info about how it is required"
	return False
