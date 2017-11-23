# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 14:02:09 2017

@author: Garsdal
"""

#-----------------------------------------------------------------------------

import numpy as np
import math

#-----------------------------------------------------------------------------

def roundGrade(grades):
    
    grade1 = np.array([-3,00])
    grade2 = np.array([00,2])
    grade3 = np.array([2,4])
    grade4 = np.array([4, 7])
    grade5 = np.array([7,10])
    grade6 = np.array([10,12])
    
    gradesRounded = np.zeros(len(grades))
    
#-----------------------------------------------------------------------------
    
    for i in range (len(grades)):
        
#-----------------------------------------------------------------------------
        
        #tjekker om karakteren er mellem -3 og 00
        if (grades[i] > -3) and (grades[i] < 00):
            
            #afstanden mellem 00 og karakter er større end mellem karakter og -3
            if (abs(grades[i]-(-3))) < (abs(grades[i]-(00))):
        
                #afrund til -3
                gradesRounded[i] = grade1[0]
            
            #afstanden mellem -3 og karakter er større end mellem karakter og 00
            elif (abs(grades[i]-(-3))) > (abs(grades[i]-(00))):
            
                #afrund til 00
                gradesRounded[i] = grade1[1]
                
#-----------------------------------------------------------------------------
                
        #tjekker om karakteren er mellem 00 og 02
        elif (grades[i] > 0) and (grades[i] < 2):
            
            #afstanden mellem karakteren og 2 er større end mellem karakteren og 0
            if (abs(grades[i]-(0))) < (abs(grades[i]-(2))):
                
                #afrund til 00
                gradesRounded[i] = grade2[0]
                
            elif (abs(grades[i]-(0))) > (abs(grades[i]-(2))):
                
                #afrund til 02
                gradesRounded[i] = grade2[1]

#-----------------------------------------------------------------------------
    
        #tjekker om karakteren er mellem 02 og 04
        elif (grades[i] > 2) and (grades[i] < 4):
            
            if (abs(grades[i]-(2))) < (abs(grades[i]-(4))):
                
                #afrund til 2
                gradesRounded[i] = grade3[0]
                
            elif (abs(grades[i]-(2))) > (abs(grades[i]-(4))):
                
                #afrund til 4
                gradesRounded[i] = grade3[1]

#-----------------------------------------------------------------------------
            
        #tjekker om karakteren er mellem 04 og 7
        elif (grades[i] > 4) and (grades[i] < 7):
            
            if (abs(grades[i]-(4))) < (abs(grades[i]-(7))):
                
                #afrund til 4
                gradesRounded[i] = grade4[0]
                
            elif (abs(grades[i]-(4))) > (abs(grades[i]-(7))):
                
                #afrund til 7
                gradesRounded[i] = grade4[1]
            
#-----------------------------------------------------------------------------
            
        #tjekker om karakteren er mellem 7 og 10
        elif (grades[i] > 7) and (grades[i] < 10):
            
            if (abs(grades[i]-(7))) < (abs(grades[i]-(10))):
                
                #afrund til 7
                gradesRounded[i] = grade5[0]
                
            elif (abs(grades[i]-(7))) > (abs(grades[i]-(10))):
                
                #afrund til 10
                gradesRounded[i] = grade5[1]
            
#-----------------------------------------------------------------------------
            
        #elif #tjekker om karakteren er mellem 10 og 12
        elif (grades[i] > 10) and (grades[i] < 12):
            
            if (abs(grades[i]-(10))) < (abs(grades[i]-(12))):
                
                #afrund til 10
                gradesRounded[i] = grade6[0]
                
            elif (abs(grades[i]-(10))) > (abs(grades[i]-(12))):
                
                #afrund til 12
                gradesRounded[i] = grade6[1]
            
#-----------------------------------------------------------------------------

    return gradesRounded

