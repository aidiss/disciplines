#small.py


'''As the professional case is, this process can be conceived as taking
place in di¡erent arenas, which can be thought of as being composed
of di¡erent sets of potential constituencies. In particular, the process,
666
as it regards Afro-Americanists, appears to take place in three, in-
creasingly larger arenas: (1) a local institutional arena, involving local
university administrators, students, and faculty of di¡erent departments,
from which they gain institutional support and capital resources; (2) a
wider academic arena, involving scholars in African-American Studies
and other disciplines, from which they gain academic recognition and
intellectual legitimacy; (3) and a much wider public arena, involving
both politically active black communities and larger constituencies
of journalists, philanthropists, and politicians, from which they gain
political support, as well as capital. Less than arenas in Abbot's strict
sense, these represent di¡erent and increasingly larger circles of in£u-
ence and support where the legitimation of Black Studies appears
crucial for its survival. The practitioners would have to ¢nd speci¢c
constituencies within each, consecutively larger circle, and convince
those particular constituencies of the legitimacy of Black Studies.
Furthermore, they would have to respond to the local, academic, and
public environment or context in which Black Studies is embedded
(I discuss this further below). While the current literature does not
frame itself in these terms, it can be thought of as focusing only on
either the ¢rst or the second arenas. The work of Camic and others,
described previously, has tended to focus largely on the local institu-
tional arena. Recent work in the emergence of disciplines, such as
Gaziano's,40 focus almost exclusively on the academic arena. In his
study of the emergence of human ecology, Gaziano attributes the
latter's development to Robert Park's uses of ``ecology'' as a theoretical
metaphor and his association of biology to sociology ^ processes
taking place exclusively within the theoretical plane ^ ignoring by
and large the reform ethic in the city of Chicago and the sociology
department, or Park's relationship to political activists and reformists,
all of which a¡ected his conception of ``the city.''41 I suggest that
constituencies in all three arenas ^ not only local institutional and
academic arenas but also the wider public arena ^ are, in varying
degrees, potential sources of support for the new enterprise, and as
such, important factors in the development of the latter. The speci¢c
extent to which factors in each arena a¡ect the conception of the new
intellectual enterprise can only be determined empirically.'''

local_institutional_arena = '''
	involving local
	university administrators, students, and faculty of di¡erent departments,
	from which they gain institutional support and capital resources
	'''
players = [
	'university_administrators', 
	'students', 
	'faculty_of_different_departments'
	]
aims = [
	'institutional support'
	'capital resources'
	]

wider_academic_arena = '''
	wider academic arena, involving scholars in African-American Studies
	and other disciplines, from which they gain academic recognition and
	intellectual legitimacy; 
	'''
people = [
	'scholars in African-American Studies', 'other disciplines(, scholars of)'
	]
fight_for = [
	'academic recognition',
	'intellectual recognition'
	]

public_arena = '''... and a much wider public arena, involving
	both politically active black communities and larger constituencies
	of journalists, philanthropists, and politicians, from which they gain
	political support, as well as capital.
	'''
players = ['politically active black communities', 'journalists', 'philanthropists', 'politicians']
fightsfor = ['political support', 'capital']