"""Classifications 

This module contains some academid disciplines

'Economic and Social Research Council'
'http://www.esrc.ac.uk/funding-and-guidance/applicants/proposal-classifications-esrc-disciplines.aspx'


Source: (Holland, 1973, 1997); Smart et al. (2000) 
Refs:
    Holland, J. (1973). Making vocational choices: A theory of careers (1st 
    ed.). Englewood Cliffs, NJ: Prentice-Hall.
    Holland, J. (1997). Making vocational choices: A theory of vocational 
    personalities and work environments (3rd ed.). Odessa, FL: 
    Psychological Assessment Resources.
    Smart, J., Feldman, K.A., & Ethington, C.A. (2000). Academic 
    disciplines: Holland's theory and the study of college students and 
    faculty (1st ed.). Nashville, TN: Vanderbilt University Press.

Notes:
    Might be moved to other part: theories.
"""

Academic_Disciplines_by_Holland_Types = [{
    'type': 'investigative', 
    'disciplines':['biology and life sciences', #
        'economics', 
        'geography', 
        'math/statistics', 
        'physical sciences', 
        'finance', 
        'aeronautical' 
        'engineering', 
        'civil engineering', 
        'chemical engineering', 
        'astronomy', 
        'earth science', 
        'pharmacy', 
        'anthropology', 
        'ethnic studies', 
        'geography', 
        'sociology']},
    {'type': 'artistic', 
    'disciplines': [
        'architecture', 
        {'fine arts': ['art', 'drama', 'music']}, 
        'foreign languages', 
        'English', 
        'music', 
        'speech', 
        'theater',
        'environmental design']},

    {'type': 'social',
    'disciplines':[
        'ethnic studies', 
        'home economics', 
        {'humanities': ('history', 'philosophy', 'religion', 'rhetoric')},  #
        'library science', 
        'physical and health education',  #
        'psychology', 
        {'social sciences': ('anthropology', 'political science', 'social work')}, 
        'education']},

    {'type': 'enterprising',
    'disciplines':[
        'business', 
        'communications', 
        'computer/information science',  #
        'law', 
        'public affairs', 
        'journalism', 
        'marketing', 
        'industrial engineering']}]

other_known_classifications = ['Biglan', 'Lithuanian Research Council', 'Becher', 'Holland', 'Cerit?']
university_structure_classifications = ''
syllabi_content_classification = ''