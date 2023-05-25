import os

path = 'Z:\ppt\简约'

for file_name in os.listdir(path):
    # if '简约创意' in file_name:
        file_path = os.path.join(path, file_name)
        file_ext = os.path.splitext(file_name)[1]  # 获取文件扩展名
        new_name =file_name.replace("[", "").replace("]", "").replace(" ", "").replace("'", "").replace("-优品PPT","")
        new_file_path = os.path.join(path, new_name)
        os.rename(file_path, new_file_path)

print("文件重命名完成")