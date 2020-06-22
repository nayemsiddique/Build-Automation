import sys
import os

f= open("guru99.txt","w+")
f.close() 
os.system("git add .")
os.system("git commit -m 'update'")
os.system("git push")
