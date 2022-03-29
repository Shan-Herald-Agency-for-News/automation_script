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
