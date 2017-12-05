# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 15:14:11 2017

@author: Garsdal and Emiiiiiil, and Adam Beilin
"""

#initial imports
#----------------------------------------------------------------------------

import pandas as pd
from gradeRoundingFunction import *
from gradesPlotFunction import *
from finalGradeFunction import *

#initial values
#----------------------------------------------------------------------------

fileload = False

#Introduction to the program
#----------------------------------------------------------------------------

print("\nWelcome to our grading calculator")

#Loading a .csv file
#----------------------------------------------------------------------------

while(True):

    file = input("Input the name of your .csv file to start the program: ")
    
    if (file == 'quit') or (file == 'q'):
        break   
    else:
        try:
            #load file with panda
            studentGrades = pd.read_csv(file,header=None)
            
            #find the place of the dublicates

#Error handling for duplicates
#----------------------------------------------------------------------------            
            
            findDubs = studentGrades.duplicated(subset=0)
            findDubs = np.array(findDubs)
            
            index = np.where(findDubs==True)
            index = index[0]
            
            #find amount of dublicates
            noDubs = len(index)
            dubs = [""]*len(index)

            #convert place holder so we can still operate on studentGrades with panda
            temp = np.array(studentGrades)
            
            #find the specific duplicates
            dubs = [""]*len(index)
            
            for i in range (noDubs):
                dubs[i] = temp[index[i],0]
                
            #print message of which IDs were duplicates
            if len(dubs) >0:
                print("\nThere were",noDubs,"duplicates found in the student IDs, they were:")
                for i in range(noDubs):
                    print(dubs[i],"from row",index[i])
                    
                    
            #removes duplicates in studentnumber
                    #print(dubs[i],"from row",index[i])

#datafile (grades) needed to work with is defined                    
#----------------------------------------------------------------------------
      
            #removes duplicates in studentnumber, but does not say where!!
            
            studentGrades = studentGrades.drop_duplicates(subset = 0)
            
            studentGrades = np.array(studentGrades)
            
            #kode til at fjerne navne/student ID/assignments
            grades = np.delete((np.delete((np.delete(studentGrades,0,axis=0)),0,axis = 1)),0,axis=1)
            grades = grades.astype(float)
            
            
            noAss = (len(studentGrades[0,:]) -2)
            noStu = (len(studentGrades[:,0]) -1) 
            
            #Must also check if grades are not on the 7 point scale
            
            
            print("\nThere are a total of" , noStu , "valid students each with a total of" , noAss , "assignments")
     
#some error handling
#----------------------------------------------------------------------------
            
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

#Continue to main script if file is loaded
#----------------------------------------------------------------------------

if (fileload == True):

#----------------------------------------------------------------------------
    
    while(True):
        #main menu
        print("\n1. Load new data \n2. Check for data errrors\n3. Generate plots\n4. Display list of grades\n5. quit\n")
        
        option = input("Input: ").lower()
        
        
        #Load new data
        print("\n1. Check for data errors\n2. Generate plots\n3. Display list of grades\n4. Quit")
        
        option = input("Input: ").lower()
        
#----------------------------------------------------------------------------

        #show data errors
        if (option == "1"):
            print("bruh")
        
        #show data errors
        if (option == "2"):
            print("bruh")
                
#----------------------------------------------------------------------------

        #generate plots    
        elif (option == "3"):
            print("bruh")
        elif (option == "2"):
            gradesPlot(grades)
                
#----------------------------------------------------------------------------
  
        #display grades    
        elif (option == "4"):
                print(studentGrades)
                
#----------------------------------------------------------------------------
     
        #quit    
        elif (option == "5") or (option =="quit") or (option =="q"):
            break
        
#----------------------------------------------------------------------------
        
        else:
            print("\nPlease choose one of the listed options")
        
        
        
        
    