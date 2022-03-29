import os
from pathlib import Path, PurePath, PurePosixPath
from shutil import move

SUBDIR = {
        "DOCUMENTS": [".pdf", ".docx", ".doc", ".txt", ".xls", ".ppt", ".xlsx", ".odt", ".pptx", ".pmd", ".wps"],
        "AUDIOS": [".m4a", ".m4b", ".mp3", ".wav", ".amr"],
        "VIDEOS": [".mp4", ".MOV", ".mov", ".wmv", ".vob", ".bup", ".ifo", ".flv", ".aac", ".3gp"],
        "IMAGES": [".jpg", ".jpeg", ".png", ".tif", ".psd", ".ai", ".gif", ".ico", ".cr2", ".eps", ".bmp"],
        "COMPRESS": [".zip", ".rar", ".part"],
        "CODE_SCRIPT": [".py", ".htm", ".html", ".php", ".c", ".cpp", ".js", ".css", ".sh", ".bat", ".VBS"],
        "FONTS": [".ttf", ".TTF", ".woff", ".woff2"],
        "PROGRAMS": [".exe", ".dll", ".dmg", ".deb", ".tar", ".iso", ".msi"],
        "DATABASES": [".db", ".sql", ".sqlite"]
        }

# get dir name by ext type
def pickDir(value):
    for category, ext in SUBDIR.items():
        for suffix in ext:
            if suffix == value:
                return category

# rename if file exists
def check_and_rename(file, add=0):
    original_file = file
    if add != 0:
        split = file.split(".")
        part_1 = split[0] + "_" + str(add)
        file = ".".join([part_1, split[1]])
    if not os.path.isfile(file):
        os.rename(original_file, file)
    else:
        add += 1
        check_and_rename(original_file, add)


def organize(parentsDir):
    # for each deep file in dir
    for root, dirs, files in os.walk(parentsDir, topdown=False):
        # skip "ORGANIZED" dir
        if "ORGANIZED" in root:
            continue

        for name in files:
            # full file path
            filePath = Path(os.path.join(root, name))
            # get ext
            fileType = filePath.suffix.lower()

            # get dir by ext type
            directory = pickDir(fileType)

            # OTHER for unknow file type
            if directory == None:
                directory = 'OTHER'

            # ORGANIZED Dir in parentsDir
            organize_path = Path(os.path.join(parentsDir, "ORGANIZED"))

            # create new ORGANIZED Dir
            if organize_path.is_dir() != True:
                organize_path.mkdir()

            # new save path
            directoryPath = Path(os.path.join(organize_path, directory))

            # create if not exits
            if directoryPath.is_dir() != True:
                directoryPath.mkdir()

            # new file path
            newPath = os.path.join(directoryPath, name)

            # check if file exists
            if os.path.exists(newPath):
                # rename file if exists
                check_and_rename(newPath)
            else:
                # move if file not exists yet.
                move(filePath, directoryPath)

def organizeFiles(cwd):
    # for each dir with well organize
    for item in os.scandir(cwd):
        parentsDir = Path(item)
        organize(parentsDir)
