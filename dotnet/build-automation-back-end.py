import sys
import os
import msvcrt as m
os.system("pip install tqdm")
from tqdm import tqdm

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
            try:
                shutil.copytree("test",Clone_Path)
            except:
                 print("\033[1;31;40m"+Clone_Path+"\n This Directory does not exist.\033[1;32;40m \nPress Any Key To Exit\033[0;37;40m.")
                 shutil.rmtree("test")
                 m.getch()
                 return
            #return
            

    #download from git

    

    if os.path.isdir(newPath):
        os.chdir(newPath)
        try:
            print("\033[1;33;40m Pulling...\033[0;37;40m.")
            #repo = git.Repo(newPath)
            for i in tqdm(range(1)):
                #repo.remotes.origin.pull()
                os.system("git pull")
            print("\033[1;33;40m Done..\033[0;37;40m.")
        except:
            print("\033[1;31;40m Git pull not working.please check configuration and connection.\033[1;32;40m \nPress Any Key To Exit\033[0;37;40m.")
            m.getch()
            return
       
    else:
        os.chdir(Clone_Path)
        try:
            print("\033[1;33;40m Cloning......\033[0;37;40m..")
            for i in tqdm(range(1)):
                git.Git(Clone_Path).clone(GitHub_Link)
            print("\033[1;33;40m Done.\033[0;37;40m.")
            os.chdir(newPath)
        except:
            print("\033[1;31;40m Git Clone not working.please check configuration and connection.\033[1;32;40m \nPress Any Key To Exit\033[0;37;40m.")
            m.getch()
            return
    #os.chdir(newPath)


    #Restore
    os.system("dotnet restore")
    try:
        os.system("nuget restore")
    except:
        print("\033[1;31;40m Restore Faild.please check nuget configuration.\033[1;32;40m \nPress Any Key To Exit\033[0;37;40m.")
        m.getch()
        return
    try:
        os.system("dotnet publish -c Release")
    except:
        print("\033[1;31;40m Publish Faild.Try Again\033[1;32;40m \nPress Any Key To Exit\033[0;37;40m.")
        m.getch()
        return
          
    
    if os.path.isdir(Destination_Path):
        if os.path.isdir(Backup_Path):
            print("\033[1;31;40m Backup Directory Path is Already exist. Please Change the Directory Name/Path..And Try Again!!! \033[1;32;40m \nPress Any Key To Exit\033[0;37;40m.")
            m.getch()
            return
        if  not len(os.listdir(Destination_Path))==0:
            try:
                shutil.copytree(Destination_Path,Backup_Path)
            except:
                print("\033[1;31;40m Backup Process Faild.please Try Again.\033[1;32;40m \nPress Any Key To Exit\033[0;37;40m.")
                m.getch()
                return
        try:
            shutil.rmtree(Destination_Path)
        except:
             print("\033[1;31;40m Can not Delete Previous Publish Files.please Try Again.\033[1;32;40m \nPress Any Key To Exit\033[0;37;40m.")
             m.getch()
             return
    try:        
        shutil.copytree(Published_File_Path,Destination_Path)
    except:
        print("\033[1;31;40m Can not Copy The Publish Files,Please Check Directory Path And Try Again.\033[1;32;40m \nPress Any Key To Exit\033[0;37;40m.")
        m.getch()
        return
    
    os.chdir(Destination_Path)
    with open('index.html', 'w'):
        pass
    
    print("\033[1;32;40m publish completed. \nPress Any Key To Exit\033[0;37;40m.")
    m.getch()


#file Read Start
try:
    data = pd.read_excel ('input.xlsx',sheet_name='dotnet')
    GitHub_Link = data['Github_Link'].tolist()[0]
    print(GitHub_Link)
    Clone_Path = data['Clone_Path'].tolist()[0]
    Published_File_Path = data['Published_File_Path'].tolist()[0]
    Destination_Path = data['Destination_Path'].tolist()[0]
    Backup_Path = data['Backup_Path'].tolist()[0]
    dotnet()
except:
    print("\033[1;31;40m File does not exist.\033[1;32;40m \nPress Any Key To Exit\033[0;37;40m.")
    m.getch()



#File Read End







    

