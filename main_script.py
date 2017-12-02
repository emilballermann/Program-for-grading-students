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

    file = input("Input the name of your .csv file to start the program: ")
    
    if (file == 'quit') or (file == 'q'):
        break   
    else:
        try:
            studentGrades = pd.read_csv(file,header=None)
            
            
            findDubs = studentGrades.duplicated(subset=0)
            findDubs = np.array(findDubs)
            
            index = np.where(findDubs==True)
            index = index[0]
            
            noDubs = len(index)
            
            dubs = [""]*len(index)
            rows = [""]*len(index)
            
            #convert place holder so we can still operate on studentGrades with panda
            temp = np.array(studentGrades)
            
            for i in range (noDubs):
                dubs[i] = temp[index[i],0]
                rows[i] = index[i]
            
            if len(dubs) >0:
                print("\nThere were",noDubs,"duplicates found in the student IDs, they were:")
                for i in range(noDubs):
                    print(dubs[i],"from row",rows[i])
                    
                    
            #removes duplicates in studentnumber, but does not say where!!
            
            studentGrades = studentGrades.drop_duplicates(subset = 0)
            
            studentGrades = np.array(studentGrades)
            
            noAss = (len(studentGrades[0,:]) -2)
            noStu = (len(studentGrades[:,0]) -1)
            
            
            print("\nThere are a total of" , noStu , "valid students each with a total of" , noAss , "assignments\n")
            
            
            
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
      

if (fileload == True):

    
    while(True):
        #main menu
        print("\n1. Check for data errrors\n2. Generate plots\n3. Display list of grades\n4. quit\n")
        
        option = input("Input: ").lower()
        
        
        #show data errors
        if (option == "1"):
            print("bruh")
                
                
        #generate plots    
        elif (option == "2"):
            print("bruh")
                
        
        #display grades    
        elif (option == "3"):
                print(studentGrades)
                
        
        #quit    
        elif (option == "4") or (option =="quit") or (option =="q"):
            break
        
        
        
        else:
            print("\nPlease choose one of the listed options\n")
        
        
        
        
    