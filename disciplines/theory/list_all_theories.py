import os 

def do():
    thelist = [
    'emergence', 
    'characterisation_of_organisational_structures',
    'interdisciplinary_models',
    'justifications_for_interdisciplinary_work',
    'learning_styles_and_disciplinary_differences',
    'power_strugles',
    'regimes_of_knowledge_production',
    'structuring_of_research_fields',
    'taxonomy_of_interdisciplinarity']
    for x in sorted(thelist):
        print x

'''
def do():
    current_dir = os.getcwd()
    theories_dir = current_dir+r'/disciplines/theory'
    for x in os.listdir(theories_dir):
        print x
'''
