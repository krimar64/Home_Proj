import os
folder_path = r'C:\Users\ekrrmai\OneDrive - Ericsson\Ericsson\Python_Home'

#This dirlist prints all files and folders in terminal
def listdir(dir):
    fileNames = os.listdir(dir)
    for fileName in fileNames:
        print('FileName: ' + fileName)
        print('Folder path: ' + os.path.abspath(os.path.join(dir,fileName)), sep = '\n')

if __name__ == '__main__':
    listdir(folder_path)