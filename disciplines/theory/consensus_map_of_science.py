# -*- coding: utf- -*-
#consensus_map_of_science
#



name_dict = {
    'M' : 'Mathematics ',
    'B' : 'Biology',
    'CS' : 'Computer science ',
    'I' : 'Infectious disease',
    'P' : 'Physics ',
    'MD' : 'Medical specialties',
    'PC' : 'Physical chemistry ',
    'HS' : 'Health services',
    'C' : 'Chemistry ',
    'N' : 'Brain research (neuroscience)', #two names
    'E' : 'Engineering',
    'PS' : 'Psychology/psychiatry',
    'G' : 'Earth sciences (geoscience)', #two names
    'SS' : 'Social sciences',
    'BC' : 'Biochemistry',
    'H' : 'Humanities'}



TABLE_3 = {
    'name': 'Consensus pairs of scientific areas from 20 maps of science',
    'columns':['Rank', 'Pair', 'N', 'N-poss', '%'],
    'table': [
        [1, 'B', 'BC', 20, 20, 100.0],
        [2, 'I','MD', 20, 20, 100.0],
        [3, 'H','SS', 8, 8, 100.0],
        [4, 'C','PC', 19, 20, 95.0],
        [5, 'HS','MD', 16, 17, 94.1],
        [6, 'PS','SS', 16, 17, 94.1],
        [7, 'P', 'PC', 18, 20, 90.0],
        [8, 'MD','N', 16, 18, 88.9],
        [9, 'E','G', 16, 18, 88.9],
        [10, 'B','G', 17, 20, 85.0],
        [11, 'BC','I', 16, 20, 80.0],
        [12, 'E','PC', 14, 18, 77.8],
        [13, 'N','PS', 14, 18, 77.8],
        [14, 'CS','M', 13, 18, 72.2],
        [15, 'BC','MD', 14, 20, 70.0],
        [16, 'BC','C', 14, 20, 70.0],
        [17, 'E','P', 12, 18, 66.7],
        [18, 'B','I', 13, 20, 65.0],
        [19, 'CS','SS', 10, 16, 62.5],
        [20, 'H','PS', 5, 8, 62.5],
        [21, 'M','P', 11, 19, 57.9],
        [22, 'C','E', 10, 18, 55.6],
        [23, 'C','P', 11, 20, 55.0],
        [24, 'HS', 'N', 8, 15, 53.3],
        [25, 'CS','E', 9, 17, 52.9],
        [26, 'C','G', 10, 20, 50.0],
        [27, 'HS','PS', 8, 16, 50.0]]}
        
        
#also interesting
Appendix_A='''
Appendix_A = 'Matrix of Edges by Map'
B;I-BC 
B;I-C  
B;I-MD;N 
B;I-PS  
B-B;I 
B-BC
B-BC;I  
B-BC;I;MD   
B-C     
BC;I;MD-C  
BC;I;MD-CS  
BC;I;MD-I   
BC;I;MD-M  
BC;I;MD-MD   
BC;I;MD-N   
BC;I;MD-P  
BC;I;MD-PC  
BC;I;MD-PS  
BC;I;MD-SS  
BC;I-C;PC  
BC;I-E  
BC;I-MD  
BC;I-N  
BC;I-PS;SS  
B-C;PC   
BC-BC;I;MD   
BC-C          
BC-C;P;PC  
BC-C;PC    
BC-CS   
BC-G
BC-HS;I;MD  
BC-HS;MD  
BC-I          
BC-I;MD;N  
BC-MD          
BC-N  
BC-N;PS  
BC-PC  
B-E      
B-G     1        
B-HS;I;MD  
B-I   
B-I;MD;N  
B-M  
B-MD 
B-N  
B-P  
B-PS;SS  
C;P;PC-E 
C;PC-CS  
C;PC-E  
C;PC-G 
C;PC-P   
C;PC-PC 
C-E    
C-G     
C-HS;MD 
C-MD 
C-N;PS 
C-P   
C-PC       
CS-E     
CS-G 
CS-H;SS  
CS-M       
CS-MD 
CS-N 
CS-P
CS-PC  
CS-SS  
E-G         
E-M     
E-MD 
E-P      
E-PC      
E-PS;SS 
E-SS  
G-M  
G-P    
G-PC 
G-PS;SS 
H;SS-N 
H;SS-PS  
H-M 
H-PS;SS  
HS;I;MD-MD 
HS;I;MD-N  
HS;I;MD-PS;SS
HS;MD-I 
HS-I 
HS-I;MD;N 
HS-MD      
HS-N   
HS-PS   
HS-PS;SS  
H-SS 
I;MD;N-PS;SS 
I-MD      
MD;N-PS 
MD-N     
MD-N;PS 
MD-PS 
M-MD;N 
M-P      
M-PS 
M-PS;SS 
M-SS   
N-PS
P-PC       
PS;SS-SS 
PS-SS
'''
