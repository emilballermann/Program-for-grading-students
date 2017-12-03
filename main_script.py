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
            #load file with panda
            studentGrades = pd.read_csv(file,header=None)
            
            #find the place of the dublicates
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
            
            studentGrades = studentGrades.drop_duplicates(subset = 0)
            
            studentGrades = np.array(studentGrades)
            
            noAss = (len(studentGrades[0,:]) -2)
            noStu = (len(studentGrades[:,0]) -1)
            
            
            print("\nThere are a total of" , noStu , "valid students each with a total of" , noAss , "assignments\n")
            
            
            #Must also check if grades are not on the 7 point scale
            
            
            
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
        print("\n1. Load new data \n2. Check for data errrors\n3. Generate plots\n4. Display list of grades\n5. quit\n")
        
        option = input("Input: ").lower()
        
        
        #Load new data
        if (option == "1"):
            print("bruh")
        
        #show data errors
        if (option == "2"):
            print("bruh")
                
                
        #generate plots    
        elif (option == "3"):
            print("bruh")
                
        
        #display grades    
        elif (option == "4"):
                print(studentGrades)
                
        
        #quit    
        elif (option == "5") or (option =="quit") or (option =="q"):
            break
        
        
        
        else:
            print("\nPlease choose one of the listed options\n")
        
        
        
        
    