''' Program for grading students
==========================================================

Project start: 23rd of November 2017

Project by Adam Beilin, Marcus Garsdal and Emil Ballermann'''

import matplotlib.pyplot as plt 
import numpy as np
from FinalGradeFunction import *
a=[4,7,12,10,10,00,2]
b=[12,10,7,4,4,2,2,]
c=[00,-3,00,-3,-3,4,4]
d=[4,7,7,10,00,2,2]
grades = np.vstack([a,b,c,d])
data=np.copy(grades)

#Defines plot function
def gradesPlot(grades):
    '''
=============Plot "Final grades"===============
    '''        
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
                        hspace=0.2,wspace=0.2) #Adjusting size
    #Plotting bar plot
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
    
    '''
===============Plot "Grades per assignment"==================
     '''
               
    #Save the number of students and assignments as variables
    N = grades.shape[0]
    M = grades.shape[1]
    y = [-3,00,2,4,7,10,12]
    #Making a matrix with random numbers for dot-position
    x=np.random.uniform(-0.1,0.1,M*N).reshape(N,M)
    newdata = data + x
    #Make dots for each assignment
    for i in range(M):
        plt.plot(np.random.uniform(-0.1,0.1,N)+i+1, newdata[:,i] ,color='blue',marker='o',linestyle='None', markersize=5)
    #Plot the mean grade for each assignment as a line  
    mean=np.ones(M)
    for i in range(M):
        mean[i]=np.mean(newdata[:,i])
    plt.plot(np.arange(M)+1, mean ,color='red',linestyle='-',label="Mean grade")

    plt.title("Grades per assignment") # Set the title of the graph
    plt.yticks(y, rotation = 35)
    plt.xlabel("Assignment number") # Set the x-axis label 
    plt.ylabel("Grade") # Set the y-axis label 
    plt.grid(True) #Attach grid to plot
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.show()
    
    #define empty variable (y) to return from function
    y=" "
    return y
    

print(gradesPlot(grades))

