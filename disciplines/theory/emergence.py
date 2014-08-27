# -*- coding: utf-8 -*-
""" Emergence of discipline 

This module is an implementation of theoretical work by Ziman.
It checks a stage of development and contains multiple functions 
designed for looking for evidence of stage of emergence.

Vars:
    author
    concepts
    data
    claim
    theory
    approach
"""

author = ['Ziman']
authors = author
concepts = ['nodal point', 
    'organize little research conferences', 
    'hierarchy of authority', 
    'association develops into a learned society', 
    'newsletter becomes reputable primary journal', 'primary journal']
data = ['citation network', 'journal', 'newsletter', 'conference participants']
claim = 'No claims found yet'
theory = '''
    1. Emerging specialty is only observable as a nodal point in the network of 
    citations. 
    2. Scientists whose research is associated with this co-citation cluster 
    organize little research conferences to discuss their common interests, or are 
    commissioned to write articles for a special issues of a primary journal 
    drawing attention to progress in this particular problem area. 
    3. An ‘invisible college’ begins to condense out, in the form, say, of a semi-
    official association held together by further conferences, the regular 
    exchange of pre-prints and re-prints and the publication of an informal 
    ‘newsletter’. 
    4. The association develops into a regular learned society, whose newsletter 
    has become a reputable primary journal. 
    5. A hierarch of authority is soon set up to preside over conferences, edit 
    journals, allocate resources, and confer recognition on the members of the new
    discipline.
    '''
    
approach =  '''
    The object of analysis is easy to specify when it comes to first point. It is 
    some citations. In second point we have to identify a) scientists associated 
    with citation cluster, b) conferences. Or and to look for special issues of 
    primary journals. It is hard to identify third point as we would need to 
    find "invisible college", exchange of pre-prints nadd reprits. But, it is 
    possible to find some newsletters. The fourth step is straightforward, it is 
    rather easy to identify learned society when it already exists, the same about 
    the journal. The fifth. Who presides over conferences, who edit journal and 
    who allocate resources and confer recognition is easy to get. Most of this 
    information can be get online.
    Several strategies are available to do such things. It depends what we want to 
    do. The later stage of development the easier is to get data. However, even 
    when it comes to finding NPNOC it can be accomplished.
    Other thing to consider is the starting point of research. Whether to start 
    from specific disciplines or just run over all. The first type is easier to 
    do, but then we would come to a problem of integrating the data. The second 
    approach is harder to do but is better one. For know, I think the best way to 
    go is to have small case studies, built on earlier research, and follow by 
    constructing the overarching algorithms.
    Functionality: identification of turning points of development of a discipline 
    by identifying NPNOC, people, conferences and etc date is the prime focus.
    

    Ideas:
    if nodal_point(citation_network):
        researchers = get_researchers()
        emergence_stage = 1

    if special_issue in primary_journal:
        emergence_stage = 2
    if cocitation_cluster organize_little_conferences:
        emergence_stage = 2

    if further_conferences or regular_exchange_of_pre_prints:
        emergence_stage = 3

    if learned_society(researcher_list):
        emergence_stage = 4 
    if primary_journal(researcher_list):
        emergence_stage = 4 

    if hierarchy_of_authority:
        emergence_stage = 5
    '''

def what_emergence_state(dsc):
    """ Checks for state of emergence of a discipline

    Runs other functions that looks for different aspects

    Args:
        dsc : discipline

    Returns:

    Notes:
    """
    return

def is_emergence_state(dsc, stage):
    """ Checks for state of emergence of a discipline

    Runs other functions that looks for different aspects

    Args:
        dsc : discipline

    Returns:

    Notes:
    """
    return


def observe_nodal_points(network_of_citation, stage):
    """ Oserve_nodal_points

    Args:
        network_of_citations : networkx object /might be any graph type next time
        stage : what part of stage to look.

    Returns: tuple of cliques each representing a (forming discipline)

    Theory:
        '1. Emerging specialty is only observable as a nodal point in the network of
        citations.' also can be named co-citation cluster  

        """
    clique = ''
    cliques = ''
    network_of_citation
    stage
    return cliques

def get_conferences_organized_by_cluster(researcher_list):
    """ Conferences organized by cluster of researchers 

    Researchers are looking in some ways.
    Args:
    """
    researcher_list
    conference_list = ['Interdisciplinarity: How to make it work', 'Academic demarcations']

    return conference_list

def get_special_issues_of_a_primary_journal(network_of_citation):
    """ Gets special issues of a journal

    Args:
        network_of_citation
        
    Vars:
        journal :
        journals :
        primary_journal : value of primarisness of a journal.
        primary_journal : value of primarisness of a journal.

    Theory:
        2. Scientists whose research is associated with this co-citation cluster 
        organize little research conferences to discuss their common interests, or are 
        commissioned to write articles for a special issues of a primary journal 
        drawing attention to progress in this particular problem area.
    """
    answer = None
    journal = ''
    journals = []
    primary_journal = '' 
    return answer

def get_invisible_college(network_of_citation):
    """
    Args:
        network_of_citation

    Vars:
        condensation_of_invisible_college :
        semi_official_association (str) :
        semi_official_associations (list) :
        conferences (list) :
        exchange_of_prints :
        informal_newsletter :

    Theory:
        An ‘invisible college’ begins to condense out, in the form, say, of a semi-
        official association held together by further conferences, the regular 
        exchange of pre-prints and re-prints and the publication of an informal 
        ‘newsletter’.


    """


def get_regular_exchange_of_pre_prints(network_of_citation):
    network_of_citation
    return


def detect_regular_learned_society(url):
    """Detects regular learned societies in web or based on data.

    regular learned societies of disciplines ar looked for.
    We depend on many online resources that list disciplines

    '...4. The association develops into a regular learned society, whose newsletter 
has become a reputable primary journal. ...'

    Args:
    url = 
    """
    url
    return

def reputable_primary_journals():
    """ Finds reputable primary journals.

    Depends on online resources

    Args:

    Returns:
    """
    return


"""5. A hierarch of authority is soon set up to preside over conferences, edit 
journals, allocate resources, and confer recognition on the members of the new
 discipline."""

def detect_hierarchy_of_authority():
    return

def who_presides_over_conferences():
    """ Detects hierrarchy of authority be examining decisions made
    """
    return

def who_edits_journals():
    """ Find edditors of journals

    """
    return

def who_confers_recognition(data ,members=None):
    """
    Args:
    members - possible, group of people who are influenced by authority.
    """
    return


def is_stage(number_of_stage, data=False):
    """ Checks whether discipline is in stage
    
    Args:
    supporting - 0-1 of evidence for supporting
    against - 0-1 of weight of against evidences

    Returns:
    the_stage_is dictionary with two values. x, represents number o
    """

    supporting = None
    denying = None
    answer = None

    if data == True:
        return full_answer

    if data == False:
        return answer 




def detect_emergences():
    """This is to detect emergence. It takes networkx object and other data
    

    Returns:
    emergence - description of key points, places and names related to emergence.
    emergence stage = (1, 5, 3, 0)  #That means that there are 0 evicence points 
    for stage 1, 1 for second stage, and three for third.

    Note:
    Further forks could look for emergence all the time live, by looking at the web
    """


def recreate_emerge(discipline):
    """Recreates emergence of a discipline.

    Extracts main events and puts them into event graph. The graph is directed, it 
    it moves from most past events, through people, names and concepts.

    Args/Variables, might be both.
    concepts = {'ontologija': 'apibudinimas', 'sinergija': 'apibudinimas'}
    people = {'JT Klein': 'papildoma informacija'}
    literature = {'doi':,
                  'pavadinimas:
                  'autorius'}

    edgetypes:
        author - person to publication (when)
        organised - person to event (when)
        released - journal to book (when)
        conferino - person to person (where, when)
        claimed - person to quote, or website
        chaired - conferences
        edited - perosn to journal
        attended - person to event

        Each of these can be defined by separation functions.


    Returns: a rather complicated thing. Yes, networkx_graph.
    """

    '''
    g.add_node(author, author_data)
    g.dd_node(publication, publication_data)
    g.add_node(event, event_data)
    g.add_node(concept, concept_data)

    g.add_edge(author, publication, {when="timestamp"})
    g.add_edge(person, vent, {when="timestamp"})
    g.add_edge(journal, book, {when="timestamp"})
    g.add_edge(person, person, {when="timestamp"})
    g.add_edge(concept, publication, {when="timestamp"})
    '''

# Or same with claimege
    def add_authorship(data, graph ,author, publication):
        """adds stuff to a graph,
        add_edge(author, publication, attrs)

        Args:
        data - where data comes from.
        graph - graph to which edge will be added
        author - 
        publication -
        data - """

    def add_organizer(data, graph, event, organizer):
        """adds stuff to a graph,
        add_edge(event, organizer, attrs)

        Args:
        data - where data comes from.
        graph - graph to which edge will be added
        author - 
        publication -
        data - """


    def add_authors(data, filters):
        """ Adds all authors that pass the filters"""
        g.add_nodes(nbunch, attrs)
        return

    def add_events(data, filters):
        """ Adds all events that pass the filters"""
        g.add_nodes(nbunch, attrs)
        return

    def add_concepts(data, filters):
        """ Adds all concepts that pass the filters"""
        g.add_nodes(nbunch, attrs)
        return

    def add_people(data, filters):
        """ Adds all author that pass the filters"""
        g.add_nodes(nbunch, attrs)
        return