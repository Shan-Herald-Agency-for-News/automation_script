import os
import datetime
from pathlib import Path

import json
from bson import json_util
from collections import OrderedDict

def listfiles(parentsDir):
    global id, dict_list
    for root, dirs, files in os.walk(parentsDir, topdown=True):
        for file in files:
            rootPath = os.path.dirname(root)
            rootPathName = os.path.basename(rootPath)

            fileName, fileType = os.path.splitext(file)
            fileType_name = fileType.split(".")[-1]
            filePath = os.path.join(root, file)

            c_time = os.path.getctime(filePath)
            m_time = os.path.getmtime(filePath)

            dt_c = datetime.datetime.fromtimestamp(c_time)
            dt_m = datetime.datetime.fromtimestamp(m_time)

            dlist = OrderedDict()
            dlist["id"] = id
            dlist["name"] = rootPathName + " - " + fileName
            dlist["type"] = fileType_name.lower()
            dlist["path"] = filePath
            dlist["create_time"] = dt_c
            dlist["modifiled_time"] = dt_m
            dict_list.append(dlist)

            id = id+1
    
    j = json.dumps(dict_list, default=json_util.default, ensure_ascii=False)

    with open("filelist_db.json", "w", encoding="utf8") as f:
        f.write(j)

id = 0
dict_list = []

def main():
    cwd = os.getcwd()
    for item in os.scandir(cwd):
        parentsDir = Path(item)
        if not os.path.isfile(parentsDir):
            listfiles(parentsDir)

if __name__ == '__main__':
    main()