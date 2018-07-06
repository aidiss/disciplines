# -*- coding: utf-8 -*-
def assess_data_fitness(data, theory):
    """ Checks fitness of available data for a particular theory

    Args:
            data - link to database, dataframe or to ontology (networkx) object.
            theory - name of module that will be investigated.

    Return:
            fitness (float(0,1)) : where 1 represents complete fitness

    """
    theory_requirements = ""
    theory_requirements = help(theory)
    theory_requirements = theory.__doc__
