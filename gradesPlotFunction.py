''' Program for grading students
==========================================================

Project start: 23rd of November 2017

Project by Adam Beilin, Marcus Garsdal and Emil Ballermann'''

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

grades = np.random.random((10,10))
grades = np.round(grades*10)

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
    x,y = np.count 
    
    
        #Plot "Number of bacteria"
    x,y = np.unique(data[:,2],return_counts=True) #get x and y values
    x = x.astype(int) #Convert to integers
    bacStr = np.array(["Salmonella enterica","Bacillus cereus","Listeria",
             "Brochothrix thermosphacta"]) #x-labes
    prop_iter = iter(plt.rcParams['axes.prop_cycle']) #Iterate through colors

    plt.figure(1,figsize=(6,6)) #Set first figure with 1:1 ratio
    plt.subplots_adjust(top=0.88, bottom=0.225, left=0.11, right=0.9,
                        hspace=0.2,wspace=0.2) #Adjust size
    for i in range(0,len(x)):
        plt.bar(x[i],y[i],color=next(prop_iter)['color']) #Plot bar plot with colors