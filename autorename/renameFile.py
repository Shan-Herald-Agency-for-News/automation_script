import os

def renameFile():
    dirs = os.getcwd()
    for name in os.listdir(dirs):
        if os.path.isdir(name):
            continue

        old_name = os.path.join(dirs, name)
        new_name = old_name.replace('_1_1_1', '')

        os.rename(old_name, new_name)


renameFile()
