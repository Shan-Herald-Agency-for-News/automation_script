import os
from pathlib import Path
import shutil

def removeEmptyDir(parentsDir):
    for item in os.scandir(parentsDir):
        if item.name == "ORGANIZED":
            continue

        # skip file
        if os.path.isfile(item):
            continue

        shutil.rmtree(Path(item))

def walkInDir(cwd):
    for item in os.scandir(cwd):
        if item.is_dir():
            removeEmptyDir(item.name)
