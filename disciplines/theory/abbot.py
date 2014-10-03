
# from chaos of disciplines. Maybe a decorator?
methods = {
	'quantitative':{
		'quantitative':['regression'],
		'qualitative':['scaling','clustering']},
	'qualitative':{
		'quantitative':['formal measure of culturer'],
		'qualitative':['pure interpretation']}}


figure_1_3 = {
	'culture': {
		'culture': {'culture':'Sahlins', 'social structure':''},
		'social structure': {'culture': 'Marx', 'social structure': None}},
	'social structure':{
		'culture': None, 
		'social structure': None}}


figure_1_4 = {
	'history': {'mainstream': None, 'social science history': None},
	'sociology': {'historical sociology': None, 'mainstream': None} 
}

figure_1_5 = ['conflict', 'consensus'] # make tree out of this
leafs = ['liberal economics', 'rational choice', 'conflict sociology', '1960 mainstream']

bySmall ='''
Abbot elaborates further on where these jurisdictional contests may
occur. He suggests they generally take place in three di¡erent ``arenas'':
the legal arena, where practitioners attempt to obtain a legal license; in
the media or public arena, where they attempt to convince the public
of their authority over the practice; and in the work site itself, where
practices are actually carried out. Boundary-work takes place in all
arenas. Consequently, it takes place before di¡erent sets of audiences ^
judges, policy-makers, journalists ^ and in the interest of securing
di¡erent resources.39 Thus, when obstetricians attempt to obtain legal
licenses (one resource) from law-makers (one audience) in the legal
arena, they are required to perform di¡erent boundary-work from
that required when they attempt to obtain political support (another
resource) from journalists (a di¡erent audience) in the public arena.
'''


boundary_work_arena = 'all'
legal_arena = 'Where is it happening'
media_or_public_arena = 'Where is it happening'
work_site_itself = 'Where is it happening'

boundary_work_arenas = [legal_arena, media_or_public_arena, work_site_itself]





judges = None
policy_makers = None
journalists = None
political_support = None
obtain_political_support = None

from pprint import pprint
pprint(figure_1_3)
pprint(figure_1_4)