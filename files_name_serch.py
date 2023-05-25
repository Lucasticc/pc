import os
import zipfile

path = 'Z:\ppt\开题'
for file_name in os.listdir(path):
    if '简约创意' in file_name:
        file_path = os.path.join(path, file_name)
        print(file_path)
        if zipfile.is_zipfile(file_path):
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(path)
            print(f"{file_path} 解压缩完成")
        else:
            print('不是zip文件')