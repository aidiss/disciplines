"""Academic English corpus
http://courses.washington.edu/englhtml/engl560/corplingresources.htm


academic english corpus
"""
import os
url = 'http://www.coventry.ac.uk/research/research-directory/art-design/british-academic-written-english-corpus-bawe/contents-of-the-bawe-corpus/'
lurl = r'g:\Desktop\academic english corpus\2539\CORPUS_TXT'

os.chdir(lurl)
print(len(os.listdir(lurl)))
print(os.listdir(lurl)[0])
f  = open(os.listdir(lurl)[0])

text = f.read()
print(text)

"""
MICASE—Michigan Corpus of Academic Spoken English lets you browse and search for any word in a highly stratified corpus and to download the lecture or speech or conversation transcripts that contain the word. Currently has 152 transcripts totalling 1.8 million tokens.

BASE— The British Academic Spoken English corpus— is made up of 160 lectures and 39 seminars in various disciplines totalling about 1.64M tokens recorded between 2000-2005. Transcripts are available from Warwick Centre for Applied 

BAWE—British Academic Written English— is the counterpart to BASE and can be accessed (after a harmless free registration). The writing in the corpus is of British University students, and can be sorted by genre and discipline. The full corpus (6.7 M words) is available at the Oxford Text Archive.

INTELLITEXT-ACADEMIC presents the results of BootCat collections of web pages using keywords of various disciplines. ABout 70 million tokens in nine academic "genres"/domains.
"""
