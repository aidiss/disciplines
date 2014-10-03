# -*- coding: utf-8 -*-
#phenomenon.py
"""This module describes different objects analyzed within the framework

This module is related with data\classes.py
"""

['person', 'profession' 'event', 'publication', 'concept', 'definition', 'organization', 'disciplines']

person = ''
"""Person

Person is a human being, an individual. We are interested in persons who 
are considered to be *member of academic disciplines*, the category overlaps
with *researcher*, *scientist*. In other case it overlaps with, dean, head editor. 
On one more scale it overlaps with *philosopher*, *economist* and etc.

Data about persons can be access from dbpedia.
"""

event = ''
"""Event is when something happens, a distinct point and time, might be 
more spatial or more time-period related.In list of events we can see 
such as conference o phd aqcuirement procedure (more time related)
Howver, we will use event more for spatial occurances rather than time 
related.

From:
    - dbpedia
    - online conference listings
"""

publication = ''
""" An organized dissemination of some kind of text. ussualy it has 
person or institution related *publisher* and *text* that is released. 
Every publication has *claims*, *statements* and *propositions*.
Publications are interesting because they are prime communication tool
From:
    publishers
    arxiv
    open access
    
"""

concept = ''
""" Concept

Concept is an idea in relation with a symbol that represents the idea. 
In our case we work with textual concepts that are expressed textually.
We unrestand the fact that concepts appear differenty and we will track 
their semantic and other relations. To list some concepts *discipline*, 
*understanding*, *scientific*, *transdisciplinary*. Concepts appear in 
text. *definitions*
Were to get them:
    - dictionaries,
    - books
    - articles."""


organization = ''
"""A grouping of intercting people.

Organization is something that relates.
*Universities*, *learned societies*, *publishers*.

Where:
    dbpedia
"""


institution = ""

Research community = "Academia and universities; research institutes - see sociology of science"

