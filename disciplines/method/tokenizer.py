"""Tokenizer

Tokenizer prepares prepares to look for different expressions by providing rules to look for.

Biology: creates, created, monitors, develops, is guilty of, organizes, provides, denies, proves, proved, generates, stimulates, stipulates, claims.
Biologists

Philosophy develops, is developing, developed.
Philosopher

There is still some data on one of my blogs.

Each formulae will be described. I will list theoretical foundations of it.
"""

import nltk

from nltk.book import text4

text4.concordance("vote")
text4.similar("vote")
text4.collocations()


'''
from nltk.corpus import shakespeare
from nltk import ConditionalFreqDist as CFD
ratings = (('me', 2),('you',10))
ratings_cfd = CFD(ratings)
ratings_cfd.conditions()
#ratings.tabulate()
'''

discipline_name = 'philosophy'
tokenizer = [
    ["neighboring disciplines", None],
    ["perspectives", discipline_name],
    ["perspective on",	discipline_name],
    ["perspectives on",	discipline_name],
    ["approach to",	discipline_name],
    ["methods used by",	discipline_name],
    ["defines", discipline_name],
    ["needs to acknowledge", discipline_name],
    ["acknowledges", discipline_name],

    [discipline_name, 'generates'],
    [discipline_name, 'claimes'],
    [discipline_name, 'proved'],
    [discipline_name, 'proves'],

    [discipline_name, 'is an ally of', discipline_name],
    [discipline_name, 'uses methods of', discipline_name],
    [discipline_name, 'denies claims of', discipline_name],
    [discipline_name, 'supports', discipline_name],
    [discipline_name, 'is also', x, 'of', discipline_name],
    [discipline_name, 'is also', x, 'for', discipline_name],
    [discipline_name, 'is similar to', discipline_name],
    [discipline_name, 'is related', discipline_name],
    [discipline_name, 'uses methods created by', discipline_name],
    [discipline_name, 'uses methods developed by', discipline_name]]
