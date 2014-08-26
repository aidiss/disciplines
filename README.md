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

The main packages:
- theory
- data
- method
- drawing
- describe
- web


Development strategy
-----
1. Prototype with theory that describes small phenomenon.

Use of examples. L
iterature provides us with many examples. 
- In some cases examples are just a mentioning of some discipline or subdiscipline.
- In other cases we have examples that are described in 5 to 10 sentences. 
- In some unique casese we have long descriptions of each discipline (Small, history of social sciences)

We have a strategy:
1. List all disciplines and to which theories (including methods) are they related.
2. List all disciplines that have description
3. Tackle big descriptions by using earlier findings and NLP (NLTK).
4. Reverse findings on less documented cases.
5. Estimate or build a strategy for developing rarely mentioned cases.
6. Based on findings of stages 1 to 5, investigate disciplinary formations not mentioned in theory.

Dependencies
-----------

Disciplines uses a number of open source projects to work properly:

* [pandas]
* [networkx]
* [matplotlib]
* [bokeh]
* [sqlite3]


Some outhors like [Vinck], [Lyall], [Klein].

Concepts as [interdisciplinarity], [multidisciplinarity], [transdisciplinarity]
Events like [Interdisciplinarity: How to make it work], [Academic demarcations]
Disciplines like [philosophy], [law], [medicine], [theology], [physics], [chemistry], [sociology], [economics] and many many many more.

Learned societies like ...,...,... and others in [List of learned societies]

Installation
--------------

Later...

License
----
MIT

[Vinck]:http://epr.ist.utl.pt/~epr.daemon/EPGC/index.php/dominique-vinck
[Lyall]:http://www.sps.ed.ac.uk/staff/science_technology_and_innovation_studies/lyall_catherine
[Klein]:http://csid.unt.edu/about/people/klein/

[interdisciplinarity]:https://en.wikipedia.org/wiki/Interdisciplinary
[multidisciplinarity]:https://en.wikipedia.org/wiki/multidisciplinarity
[transdisciplinarity]:https://en.wikipedia.org/wiki/transdisciplinarity

[law]:https://en.wikipedia.org/wiki/Law
[medicine]:https://en.wikipedia.org/wiki/medicine
[theology]:https://en.wikipedia.org/wiki/theology
[philosophy]:https://en.wikipedia.org/wiki/philosophy
[sociology]:https://en.wikipedia.org/wiki/sociology
[economics]:https://en.wikipedia.org/wiki/economics
[chemistry]:https://en.wikipedia.org/wiki/chemistry
[physics]:https://en.wikipedia.org/wiki/physics

[esf peerreview guide]:http://www.esf.org/coordinating-research/mo-fora/peer-review.html

[Interdisciplinarity: How to make it work]:http://www.ljms.lt/interdisciplinarity/home
[Academic demarcations]:http://www.uio.no/english/research/interfaculty-research-areas/plurel/news-and-events/events/external/2012/academic_demarcations.html

[List of learned societies]:https://en.wikipedia.org/wiki/List_of_learned_societies

Barre, R., Hernandez, V., Meyer, J. B., & Vinck, D. (2003). Scientific diasporas. Paris: IRD Editions.
The sociology of scientific work. The fundamental relationship between science and society
Ziman JM (1987) An Introduction to Science Studies. 


[more.md][more.md]




