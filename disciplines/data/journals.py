# -*- coding: utf-8 -*-
#journals.py
"""Journals are particular kind of publication.

They have different publications in them by different authors.
Journals are periodical. Journals are made by publishers. Authors publish
in journals. Journals contain articles. Journals have associated editors.
Journals have.

There is a limited number of journals we have interest. For know we can 
separated two groups of journals. First group of journals contain 
interesting theoretical claims that we base our research on. Second 
group of journals are mor einterested as a source of data.

First group consist of around 50 journals.
Second group is way larger.
"""
import pandas as pd

class Journal():
    __self__ = ''
    editors = []
    publications = []
    volumes = None
    established = 'timestamp'
    authors_who_published = []
    journals_that_cited_this_journal = []
    
s4 = Journal


source_url = 'http://www.4sonline.org/resources/journals'
url = r'C:\Users\Saonkfas\Documents\GitHub\disciplines\disciplines\data\xlsx\sts books and journals.xlsx'
df = pd.read_excel(url, header=None )
df.columns = ['name', 'url']
