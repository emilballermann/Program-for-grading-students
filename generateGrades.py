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

#random rows (number of students)
x = randint(1, 10)
#random colums (number of grades)
y = randint(1, 5)

#random student names
student_names = np.array(["Ben","Mikkel","Thomas","Mads","Jesper","Emil","Adam","Marcus"])

#we create a matrix with random grades
A = np.random.uniform(low=-3, high=12, size=(x,y))

#we round our random integers to grades using our grade_rounding_function
for i in range(np.size(A,axis=0)):
    A[i,:] = roundGrade(A[i,:])

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

#-----------------------------------------------------------------------------

#save the studentGrades as a .csv file
np.savetxt("studentGrades.csv", studentGrades, fmt='%s', delimiter=",")
