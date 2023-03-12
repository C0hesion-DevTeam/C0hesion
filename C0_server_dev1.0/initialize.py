import csv 

header_list=['ruid','studentname','teamtype','peoplenum','description','needpeople']
with open('teams_request.csv','w',encoding='utf-8',newline='') as f:
                writer = csv.DictWriter(f, fieldnames=header_list)
                writer.writeheader()
with open('ruid.txt','w',encoding='utf-8',newline='') as f:
                f.write('1');
import shutil
import os

# Specify the paths of the directories to delete and create
dirs_to_delete = ['team', 'stuj', 'stuc']
dirs_to_create = ['team', 'stuj', 'stuc']

# Delete the directories
for d in dirs_to_delete:
    shutil.rmtree(d, ignore_errors=True)

# Create new empty directories with the same names
for d in dirs_to_create:
    os.makedirs(d)
