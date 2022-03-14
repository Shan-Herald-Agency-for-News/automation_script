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

def organizeDir():
    for item in os.scandir():
        if item.is_dir():
            continue
        
        filePath = Path(item)
        fileType = filePath.suffix.lower()
        directory = pickDir(fileType)

        if directory == None:
            continue

        directoryPath = Path(directory)

        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))
    
organizeDir()
