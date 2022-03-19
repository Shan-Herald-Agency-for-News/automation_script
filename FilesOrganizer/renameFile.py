import os
import shutil

from pathlib import Path

def renameFile(parentsDir):
    for root, dirs, files in os.walk(parentsDir, topdown=False):
        for name in files:
            old_name = os.path.join(root, name)
            new_name = old_name.replace('_1_1_1_1_1', '')
            os.rename(old_name, new_name)

def walkInDir():
    for item in os.scandir():
        parentsDir = Path(item)
        renameFile(parentsDir)

walkInDir()
