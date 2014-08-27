# -*- coding: utf-8 -*-
"""Characterisation of organisational structures

Checks the characterisation of organisational structure. It is based on two axes
functional dependence and strategic dependence. Uncertainty is a third axis.

Args:
    dependencies
    authors
    concepts
    data
    theory
"""

dependencies = ['functional', 'strategic']
authors = ['Vinck']
concepts = ['cumulative results', 'teams']
data = ['teams', 'procedures']
theory = '''
    Uncertainty can be split into two dimensions:
    1 Technical uncertainty: control of procedures and of the ability to achieve results.
    2 Strategic uncertainty: importance given to research problems, their relevance and
    degree of priority.'''


def get_functional_dependence(dsc, team, procedurs, results):
    """Functional dependence

    Theory:
        Functional dependence (FD): the different types of knowledge produced 
        rely on each other. When there is a high level of FD, teams use the 
        same procedures and link up their results. When it is low, the procedures 
        vary and the results are not cumulative.
        Examples:

    Args:
        dsc
        teams
        procedures
        results

    Vars:
        teams
        procedures
        varryiness_of_procedures
        results_are_cumulative

    Returns:
        functional_depentence - describes the 
    """

def get_strategic_dependence(dsc, team, procedures, results):
    """ Gets strategic dependeces of discipline

    Theory:
        Strategic dependence (SD): work depends on the definition of collective 
        research priorities and the allocation of resources. When SD is high, 
        teams rival with each other in order to control resources and recognition 
        in the field, including control over the name given to the field. When 
        it is low, teams are less concerned with the hierarchy of objectives 
        across the field.
        Examples:
        None

    Args:
        collective_research_priorities = 
        allocation_of_resources = 
        teams_are_less_concerned_with_hierarchu_of_objectives = 
        teams_rival = True/False
        is_renaming_field  Might turn into function.

    Returns:
        int from 0 to 1 where 1 represents totally sure.
    """

#Now for each
"""
Anarchy of the teams pursuing different goals with different methods, without either
coordination or division of labour?
"""
def get_goals(team):
    return goals

def get_coordination_level():
    return coordination_level

def get_standard_methods():
    return standard_methods

def get_method_difference(method, method1):
    return value

"""
Theory:
    Pacific coexistence of specialised teams working with standardised methods and coordinating their work but
    without imposing any structure to their research field 
"""

def is_pacific_coexistence_of_specialised_teams(dsc):
    """ pacific_coexistence_of_specialised_teams

    Can we call the existence pacific?

    Args:

    Returns:

    Theory:

    Notes:

    """
    return value


def get_specialised_teams(dsc):
    """ specialised_teams

    Longer.

    Args:

    Returns:

    Notes:

    """
    return value

def is_imposing_structure_to_the_research_field(dsc):
    """ Checks whether a discipline is imposing structure to the research field.

    Longer.

    Args:
        dsc - a discipline

    Returns:

    Notes:
        Could do a bit more.

    """
    return value


"""
Theory:
    High Fight between schools of thinking for the domination of the discipline.
    Teams internally coordinated but pursuing different goals and using different methods
"""

def is_standard_method(mth, dsc):
    """ Checks whether method is standard for a discipline

    Longer.

    Args:

    Returns:

    Notes:

    """
    return value

"""
Theory:
    Fight between subdisciplines (using the same procedures and coordinating their work) for control and the
    hierarchy inside the discipline
"""

def get_fights_between_subdisciplines(discipline):
    """    
    Return
    """
    return subdiscipline_fights

def are_using_same_procedures(discipline):
    return True, list_of_procedures




"""I Should separate ones I define before matrix or even before introduction of axis"""

def is_school(name):
    """ what.

    Longer.

    Args:

    Returns:

    Notes:

    """
    return value

def is_team(name):
    """
    """
    return value
    
def is_fighting_for_domination(dsc):
    if True:
        return True
    if False:
        return False #second may be added
