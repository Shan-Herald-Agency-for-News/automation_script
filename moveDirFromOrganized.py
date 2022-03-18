import os
from pathlib import Path
import shutil

def moveFrom_Organized(parentDir):
    rootDir = os.path.join(parentDir, 'ORGANIZED')
    for item in os.listdir(rootDir):
        shutil.move(os.path.join(rootDir, item), os.path.join(parentDir, item))
    os.rmdir(rootDir)

def walkInDir():
    for item in os.scandir():
        if os.path.isfile(item):
            continue
        moveFrom_Organized(item.name)

walkInDir()
