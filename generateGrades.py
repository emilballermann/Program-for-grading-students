# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 12:59:53 2017

@author: Garsdal
"""

#-----------------------------------------------------------------------------

from grade_rounding_function import *
import numpy as np
from random import randint

#-----------------------------------------------------------------------------
#Here you can input the number of students and assignments you want to test for
#You can chose to use random numbers where you pick the lower and higher boundaries

#random rows (number of students)
#x = randint(1, 10)
x = 8

#random colums (number of assignments)
#y = randint(1, 5)
y = 5

#-----------------------------------------------------------------------------

#random student names
student_names = np.array(["Ben","Mikkel","Thomas","Mads","Jesper","Emil","Adam","Marcus"])

#we create a matrix with random grades
A = np.random.uniform(low=-3, high=12, size=(x,y))

#we round our random integers to grades using our grade_rounding_function
for i in range(np.size(A,axis=0)):
    A[i,:] = roundGrade(A[i,:])
    
#we create a vector with the number of assignments
assignments=[""]*y

for i in range (y):
    assignments[i]="Assignment"+" "+str(i+1)

#Labels for the data in our matrix
labels = ["Student ID"]+["Name"]+assignments

#-----------------------------------------------------------------------------

#empty string array to fill with students
string_array = [""]*x

for i in range (x):
    string_array[i]=student_names[randint(0, len(student_names)-1)]

#we transpose our names to have same dimension as our grades
students = np.array([string_array]).T

#-----------------------------------------------------------------------------

#empty string array to fill with student numbers
string_array2 = [""]*x

#random student numbers
for i in range (x):
    string_array2[i] = "s"+str(randint(12300, 12999))

#we transpose our student numbers to have same dimension as our grades
student_numbers = np.array([string_array2]).T

#-----------------------------------------------------------------------------

#we add our student names to the left side of our grades
A_new = np.hstack((students, A))

#we add our student numbers to the left side of our student names / grades
studentGrades = np.hstack((student_numbers, A_new))

#we add our labels (Name, student ID, assignment)
studentGrades = np.vstack((labels, studentGrades))
#-----------------------------------------------------------------------------

#save the studentGrades as a .csv file

#print(np.mean(A))
np.savetxt("studentGrades½.csv", studentGrades, fmt='%s', delimiter=",")
