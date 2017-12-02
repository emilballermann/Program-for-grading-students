# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 15:14:11 2017

@author: Garsdal and Emiiiiiil, and Adam Beilin
"""
import pandas as pd
from grade_rounding_function import *
#from gradesPlotFunction import *
from FinalGradeFunction import *

#initial values
fileload = False

print("Welcome to our grading calculator\n")

#start manu
while(True):
    
    #main menu
    print("1. Load new data\n2. Check for data errrors\n3. Generate plots\n4. Display list of grades\n5. quit\n6. shits and giggles")
    option = input("Input: ").lower()
    
    #load function
    if (option == "1" or option == "load new data"):
        
        while(True):
            file = input("Input the name of your .csv file to start the program: ")
            
            if (file == 'quit') or (file == 'q'):
                break   

            else:
                try:
                    studentGrades = pd.read_csv(file,header=None)
                    studentGrades = np.array(studentGrades)
                    
                    fileload = True
                    break
                
                except (FileNotFoundError):
                    print("\nFile not found")
                    pass
                except (ValueError):
                    print("\nFile has to be .csv format")
                    pass
                except (PermissionError):
                    print("\nFile not found")
                    pass
                except (OSError):
                    print("\nFile not found")
                    pass
                
                    
                #for i in range(len(studentGrades[0,:])):
                #    print(np.where(studentGrades.count(studentGrades[i,:])))
        
    
    
    #show data errors
    elif (option == "2"):
        if (fileload == False):
            print("\nYou need to load file first\n")
        else:
            print("bruh")
            
            
    #generate plots    
    elif (option == "3"):
        if (fileload == False):
            print("\nYou need to load file first\n")
        else:
            print("bruh")
            
    
    #display grades    
    elif (option == "4"):
        if (fileload == False):
            print("\nYou need to load file first\n")
        else:
            print(studentGrades)
            
    
    #quit    
    elif (option == "5") or (option =="quit") or (option =="q"):
        break
    
    
    
    else:
        print("\nPlease choose one of the listed options\n")
    
    
    
    
    