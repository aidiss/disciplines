#learned_societies.py
"""DEPRECATED
THIS MODULE COULD BECOME DESCRIPTION OF LEARNED SOCIETIES CLASS.
CURRENTLY GATHERED INFORMATION HAS TO BE STORRED SOMEWHERE. JSON?
Module dedicated to getting data about learned societies

The module is connecting to different websites that unite different
learned societies.

Currently implemented things:
	- Scrapping of ACLS website 

Urls:
	- Urls to dbpedia are here. They will be parsed using dbpedia module."""

learned_societies_urls = [{'url': 'http://en.wikipedia.org/wiki/Category:Learned_societies'},
	{'url' : 'http://en.wikipedia.org/wiki/Category:Facilities_and_organizations_of_science'},
	{'url' : 'http://en.wikipedia.org/wiki/Category:Scientific_societies'}]

url = 'https://www.acls.org/societies/'

acls_members = [
	['African Studies Association',	'https://www.acls.org/societies/societies.aspx?sid=363E4D14-98A2-DB11-A735-000C29\03E717',''],
	['American Academy of Arts and Sciences',	'https://www.acls.org/societies/societies.aspx?sid=08895C50-C9A2-DB11-A735-000C2903E717',''],
	['American Academy of Religion'	,'https://www.acls.org/societies/societies.aspx?sid=0B895C50-C9A2-DB11-A735-000C2903E717',''],
	['American Anthropological Association', 'https://www.acls.org/societies/societies.aspx?sid=0E895C50-C9A2-DB11-A735-000C2903E717',''],
	['American Antiquarian Society', 'https://www.acls.org/societies/societies.aspx?sid=11895C50-C9A2-DB11-A735-000C2903E717',''],
	['American Association for the History of Medicine', 'https://www.acls.org/societies/societies.aspx?sid=5405940B-81A3-DB11-A735-000C2903E717',''],
	['American Comparative Literature Association',	'https://www.acls.org/societies/societies.aspx?sid=2F895C50-C9A2-DB11-A735-000C2903E717',''],
	['American Dialect Society', 'https://www.acls.org/societies/societies.aspx?sid=38895C50-C9A2-DB11-A735-000C2903E717',''],
	['American Economic Association', 'https://www.acls.org/societies/societies.aspx?sid=3B895C50-C9A2-DB11-A735-000C2903E717',''],
	['American Folklore Society', 'https://www.acls.org/societies/societies.aspx?sid=3E895C50-C9A2-DB11-A735-000C2903E717',''],
	['American Historical Association',	'https://www.acls.org/societies/societies.aspx?sid=41895C50-C9A2-DB11-A735-000C2903E717',''],
	['American Musicological Society',	'https://www.acls.org/societies/societies.aspx?sid=4A895C50-C9A2-DB11-A735-000C2903E717',''],
	['American Numismatic Society', 'https://www.acls.org/societies/societies.aspx?sid=4D895C50-C9A2-DB11-A735-000C2903E717',''],
	['American Oriental Society', 'https://www.acls.org/societies/societies.aspx?sid=50895C50-C9A2-DB11-A735-000C2903E717',''],
	['American Philosophical Association',	'https://www.acls.org/societies/societies.aspx?sid=56895C50-C9A2-DB11-A735-000C2903E717',''],
	['American Philosophical Society',	'https://www.acls.org/societies/societies.aspx?sid=59895C50-C9A2-DB11-A735-000C2903E717',''],
	['American Political Science Association',	'https://www.acls.org/societies/societies.aspx?sid=5C895C50-C9A2-DB11-A735-000C2903E717',''],
	['American Schools of Oriental Research',	'https://www.acls.org/societies/societies.aspx?sid=65895C50-C9A2-DB11-A735-000C2903E717',''],
	['American Society for Aesthetics','https://www.acls.org/societies/societies.aspx?sid=68895C50-C9A2-DB11-A735-000C2903E717',''],
	['American Society for Eighteenth-Century Studies','https://www.acls.org/societies/societies.aspx?sid=6B895C50-C9A2-DB11-A735-000C2903E717',''],
	['American Society for Environmental History',	'https://www.acls.org/societies/societies.aspx?sid=563A7C1E-81A3-DB11-A735-000C2903E717',''],
	['American Society for Legal History	','https://www.acls.org/societies/societies.aspx?sid=6E895C50-C9A2-DB11-A735-000C2903E717',''],
	['American Society for Theatre Research',	'https://www.acls.org/societies/societies.aspx?sid=71895C50-C9A2-DB11-A735-000C2903E717',''],
	['American Society of Church History',	'https://www.acls.org/societies/societies.aspx?sid=4A0E4AF8-80A3-DB11-A735-000C2903E717',''],
	['American Society of Comparative Law',	'https://www.acls.org/societies/societies.aspx?sid=74895C50-C9A2-DB11-A735-000C2903E717',''],
	['American Society of International Law',	'https://www.acls.org/societies/societies.aspx?sid=77895C50-C9A2-DB11-A735-000C2903E717',''],
	['American Sociological Association',	'https://www.acls.org/societies/societies.aspx?sid=7A895C50-C9A2-DB11-A735-000C2903E717',''],
	['American Studies Association','https://www.acls.org/societies/societies.aspx?sid=7D895C50-C9A2-DB11-A735-000C2903E717',''],
	['Archaeological Institute of America',	'https://www.acls.org/societies/societies.aspx?sid=A7895C50-C9A2-DB11-A735-000C2903E717',''],
	['Association for Asian Studies',	'https://www.acls.org/societies/societies.aspx?sid=CE895C50-C9A2-DB11-A735-000C2903E717',''],
	['Association for Jewish Studies',	'https://www.acls.org/societies/societies.aspx?sid=D4895C50-C9A2-DB11-A735-000C2903E717',''],
	['Association for Slavic, East European, and Eurasian Studies',	'https://www.acls.org/societies/societies.aspx?sid=1A895C50-C9A2-DB11-A735-000C2903E717',''],
	['Association for the Advancement of Baltic Studies',	'https://www.acls.org/societies/societies.aspx?sid=D7895C50-C9A2-DB11-A735-000C2903E717',''],
	['Association of American Geographers','https://www.acls.org/societies/societies.aspx?sid=DD895C50-C9A2-DB11-A735-000C2903E717',''],
	['Association of American Law Schools',	'https://www.acls.org/societies/societies.aspx?sid=E0895C50-C9A2-DB11-A735-000C2903E717',''],
	['Bibliographical Society of America',	'https://www.acls.org/societies/societies.aspx?sid=7F8A5C50-C9A2-DB11-A735-000C2903E717',''],
	['College Art Association',	'https://www.acls.org/societies/societies.aspx?sid=5539555D-8673-DB11-A735-000C2903E717',''],
	['College Forum of the National Council of Teachers of English',	'https://www.acls.org/societies/societies.aspx?sid=16A44F5C-C9A2-DB11-A735-000C2903E717',''],
	['Dictionary Society of North America','https://www.acls.org/societies/societies.aspx?sid=C1A44F5C-C9A2-DB11-A735-000C2903E717',''],
	['Economic History Association',	'https://www.acls.org/societies/societies.aspx?sid=06A54F5C-C9A2-DB11-A735-000C2903E717',''],
	['German Studies Association',	'https://www.acls.org/societies/societies.aspx?sid=DBA54F5C-C9A2-DB11-A735-000C2903E717',''],
	['Hispanic Society of America','https://www.acls.org/societies/societies.aspx?sid=65A64F5C-C9A2-DB11-A735-000C2903E717',''],
	['History of Science Society',	'https://www.acls.org/societies/societies.aspx?sid=6BA64F5C-C9A2-DB11-A735-000C2903E717',''],
	['International Center of Medieval Art',	'https://www.acls.org/societies/societies.aspx?sid=82B30AFF-80A3-DB11-A735-000C2903E717',''],
	['Latin American Studies Association',	'https://www.acls.org/societies/societies.aspx?sid=37014862-C9A2-DB11-A735-000C2903E717',''],
	['Law and Society Association','https://www.acls.org/societies/societies.aspx?sid=40014862-C9A2-DB11-A735-000C2903E717',''],
	['Linguistic Society of America',	'https://www.acls.org/societies/societies.aspx?sid=67014862-C9A2-DB11-A735-000C2903E717',''],
	['Medieval Academy of America',	'https://www.acls.org/societies/societies.aspx?sid=09024862-C9A2-DB11-A735-000C2903E717',''],
	['Metaphysical Society of America',	'https://www.acls.org/societies/societies.aspx?sid=2D024862-C9A2-DB11-A735-000C2903E717',''],
	['Middle East Studies Association of North America'	,'https://www.acls.org/societies/societies.aspx?sid=4E024862-C9A2-DB11-A735-000C2903E717',''],
	['Modern Language Association of America'	,'https://www.acls.org/societies/societies.aspx?sid=81024862-C9A2-DB11-A735-000C2903E717',''],
	['National Communication Association',	'https://www.acls.org/societies/societies.aspx?sid=05034862-C9A2-DB11-A735-000C2903E717',''],
	['National Council on Public History',	'https://www.acls.org/societies/societies.aspx?sid=5705940B-81A3-DB11-A735-000C2903E717',''],
	['North American Conference on British Studies',	'https://www.acls.org/societies/societies.aspx?sid=EF4AB5CB-EE16-DC11-9D54-000C2903E717',''],
	['Oral History Association'	,'https://www.acls.org/societies/societies.aspx?sid=B157EC10-B4DA-E311-9BEC-000C29A3451A',''],
	['Organization of American Historians'	,'https://www.acls.org/societies/societies.aspx?sid=CA5D4068-C9A2-DB11-A735-000C2903E717',''],
	['Renaissance Society of America',	'https://www.acls.org/societies/societies.aspx?sid=845E4068-C9A2-DB11-A735-000C2903E717',''],
	['Rhetoric Society of America',	'https://www.acls.org/societies/societies.aspx?sid=A08A031B-3C28-DD11-B38E-000C2903E717',''],
	['Sixteenth Century Society and Conference'	,'https://www.acls.org/societies/societies.aspx?sid=D07233A5-7FA3-DB11-A735-000C2903E717',''],
	['Society for American Music',	'https://www.acls.org/societies/societies.aspx?sid=B95F4068-C9A2-DB11-A735-000C2903E717',''],
	['Society for Cinema and Media Studies',	'https://www.acls.org/societies/societies.aspx?sid=BC5F4068-C9A2-DB11-A735-000C2903E717',''],
	['Society for Classical Studies',	'https://www.acls.org/societies/societies.aspx?sid=53895C50-C9A2-DB11-A735-000C2903E717',''],
	['Society for Ethnomusicology',	'https://www.acls.org/societies/societies.aspx?sid=A31B3B6E-C9A2-DB11-A735-000C2903E717',''],
	['Society for French Historical Studies',	'https://www.acls.org/societies/societies.aspx?sid=A61B3B6E-C9A2-DB11-A735-000C2903E717',''],
	['Society for Military History','https://www.acls.org/societies/societies.aspx?sid=820AEE76-D65D-DF11-BC5E-000C293A51F7',''],
	['Society for Music Theory',	'https://www.acls.org/societies/societies.aspx?sid=85B30AFF-80A3-DB11-A735-000C2903E717',''],
	['Society for the Advancement of Scandinavian Study',	'https://www.acls.org/societies/societies.aspx?sid=BBF41A18-81A3-DB11-A735-000C2903E717',''],
	['Society for the History of Technology',	'https://www.acls.org/societies/societies.aspx?sid=A91B3B6E-C9A2-DB11-A735-000C2903E717',''],
	['Society of Architectural Historians'	,'https://www.acls.org/societies/societies.aspx?sid=AF1B3B6E-C9A2-DB11-A735-000C2903E717',''],
	['Society of Biblical Literature',	'https://www.acls.org/societies/societies.aspx?sid=B21B3B6E-C9A2-DB11-A735-000C2903E717',''],
	['Society of Dance History Scholars',	'https://www.acls.org/societies/societies.aspx?sid=B51B3B6E-C9A2-DB11-A735-000C2903E717',''],
	['World History Association',	'https://www.acls.org/societies/societies.aspx?sid=B1F02D93-E77B-E011-B81F-000C293A51F7', '']]

def initiative_for_science_in_europe():
	'''ISE'''
	
	members = [
		['European Acoustics Association', 'EAA','http://www.eaa-fenestra.org/',''],
		['European Association for Chemical and Molecular Sciences', 'EUChemS','http://www.euchems.org/',''],
		['European Association of Social Anthropologists', 'EASA','http://www.easaonline.org/',''],
		["European Biophysical Societies' Association", 'EBSA','http://www.ebsa.org/',''],
		['European CanCer Organization', 'ECCO','http://www.ecco-org.eu/',''],
		['European Crystallographic Association' ,'ECA', 'http://www.ecanews.org/',''],
		['European Educational Research Association', 'EERA', 'http://www.eera-ecer.eu/',''],
		['European Glaucoma Society', 'EGS', 'http://www.eugs.org/',''],
		['European Mathematical Society', 'EMS', '', ''],
		['European Molecular Biology Laboratory', 'EMBL', 'http://www.embl.org/',''],
		['EMBO, excellence in life sciences', 'http://www.embo.org/',''],
		['European Physical Society', 'EPS', 'http://www.eps.org/',''],
		['European Plant Science Organisation', 'EPSO','http://www.epsoweb.org/',''],
		['European Society for Gene and Cell Therapy' ,'ESGCT','http://www.esgct.eu/',''],
		['European Society of Endocrinology', 'ESE', 'http://www.ese-hormones.org/',''],
		['European Sociological Association', 'ESA', 'http://www.europeansociology.org/',''],
		['EuroScience', None, 'http://www.euroscience.org/'],
		['Federation of European Biochemical Societies', 'FEBS', 'http://www.febs.org/',''],
		['Pan-European Region of the International Association for Dental Research' 'IADR', 'http://www.iadr.com/']]


	observers= [
		['EIROforum', None, 'http://www.eiroforum.org/'],
		['Eurodoc, the European Council for Doctoral Candidates and Junior Researchers', None, 'http://www.eurodoc.net/'],
		['European Association for Computer Graphics', 'EG','http://www.eg.org/'],
		['European Calcified Tissue Society', 'ECTS','http://www.ectsoc.org/'],
		['European Conference for AeroSpace Sciences', 'ECASS','http://eucass.eu/'],
		['European Coordinating Committee for Artificial Intelligence', 'ECCAI','http://www.eccai.org/'],
		['European Group for Organisational Studies', None, 'http://www.egosnet.org/'],
		['European Neutron Scattering Association', 'ENSA','http://www.unizar.es/ensa/'],
		['Informatics Europe','IE','http://www.informatics-europe.org/'],
		['Young Academy of Europe','YAE','http://www.yacadeuro.org/']]
	return members, observers
	
britsh_LS = ['https://www.britac.ac.uk/links/uksahss.asp?Letter=A', 'https://www.britac.ac.uk/links/uksahss.asp?Letter=B']
letters = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ']
for letter in letters:
	url = 'https://www.britac.ac.uk/links/uksahss.asp?Letter={}'.format(letter)

for x in acls_members:
	print(x[1])