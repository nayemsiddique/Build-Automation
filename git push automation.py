import sys
import os
import datetime

x = datetime.datetime.now()
#f= open("demoFile"+str(x)+".txt","w+")
#f.close() 
os.system("git add .")
os.system("git commit -m 'update'")
os.system("git push")
