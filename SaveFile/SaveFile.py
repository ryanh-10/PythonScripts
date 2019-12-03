import os.path
import pathlib
from os import path


def saveToFile(filePath, textToSave):
    # Check if current file path exists
    file = pathlib.Path(filePath)
    if file.exists():
        print("File exists")
    else:
        print("File doesn't exist. Creating file")

    # Open the file and overwrite the current text
    file = open(filePath, "w")
    file.writelines(textToSave)
    file.close()

    # Check that current text in file is same as expected data
    if textToSave == open(filePath).read():
        print("File and text are the same")
        return True
    else:
        print("File and text are different")
        return False

def readFile(filePath):
    # Check if current file path exists
    file = pathlib.Path(filePath)
    if file.exists():
        print("File exist")
        file = open(filePath, "r")
        print(file.read())
        file.close()
    else:
        print("File doesn't exist")
        print("")

#Location of file
saveToFile("C:\\Users\\ryanh\\OneDrive\\Documents\\test2.txt", "asdfqewd")
#readFile("C:\\Users\\ryanh\\OneDrive\\Documents\\testwe2.txt")
