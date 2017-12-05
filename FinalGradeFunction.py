# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 13:00:40 2017

@author: Adam
"""

#----------------------------------------------------------------------------

import numpy as np
from gradeRoundingFunction import *

#----------------------------------------------------------------------------

#start of function
def computeFinalGrades(grades):
    
#----------------------------------------------------------------------------
    
    #if each student only has one grade it is the final
    if (len(grades[0,:]) == 1):
        gradesFinal = roundGrade(grades)
    
#----------------------------------------------------------------------------
    
    #find final grade if more than one grade
    else:
        #remove smallest grade
        grades.sort(axis=1)
        grades = grades[:,1:len(grades[0,:])]
        
#----------------------------------------------------------------------------

        #assign the mean grades to a new array
        gradesMean = np.zeros(len(grades[:,0]))
        
        for i in range(len(gradesMean)):
            gradesMean[i] = (np.mean(grades[i,:]))
      
#----------------------------------------------------------------------------
        
        #apply rounding grade function to only have valid grades
        gradesFinal = roundGrade(gradesMean)
    
    return gradesFinal

#print(computeFinalGrades(grades))