# -*- coding: utf-8 -*-
"""
Biglans classification

This can be used for machine learning.
3 dimensions are investigated by Biglan:
	pure - applied
	hard - soft
	life - non-life
"""

author = 'Biglan'
authors = author
concepts = []
data = []
claim = []
theory = '''
	'''
approach =  ''
reading = '''
	1. Ruth Neumann, Disciplinarity,  In Tight Malcolm, Ka Ho Mok, Jeroen Huisman, Christopher C. Morphew (Ed.), The Rutledge International Handbook of Higher Education, Routledge, USA, pp 487-500, 2009.
	2. Yonghong Jade Xu, Faculty Turnover: Discipline-Specific Attention is Warranted, Res earsch in High  Educ ation. Springer, Vol. 49, pp 40–61, Feb 2008.   
	3. Matthew Kwok, Disciplinary Differences in the Development of Employability Skills of Recent University Graduates in         Manitoba: Some Initial Findings. Higher Education Perspectives, volume 1, issue 1, pp.60-77, 2004.       
	4. Biglan, A., The characteristics of subject matter in academic areas, Journal of Applied Psychology, 57, 195–203, 1973. 
	5. Malaney, G. D., Differentiation in graduate education, Research in Higher Education, 25(1), pp 82–96, 1986. 
	6. Design of Interventions for Instructional Reform in Software Development Education for Competency Enhancement: Summary of PhD Thesis
	7. Assess Your Curriculum and Courses Using Harden’s Taxonomy of Curriculum Integration
	8. Software Development Education: Breadth Courses for Developing Domain Competence and Systems Thinking
	'''
urls = 'http://goelsan.wordpress.com/2010/07/27/biglans-classification-of-disciplines/'
further = [
	'http://cpr.iub.edu/uploads/AACU2008Tables.pdf', 
	'Effective Educational Practices and Essential Learning Outcomes in General Education Courses: Differences by Discipline']



the_classification = [
    [['Biology', 'Biochemistry', 'Genetics', 'Physiology'], {'pure':True, 'hard':True, 'life':True}],
    [['Mathematics', 'Physics', 'Chemistry', 'Geology', 'Astronomy', 'Oceanography'], {'pure':True, 'hard':True, 'life':False}],
    [['Psychology', 'Sociology', 'Anthropology', 'Political Science', 'Area Study'], {'pure':True, 'hard':False, 'life':True}],
    [['Linguistics', 'Literature', 'Communications', 'Creative Writing', 'Economics', 'Philosophy', 'Archaeology', 'History', 'Geography'], {'pure':True, 'hard':False, 'life':True}],
    [['Agriculture', 'Psychiatry', 'Medicine', 'Pharmacy', 'Dentistry', 'Horticulture'], {'pure':False, 'hard':True, 'life':True}],
    [['Civil Engineering', 'Telecommunication Engineering', 'Mechanical Engineering', 'Chemical Engineering', 'Electrical Engineering', 'Computer science'], {'pure':False, 'hard':True, 'life':False}],		
    [['Recreation', 'Arts', 'Education', 'Nursing', 'Conservation', 'Counseling', 'HR Management'], {'pure':False, 'hard':False, 'life':True}],
    [['Finance', 'Accounting', 'Banking', 'Marketing', 'Journalism', 'Library And Archival Science', 'Law', 'Architecture', 'Interior Design', 'Crafts', 'Arts', 'Dance', 'Music'], {'pure':False, 'hard':False, 'life':False}]
    ]

#it is interesting that he himself does outline "etc." what doe 'etc' mean here?
#notebook should contain link to the table itself