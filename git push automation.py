import sys
import os
import datetime
import msvcrt as m

x = datetime.datetime.now()
y=str(x).replace(" ", "")
p="file"
q=".txt"
fileName=p+y+q
print(fileName)

file="file.txt"

f= open(file,"w+")
m.getch()
f.close() 
os.system("git add .")
os.system("git commit -m 'update'")
os.system("git push")

m.getch()
