#1    вложенный папки
import os
os.makedirs("project/data/backup")

#os.mkdir("project")


#2 список всех 
items=os.listdir("project")
print(items)

#список сортированный файл оот папки
for item in os.listdir('project'):
    full_path=os.path.join('project',item)
    if os.path.isdir(full_path):
        print(f"папка: {item}")
    else:
        print(f"file:{item}")
        
        
        
#3 find files by extenctions
import os

for root, dirs, files in os.walk('project'):     # заходим в каждую папку по очереди
    for file in files:
        if file.endswith('.py'):                  #проверяем заканчивается на .py?
            print(os.path.join(root, file))
            
            
            
# 4 Копирование файла 
import shutil
shutil.copy('project/main.py', 'backup/main.py')


#Копирование папки 
shutil.copytree('project/src', 'backup/src')


#Перемещение
shutil.move('project/data.txt', 'backup/data.txt')


#Переименование
os.rename('project/main.py', 'project/app.py')