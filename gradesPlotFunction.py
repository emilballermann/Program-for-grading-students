''' Program for grading students
==========================================================

Project start: 23rd of November 2017

Project by Adam Beilin, Marcus Garsdal and Emil Ballermann'''

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from FinalGradeFunction import *

#Defines plot function
def gradesPlot(grades):
    '''
    INPUT:
        data: An N x M matrix

    OUTPUT:
        A bar plot of the number of students who have recieved each of possible 
        final grades on the 7-step-scale (computed using the function 
        computeFinalGrades)

    USAGE:
        gradesPlot(grades)
    '''
    
        #Plot "Final grades"
    xAxis = [-3,00,2,4,7,10,12]
    
    #Making to computeFinalGrades(grades) a list to count frequency
    finalGradesToList = list(computeFinalGrades(grades))
    yAxis = [finalGradesToList.count(-3),
             finalGradesToList.count(00),
             finalGradesToList.count(2),
             finalGradesToList.count(4),
             finalGradesToList.count(7),
             finalGradesToList.count(10),
             finalGradesToList.count(12)]
    
    
    bacStr = np.array(["-3","00","02","4","7","10","12"]) #x-lables
    prop_iter = iter(plt.rcParams['axes.prop_cycle']) #Iterate through colors

    plt.figure(1,figsize=(6,6)) #Set first figure with 1:1 ratio
    plt.subplots_adjust(top=0.88, bottom=0.225, left=0.11, right=0.9,
                        hspace=0.2,wspace=0.2) #Adjust size

    for i in range(0,len(xAxis)):
        plt.bar(xAxis[i],yAxis[i],color=next(prop_iter)['color']) #Plot bar plot with colors

    plt.xticks(xAxis,bacStr,rotation=35) #Set lables and rotation
    plt.title("Final grades") #Set title
    plt.xlabel("Grades") #Assign name to x-axis
    plt.ylabel("Number of students") #Assign name to y-axis
    
print(gradesPlot(grades))
    
