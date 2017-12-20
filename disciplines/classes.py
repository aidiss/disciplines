"""Classes

This module prepares classes that might be used in later stages of project.

Further:
- This part will be changed according to sqlalchemy declarative.
"""


class CitationNetwork(object):
    """Citation network is particular kind of network were relations describe citations
    Few types exist,

    If the class has public attributes, they should be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section.

    Attributes:
      attr1 (str): Description of `attr1`.
      attr2 (list of str): Description of `attr2`.
      attr3 (int): Description of `attr3`."""

    def __init__(self, arg):
        """        """
        super(Citation_network, self).__init__()
        self.arg = arg

    def some_other_citatio_network_function(self):
        return


class Coauthorship_network(object):
    """Coauthorship network is particular kind of network were relations show that authors wre authoring the same work"""

    def __init__(self, arg):
        super(Coauthorship_network, self).__init__()
        self.arg = arg

    def some_other_function(self):
        """
        """
        return


class Concept(object):
    """The summary line for a class docstring should fit on one line.

    If the class has public attributes, they should be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section.

    Attributes:
      attr1 (str): Description of `attr1`.
      attr2 (list of str): Description of `attr2`.
      attr3 (int): Description of `attr3`."""
    def __init__(self, arg):
        """Example of docstring on the __init__ method.

        The __init__ method may be documented in either the class level
        docstring, or as a docstring on the __init__ method itself.

        Either form is acceptable, but the two should not be mixed. Choose one
        convention to document the __init__ method and be consistent with it.

        Note:
          Do not include the `self` parameter in the ``Args`` section.

        Args:
          param1 (str): Description of `param1`.
          param2 (list of str): Description of `param2`. Multiple
            lines are supported.
          param3 (int, optional): Description of `param3`, defaults to 0.

        """
        super(Concept, self).__init__()
        self.arg = arg
        self.defintions = {'name': 'definition'}
        self.used_in = []

    def get_definition(self):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        return

    def get_usage(self):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        return

    def get_used_in(self):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        return

    def wordnet(self):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        return

    def was_coined_by(self, person=None):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        return

    def was_mentioned_in(self, book=None):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        return

    def is_keyword_in(self, publicat=None, discipline=None, journal=None):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        return

    def is_keyword_in_publication(self):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        return

    def is_keyword_in_discipline(self):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        return

    def is_keyword_in_journal(self):
        """
        """
        return

    def is_object_of(self, discipline):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        return

    def is_tool_in(self, discipline):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        return


class Discipline(object):
    """This is the main class of

    Its main feature is to take other inputs into consideration and derrive type from it.

    Attributes:
      attr1 (str): Description of `attr1`.
      attr2 (list of str): Description of `attr2`.
      attr3 (int): Description of `attr3`."""

    def __init__(self, *kwargs):
        """
        """
        for key, value in kwargs.iteritems():
            self.arg = arg
            self.name = ''
            self.in_classifications = []
            self.related_disciplines = []
            self.emergence = {}
            self.founders = []
            self.users = []
            self.concepts = []
            self.methods = []
            self.subdisciplines = []
            self.history = ''

    def mentioned_in(self):
        """ Checks whether discipline was mentioned in Journal or Article"""
        return

    def is_oligarchic(self):
        """ Is Discipline oligarchic (Vinck)"""
        return

    def is_pure(self):
        self.text
        return None

    def is_life(self):
        self.name
        return

    def is_sudiscipline_of(self, discipline):
        self.name

        return

    def is_interdisciplinary_field(self, evidence=False, source=False):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        return

    def is_superdiscipline_of(self, discipline, evidence=False, source=False):
        return

    def describe(self):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        return

    def get_neighboring_disciplines(self, source=False):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        return

    def get_subdisciplines(self, source=False):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        return

    def get_super_disciplines(self):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        return

    def get_emergence_level(self):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        return

    def get_history(self):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        return 'This is the history of discipline, looking forward for better formatting'

    def get_subdisciplines(self):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        subdisciplines = []
        subdisciplines.extend(['one discipline', 'two'])
        self.subdisciplines = subdisciplines
        print(subdisciplines)

    def get_methods(self):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        return

    def get_concepts(self):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """

        return

    def get_related_disciplines(self):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        return

    def get_methods(self):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        return

    def get_something_else(self):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        return


class Event(object):
    """The summary line for a class docstring should fit on one line.

    If the class has public attributes, they should be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (list of str): Description of `attr2`.
        attr3 (int): Description of `attr3`."""

    def __init__(self, arg):
        def __init__(self, *kwargs):
            for key, value in kwargs.iteritems():
                self.arg = arg
            self.place = ''
            self.organizer = ''

    def get_place(self):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        return

    def get_time(self):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        return

    def get_start_time(self):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        return

    def get_end_time(self):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        return

    def get_participants(self):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        return

    def get_keywords(self):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        return

    def get_publications(self):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        return


class Journal(object):
    """This a class for journal. Journals can have different things going.
    
    Attributes:
        editors (list of strings): 
        head_editor (list of strings):
        articles (list of strings):
        about_us (list of strings):
        publisher (list of strings):

    """

    def __init__(self, arg):
        """Example of docstring on the __init__ method.

        """
        super(Journal, self).__init__()
        self.arg = arg
        self.editors = []
        self.head_editor = []
        self.publisher = []

    def get_editors(self, source):
        """Gets editors from source

        Note:
          There are different types of sources.

        Args:
          source: 

        Returns:
          list_of_editors #or does not return

        """
        return

    def get_head_editor(self):
        """Gets head editor

        Note:
          Do not include the `self` parameter in the ``Args`` section.

        Args:
          param1: The first parameter.

        Returns:
          True if successful, False otherwise.

        """
        return

    def get_publisher(self):
        """Class methods are similar to regular functions.

        Note:
          Do not include the `self` parameter in the ``Args`` section.

        Args:
          param1: The first parameter.
          param2: The second parameter.

        Returns:
          True if successful, False otherwise.

        """
        return


class Method(object):
    """The summary line for a class docstring should fit on one line.

    If the class has public attributes, they should be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section.

    Attributes:
      attr1 (str): Description of `attr1`.
      attr2 (list of str): Description of `attr2`.
      attr3 (int): Description of `attr3`."""

    def __init__(sef, arg):
        """Example of docstring on the __init__ method.

        The __init__ method may be documented in either the class level
        docstring, or as a docstring on the __init__ method itself.

        Either form is acceptable, but the two should not be mixed. Choose one
        convention to document the __init__ method and be consistent with it.

        Note:
          Do not include the `self` parameter in the ``Args`` section.

        Args:
          param1 (str): Description of `param1`.
          param2 (list of str): Description of `param2`. Multiple
            lines are supported.
          param3 (int, optional): Description of `param3`, defaults to 0.

        """
        super(Method, self).__init__()
        self.arg = arg
        self.used_in = []
        self.used_by = []
        self.description = []

    def is_used_by(self, person):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        return

    def is_used_in(self):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        return

    def get_used_by(self):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        return

    def get_used_in(self):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        return


class Learned_society(object):
    """Learned society is an object.

    If the class has public attributes, they should be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section.

    Attributes:
        arg (str):
        organizations_part_of (list of str): list of organizations that learned society is part of.
    """

    def __init__(self, arg):
        """Example of docstring on the __init__ method.

        The __init__ method may be documented in either the class level
        docstring, or as a docstring on the __init__ method itself.

        Either form is acceptable, but the two should not be mixed. Choose one
        convention to document the __init__ method and be consistent with it.

        Note:
          Do not include the `self` parameter in the ``Args`` section.

        Args:
          param1 (str): Description of `param1`.
          param2 (list of str): Description of `param2`. Multiple
            lines are supported.
          param3 (int, optional): Description of `param3`, defaults to 0.

        """
        super(Learned_society, self).__init__()
        self.arg = arg
        self.organizations_part_of = {'name': 'als', 'from': '1948'}
        self.name = ['']

    def get_members(self, take_into_account=False):
        """Class methods are similar to regular functions.

        Note:
            Gets members from somewhere, might be database.

        Args:
            take_into_account (bool): should attributes be considered?

        Returns:
            List of strings reprsenting members

        """
        return

    def get_memberhip_in_learned_society(self):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
          param1: The first parameter.

        Returns:
          True if successful, False otherwise.

        """
        return

    def get_disciplines(self):
        """Class methods are similar to regular functions.

        Note:
          Do not include the `self` parameter in the ``Args`` section.

        Args:
          param1: The first parameter.
          param2: The second parameter.

        Returns:
          True if successful, False otherwise.

        """
        return

    def list_members(self):
        """Class methods are similar to regular functions.

        Note:
          Do not include the `self` parameter in the ``Args`` section.

        Args:
          param1: The first parameter.
          param2: The second parameter.

        Returns:
          True if successful, False otherwise.
        """
        return

    def add_member(self):
        """Class methods are similar to regular functions.

        Note:
          Do not include the `self` parameter in the ``Args`` section.

        Args:
          param1: The first parameter.
          param2: The second parameter.

        Returns:
          True if successful, False otherwise.

        """
        return

    def del_member(self):
        """Class methods are similar to regular functions.

        Note:
          Do not include the `self` parameter in the ``Args`` section.

        Args:
          param1: The first parameter.
          param2: The second parameter.

        Returns:
          True if successful, False otherwise.

        """
        return

    def get_keywords(self):
        """Class methods are similar to regular functions.

        Note:
          Do not include the `self` parameter in the ``Args`` section.

        Args:
          param1: The first parameter.
          param2: The second parameter.

        Returns:
          True if successful, False otherwise.

        """
        return

    def add_keyword(self):
        """Class methods are similar to regular functions.

        Note:
          Do not include the `self` parameter in the ``Args`` section.

        Args:
          param1: The first parameter.
          param2: The second parameter.

        Returns:
          True if successful, False otherwise.

        """
        return

    def del_keyword(self):
        """Class methods are similar to regular functions.

        Note:
          Do not include the `self` parameter in the ``Args`` section.

        Args:
          param1: The first parameter.
          param2: The second parameter.

        Returns:
          True if successful, False otherwise.

        """
        return

    def add_partners(self):
        """Class methods are similar to regular functions.

        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:
            param1: The first parameter.
            param2: The second parameter.

        Returns:
            True if successful, False otherwise.

        """
        return

    def add_objectives(self):
        """Class methods are similar to regular functions.

        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:
            param1: The first parameter.
            param2: The second parameter.

        Returns:
            True if successful, False otherwise.

        """
        return

    def get_objectives(self):
        """Class methods are similar to regular functions.

        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:
            param1: The first parameter.
            param2: The second parameter.

        Returns:
            True if successful, False otherwise.

        """
        return


class Person(object):
    """The summary line for a class docstring should fit on one line.

    If the class has public attributes, they should be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section.

    Attributes:
      attr1 (str): Description of `attr1`.
      attr2 (list of str): Description of `attr2`.
      attr3 (int): Description of `attr3`."""

    def __init__(self, arg):
        """Example of docstring on the __init__ method.

        The __init__ method may be documented in either the class level
        docstring, or as a docstring on the __init__ method itself.

        Either form is acceptable, but the two should not be mixed. Choose one
        convention to document the __init__ method and be consistent with it.

        Note:
          Do not include the `self` parameter in the ``Args`` section.

        Args:
          param1 (str): Description of `param1`.
          param2 (list of str): Description of `param2`. Multiple
            lines are supported.
          param3 (int, optional): Description of `param3`, defaults to 0.

        """
        super(Person, self).__init__()
        self.arg = arg
        self.name = ''  # fullname
        self.first_name = ''
        self.last_name = ''
        self.middle_name = ''
        self.biography = {}  # dict or description
        self.birth = ''
        self.death = ''
        self.membership = []  # is currently member of.
        self.affilations = []

    def is_cited_by(self, author):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        return

    def is_cited_in(self, publication):

        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        return

    def researches(self, topic):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        return

    def is_coauthor_of(self, publication, person):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        return

    def get_keywords(self):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        return

    def get_editorship(self):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        return

    def is_editor_of(self):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """

        return

    def get_publications_mentioned_in(self):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        return

    def defined_concept(self, concept):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        return

    def person_used_concept(self, concept):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        return


class Publication(object):
    """The summary line for a class docstring should fit on one line.

    If the class has public attributes, they should be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section.

    Attributes:
      attr1 (str): Description of `attr1`.
      attr2 (list of str): Description of `attr2`.
      attr3 (int): Description of `attr3`."""

    def __init__(self, arg):
        """Example of docstring on the __init__ method.

        The __init__ method may be documented in either the class level
        docstring, or as a docstring on the __init__ method itself.

        Either form is acceptable, but the two should not be mixed. Choose one
        convention to document the __init__ method and be consistent with it.

        Note:
          Do not include the `self` parameter in the ``Args`` section.

        Args:
          param1 (str): Description of `param1`.
          param2 (list of str): Description of `param2`. Multiple
            lines are supported.
          param3 (int, optional): Description of `param3`, defaults to 0.

        """
        super(Publication, self).__init__()
        self.arg = arg
        self.name = ''
        self.data = ''
        self.place = ''
        self.author = ''
        self.kind = ''
        self.journal = ''
        self.collection = ''

    def get_abstract(self):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        return

    def get_content(self):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        return

    def get_tables(self):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        return

    def get_claims(self):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        return

    def get_theories(self):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        return

    def get_discipline(self):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        return

    def get_used_tools(self):
        """Class methods are similar to regular functions.

        Note:
            A note

        Args:
            param1: The first parameter.

        Returns:
            Description of return
        """
        return


"get is save load update dump create compare fuse"
