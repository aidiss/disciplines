disciplines
===========

A package dedicated to research of academic disciplines.

disciplines
=========

Version
----

0.01

Package is dedicated to analysis of *academic scientific disciplines*. Disciplines in all of its forms and types. All branches, fields, subdisciplines, interdisciplines, 
To achieve that we:
1. implement various *theories* that describe the disciplines.
2. link to *data*, and get it
3. develop *method* that connects data to theories.
4. Visualise, *draw* it - creates different visualization. 
5. *Describe* the findings in natural text.
6. Export it to *web*.

Theories:
Such as *Academic tribes and territories* by Becher, or number of approaches listed in *The sociology of scientific work* by Vinck, or stages of emergence by Ziman.
In this module we prepare a set of of theories. Calls for implementation are also accepted [link][ff]

Data:
Links to dbpedia and other open data.
Description of missing information.
Monitor appearance of resources.
Getting data about disciplines, related conferences, publications, descriptions, syllabuses, pictures, classifications, persons, concepts, collection of urls.
Use of graph(networkx), database(sqlite), dataframe(pandas). 

Methods:
The integration of all defined data and theories. The main idea is to all theories with all available data
Applying theories to data. With having formal approach to theories and different data we can do amazing things.
Basically this module allows hypothesis testing. Allows such complicated stuff as:
history - reconstruction of history. Should be generating text, pictures, people from the data that I have analysed. It should work when asking for "do something based on"

Example:

from disciplines.theory import emergence
print emergence.concepts
> citation network
> hierarchy
> conferences

from disciplines.data import db
from methods import check_fit
check_fit(emergence.concepts, db)
> 'citation network' is available 0.3
> 'hierarchies' are available 0.3
> 'conferences' are available 0.1


Development strategy
-----
1. Prototype with theory that describes small phenomenon.
2. Use of examples.
	- In some cases examples are just a mentioning of some discipline or subdiscipline.
	- In other cases we have examples that are described in 5 to 10 sentences. 
	- In some unique casese we have long descriptions of each discipline (Small, history of social sciences)
3. Reconstruct, deconstruct and forecast
	1. List all disciplines and to which theories (including methods) are they related.
	2. List all disciplines that have description
	3. Tackle big descriptions by using earlier findings and NLP (NLTK).
	4. Reverse findings on less documented cases.
	5. Estimate or build a strategy for developing rarely mentioned cases.
	6. Based on findings of stages 1 to 5, investigate disciplinary formations not mentioned in theory.

Dependencies
-----------

Disciplines uses a number of open source projects to work properly:
* [sqlite3]
* [pandas]
* [networkx]

Installation
--------------
Not yet...

License
----
MIT

Further reading
---
[Documentation](doc/docs.md)

	[Theory](doc/theory.md)
	[Data](doc/data.md)
	[Disciplines](doc/disciplines.md)
	[Method](doc/method.md)
