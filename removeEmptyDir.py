import os
from pathlib import Path
import shutil

def removeEmptyDir(parentsDir):
    for item in os.scandir(parentsDir):
        if item.name == "ORGANIZED":
            continue
        shutil.rmtree(Path(item))

def walkInDir():
    for item in os.scandir():
        if item.is_dir():
            removeEmptyDir(item.name)

walkInDir()
