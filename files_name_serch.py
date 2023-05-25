import os
path = 'Z:\ppt\简约'
for file_name in os.listdir(path):
    if '大气' in file_name:
        print(file_name)