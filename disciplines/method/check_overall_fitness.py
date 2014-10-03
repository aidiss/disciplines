# -*- coding: utf-8 -*-
from assess_data_fitness import assess_data_fitness 
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
	return "The overal fitness is awfull"