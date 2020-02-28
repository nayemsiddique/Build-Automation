import sys
import os


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
    print(newPath)

    if os.path.isdir(Clone_Path):
         x="1"
    else:
         os.mkdir(Clone_Path)

    #download from git

    

    if os.path.isdir(newPath):
        print("Pulling....")
        repo = git.Repo(newPath)
        repo.remotes.origin.pull()
        print("Done...")
       
    else:
        print("Cloning........")
        git.Git(Clone_Path).clone(GitHub_Link)
        print("Done..")




    os.chdir(newPath)


    #Restore
    os.system("dotnet restore")
    os.system("nuget restore")

    os.system("dotnet publish")
    
      
    
    if os.path.isdir(Destination_Path):
        shutil.copytree(Destination_Path,Backup_Path)
        shutil.rmtree(Destination_Path)


    shutil.copytree(Published_File_Path,Destination_Path)
        




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


    

