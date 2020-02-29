import sys
import os
import msvcrt as m

os.system("pip install gitpython")

os.system("pip install pandas") 
os.system("pip install xlrd")

import pandas as pd

import git
import shutil 




def dotnet():
    flag= False
    
    #extract dir
    print(GitHub_Link)
    tem=GitHub_Link.split(".")
    print(tem)
    tem=tem[1].split("/")
    tem=tem[len(tem)-1] #petmatrix-backend-kku
    #end

    newPath=Clone_Path+"\\"+tem+"\\"
    #print(newPath)

    if os.path.isdir(Clone_Path):
         x="1"
    else:
        try:
            os.mkdir(Clone_Path)
        except:
            #print("\033[1;31;40m Clone Path Doesnot Exist")
            os.mkdir("test")
            shutil.copytree("test",Clone_Path)
            shutil.rmtree("test")
            m.getch()
            #return
            

    #download from git

    

    if os.path.isdir(newPath):
        try:
            print("\033[1;32;40m Pulling....")
            repo = git.Repo(newPath)
            repo.remotes.origin.pull()
            print("\033[1;32;40m Done...")
        except:
            print("\033[1;31;40m Git pull not working.please check configuration and connection.\033[1;32;40m \nPress Any Key To Exit")
            m.getch()
            return
       
    else:
        try:
            print("\033[1;32;40m Cloning........")
            git.Git(Clone_Path).clone(GitHub_Link)
            print("\033[1;32;40m Done..")
        except:
            print("\033[1;31;40m Git Clone not working.please check configuration and connection.\033[1;32;40m \nPress Any Key To Exit")
            m.getch()
            return
    os.chdir(newPath)


    #Restore
    os.system("dotnet restore")
    try:
        os.system("nuget restore")
    except:
        print("\033[1;31;40m Restore Faild.please check nuget configuration.\033[1;32;40m \nPress Any Key To Exit")
        m.getch()
        return

    os.system("dotnet publish")
    
      
    
    if os.path.isdir(Destination_Path):
        if os.path.isdir(Backup_Path):
            print("\033[1;31;40m Backup Directory Path is Already exist. Please Change the Directory Name/Path..And Try Again!!! \033[1;32;40m \nPress Any Key To Exit")
            m.getch()
            return
        try:
            shutil.copytree(Destination_Path,Backup_Path)
        except:
            print("\033[1;31;40m Backup Process Faild.please Try Again.\033[1;32;40m \nPress Any Key To Exit")
            m.getch()
            return
        try:
            shutil.rmtree(Destination_Path)
        except:
             print("\033[1;31;40m Can not Delete Previous Publish Files.please Try Again.\033[1;32;40m \nPress Any Key To Exit")
             m.getch()
             return
    try:        
        shutil.copytree(Published_File_Path,Destination_Path)
    except:
        print("\033[1;31;40m Can not Copy Publish Files.please Try Again.\033[1;32;40m \nPress Any Key To Exit")
        m.getch()
        return
        
    print("\033[1;32;40m Done.. \nPress Any Key To Exit")
    m.getch()




#file Read Start
data = pd.read_excel ('input.xlsx',sheet_name='dotnet')

GitHub_Link = data['Github_Link'].tolist()[0]
print(GitHub_Link)
Clone_Path = data['Clone_Path'].tolist()[0]
Published_File_Path = data['Published_File_Path'].tolist()[0]
Destination_Path = data['Destination_Path'].tolist()[0]
Backup_Path = data['Backup_Path'].tolist()[0]


#File Read End




dotnet()


    

