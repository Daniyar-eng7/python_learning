#1
with open("text.txt", "w") as f:
    f.write("hello, world\n")
    f.write("second line\n")
    
#2  
with open("text.txt", "r") as f:
     #print(f.read())
     for line in f:
         print(line)
    
    
#3
with open("text", "a") as f:
    f.write("new line")
    
with open("text.txt", "r") as f:
    print(f.read())


#4
import shutil
shutil.copy("text.txt", "test.txt")      #в ту же папку
shutil.copy("text.txt", "practice_5/test2.txt")    # в другую папку
shutil.copy2("data.txt", "data_backup.txt") 


#5
import os

if os.path.exist("data_backup.txt"):
    os.remove("data_backup.txt")