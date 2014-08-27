# -*- coding: utf-8 -*-
"""Structuring of research fields.

This module investigates concept used by Vinck in Sociology of Scientific work.
It contains four functions that investigate whether research field can be
considered as having one type of structuring. It looks for four types of 
structuring: polycentric oligarchy, partitioned beurocracy, fragmented adhocracy,
professional adhocracy, polycentric profession, technologically integrated bureocracy 
and conceptually integrated bureaucracy.

Example:
    is_polycentric_oligarhy('philosophy')
    > 0.1
    is_polycentric_oligarhy('sociology')
    > 0.35

Args:
    authors
    data
    concepts
    urls
    reading

Data:
    researcher positions : are they in power
    schools : hard to identify, have to be based on some research
    methods : result assessment methods
    training proggrames : check whether they are standardised
    focus : are they focused on analytical work

    coalition_list : is discipline in coalitions
    research resource coordination : who coordinates.

    working procedures : are they common?
    controversies : what is a framework of their solutions?

    instruments : what instrumentas are used?
    methods : what methods are used?
    empiricity of Knowledge : is knowledge empiric
    specificity of knowledge : is knowledge specific?

    theoretical framework : is it unified? 

"""


authors = ['Vinck', 'Whitley']
concepts = [
    'researcher position',
    'school',
    'researcher power',
    'methods',
    'training programme',
    'standardised training programme',
    'focus',
    'focus on analytical work',

    'coalition list',
    'working procedures',
    'controversies',
    'instruments',
    'methods',
    'empiricity of knowledge',
    'specificity of knowledge'.

data = ['methods', 'positions', 'training programmes', 'focus', 'controversies']
claim = 
theory = '''
    '''
approach =  
reading =
reference = [
    'Vinck. The sociology of scientific work.', 
    'Whitley, R. (1974), The Intellectual and Social Organization of the Sciences Oxford: Oxford University Press']


def is_polycentric_oligarhy(dsc):
    """ Polycentric oligarchy

    
    handful_of_researchers_occupying dominating positions existence of rival schools


    Args:
        handful_of_researchers_occupying

    Vars:
        handful_of_researchers (list) :
        dominating_positions (list) :
        rival_schools (list) :
        resuls_assessment_methods (list) :

    Returns:
        result

    Theory:
        polycentric oligarchy - in which a handful of researchers occupy dominating 
        positions and create rival schools, using their own results assessment methods. 
        Examples: ’German psychology at the start of the twentieth century and British 
        social anthropology.

        Examples:
            German psychology at the start of the twentieth century and 
            British social anthropology

    """

    return

def is_partinioned_beurocracy(dsc):
    """ Partitioned beurocracy 

    Args:
        dsc

    Vars:
        standardised_training_programmes (bool) :
        relative_theoretical_cohesion (bool)  :
        focus_on_analytical_work (bool) : 

        training_programmes (list) :

    Returns:

    Theory:
        standardised training programmes, relative theoretical cohesion and a focus on 
        analytical work (very little control of empirical phenomena). Anglo- Saxon neoclassical 
        economics, which operates like a

        Examples:
            Anglo- Saxon neoclassical economics

    """
    example_disciplines = ['Anglo- Saxon neoclassical economics']
    return

def is_fragmented_adhocracy(dsc):
    """ Fragmented adhocracy.

    Args:
        dsc :
    Vars:
        example_disciplines :

    Returns:

    Theory:
        without any kind of collective direction or overall consistency, coalitions in the 
        field are temporary. Objects are defined outside of the discipline according to 
        the audience. Example: British sociology and literary studies.
        
        Examples: 
            british sociology
            literary studies.

    Consideration:

    Notes:

    """
    example_disciplines = ['british sociology', 'literary studies']
    return

def is_professional_adhocracy(dsc):
    """ Proffesional adhocracy.

    Args:

    Vars:
        coordination :
        research_resources :
        audience :
        influence  :
        objects :
        projects :

    Returns:
        professional_adhocracy

    Theory:
        Professional adhocracy: coordination of research resources for multiple objects and 
        projects, according to audience and influence. 

        Example: 
            biomedical sciences.



    """
    example_disciplines = ['biomedical sciences']
    return

def is_polycentric_profession(dsc):
    """ Polycentric profession.

    Checks whether discipline is polycentric profession.

    Args:
        dsc - 

    Wars:
        common_working_procedures (list) : procedure list, look for standars.
        contraversies_in_the_field (list) : event list, use controversy mapping 
    
    Returns:
        polycentric_profession

    Theory:
        Polycentric profession: common working procedures act as a framework for 
        controversies in the field. Example: experimental physiology.
        
        Examples:
            experimental physiology

    """
    example_disciplines = ['experimental physiology']
    return

def is_technologically_integrated_bureaucracy(dsc):
    """Technologically integrated bureaucracy

    Theory:
        Technologically integrated bureaucracy: coordination of work using the same set of 
        instruments, methods and concept (nomenclature). Knowledge is both empirical and 
        specific. Example: chemistry.
        Example:
            chemistry


    Args:
        dsc

    Vars:
        set_of_instruments (list)
        same_set_of_instruments (list)
        instruments (list)
        methods (list)
        concepts (list)
        knowledge_is_empirical(bool)
        knowledge_is_specific(bool)

    Returns:

    Notes:

    """
    example_disciplines = ['chemistry']
    return

def is_conceptually_integrated_bureaucracy(dsc):
    """ Conceptuall integrated bureaucracy

    
    Theory:
        Conceptually integrated bureaucracy: coordination of work via a unified theoretical 
        framework establishing the hierarchy of specialities. Example: physics.
        Example:
            physics

    Args:

    Vars:
        unified_theoretical_framework :
        hierarchy_of_specialities : treelike structure

    Returns:
        conceptually_integrated_bureaucracy

    Notes:

    """
    example_disciplines = ['physics']
    return