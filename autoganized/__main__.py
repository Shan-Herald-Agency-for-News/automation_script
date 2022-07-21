import os

import organizedByDir
import removeEmptyDir
import moveDirFromOrganized

def main():
	# current working directory
	cwd = os.getcwd()

	# 1. organize files by files extension
	organizedByDir.organizeFiles(cwd)

	# 2. remove leaved empty dir
	removeEmptyDir.walkInDir(cwd)

	# 3. move organized files and directory from ORGANIZED
	moveDirFromOrganized.walkInDir(cwd)

if __name__ == "__main__":
	main()
