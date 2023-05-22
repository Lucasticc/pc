import os
def bulk_download(url_list:list,format:str,save_path:str):
    for ele in url_list:
        if format in ele:
            file_name = os.path.split(ele)[-1]
            full_path = os.path.join(save_path,file_name)
            with open(full_path,"wb") as file:
                response = get(ele)
                file.write(response.content)
            print("download %s done"%ele)
        else:
            print("%s is not a valid link for resource %s"%(ele,format))