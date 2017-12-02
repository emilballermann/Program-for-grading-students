''' Program for grading students
==========================================================

Project start: 23rd of November 2017

Project by Adam Beilin, Marcus Garsdal and Emil Ballermann'''

import math
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
    xAxis = [1,2,3,4,5,6,7]
    
    
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
        plt.bar(xAxis[i],yAxis[i],color=next(prop_iter)['color'], alpha=1) #Plot bar plot with colors
        
    
    plt.xticks(xAxis,bacStr, rotation = 35) #Set lables and rotation xAxis,bacStr,rotation=35
    plt.title("Final grades") #Set title
    plt.xlabel("Grades") #Assign name to x-axis
    plt.ylabel("Number of students") #Assign name to y-axis
    
  
    
    #Making the y-axis only integers
    locs, labels = plt.yticks()
    for each in locs:
        yAxis.append(int(each))
    plt.yticks(yAxis)

    plt.show()
    
"====================================="

     #Plot "Grades per assignment"

#Defining length of datamatrix
x = np.array(range(len(grades)))

xLabels=[""]*len(grades)

for i in range(len(grades)):
    xLabels[i]="Assignment no. "+" "+str(i+1)
print(xLabels)

y = [-3,00,2,4,7,10,12]
yLabels = [-3,00,2,4,7,10,12]

plt.plot(x,y)


plt.xticks(x, xLabel, rotation = 35)
plt.yticks(y,)
plt.show()


print(gradesPlot(grades))
    
'''“Grades per assignment”: A plot with the assignments on the x-axis and the grades on the y-axis. The x-axis must
 show all assignments from 1 to M, and the y-axis must show all grade −3 to 12. The plot must contain: 
     1. Each of the given grades marked by a dot. You must add a small random number (between -0.1 and 0.1) to the x- and
 y-coordinates of each dot, to be able tell apart the diﬀerent dots which otherwise would be on top of each other 
 when more than one student has received the same grade in the same assignment. 
     2. The average grade of each of 
 the assignments plotted as a line
The plots should include a suitable title, descriptive axis labels, and a data legend where appropriate. You are
 allowed to present the plots in separate ﬁgure windows or as sub-plots in a single ﬁgure window.'''
