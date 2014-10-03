#Knowledge_flows.py
"""
Knowledge flows – Analyzing the core literature of innovation, entrepreneurship
and science and technology studies

Samyukta Bhupatirajua, Önder Nomalerb, Giorgio Triulzi a, Bart Verspagena,∗
"""

abstract = '''
This paper applies network analysis to a citation database that combines the key references in the fields
of Entrepreneurship (ENT), Innovation Studies (INN) and Science and Technology Studies (STS). We find
that citations between the three fields are relatively scarce, as compared to citations within the fields.
As a result of this tendency, a cluster analysis of the publications in the database yields a partition that
is largely the same as the a priori division into the three fields. We take this as evidence that the three
fields, although they share research topics and themes, have developed largely on their own and in relative
isolation from one another. We also apply a so-called ‘main path’ analysis aimed at outlining the main
research trajectories in the field. Here we find important differences between the fields. In STS, we find
a cumulative trajectory that develops in a more or less linear fashion over time. In INN, we find a major
shift of attention in the main trajectory, from macroeconomic issues to business-oriented research. ENT
develops relatively late, and shows a trajectory that is still in its infancy.
'''

keywords ='''
Innovation studies
Entrepreneursip
Science and technology studies
Citation networks
Network analysis
'''

throughput ='''
These papers are ranked on “throughput”, which is defined as the
number of (direct) citations that a paper makes (to other papers in
the database) multiplied by the number of citations that the paper
receives (by other papers in the database). The throughput measure
is somewhat similar to the weights that the Hummon and Doreian
procedure assigns, the main difference being that only direct
citations are taken into account.
'''

table1 = {
'name':'Top-10 documents in terms of “throughput” (entire database).',
'columns':['Document', 'Field', 'In main path network of', '#Citations received', '#Citations made', 'Throughput (cit. made×cit. received)'],
'table':[
	['Nelson and Winter (1982)','INN/ENT/STS','Never', 50, 28, 1400],
	['Latour and Woolgar (1979)', 'STS', 1980, 1990, 2002, 55, 15, 825],
	['Dosi et al. (1988)', 'INN', 1990, 2002, 12, 59, 708],
	['Bijker et al. (1987)', 'STS', 'Never', 19, 37, 703],
	['Dosi (1988)', 'INN', 1990, 13, 41, 533],
	['Rosenberg (1982)', 'INN', 'Never', 28, 19, 532],
	['Collins (1985)', 'STS', 1990, 2002, 24, 22, 528],
	['Porter (1990)', 'INN/ENT', 2002, 26, 20, 520],
	['Latour (1987)', 'STS', 1990, 2002, 30, 17, 510],
	['Freeman (1974)' ,'INN/STS', 1980, 1990, 2002, 39, 13, 507]]}