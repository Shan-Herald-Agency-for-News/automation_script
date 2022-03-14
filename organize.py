import os
from pathlib import Path, PurePath, PurePosixPath
from shutil import move

SUBDIR = {
        "DOCUMENTS": [".pdf", ".docx", ".doc", ".txt", ".xls", ".ppt", ".xlsx"],
        "AUDIOS": [".m4a", ".m4b", ".mp3", ".wav"],
        "VIDEOS": [".mp4", ".MOV", ".mov", ".wmv", ".VOB", ".BUP", ".IFO", ".flv", ".aac"],
        "IMAGES": [".jpg", ".jpeg", ".png", ".tif", ".psd", ".ai"],
        "COMPRESS": [".zip", ".rar", ".part"],
        "CODE_SCRIPT": [".py", ".htm", ".html", ".php", ".c", ".cpp", ".js", ".css"],
        "FONTS": [".ttf", ".TTF", ".woff", ".woff2"]
        }

def pickDir(value):
    for category, ext in SUBDIR.items():
        for suffix in ext:
            if suffix == value:
                return category

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

def organizeDir():
    for root, dirs, files in os.walk("./OrganizeTest", topdown=False):
        for name in files:
            filePath = Path(os.path.join(root, name))
            fileType = filePath.suffix.lower()

            directory = pickDir(fileType)

            if directory == None:
                continue

            directoryPath = Path('OrganizedFile/' + directory)

            if directoryPath.is_dir() != True:
                directoryPath.mkdir()
            # filePath.rename(directoryPath.joinPath(filePath))

            # check if file exist
            newPath = os.path.join(directoryPath, name)

            if os.path.exists(newPath):
                add += 1
                check_and_rename(newPath, add)
            else:
                move(filePath, directoryPath)


organizeDir()
