import os

#This Dir-listing prints all files and folders in alphabetic order in Terminal
folder_path = r'C:\Users\ekrrmai\OneDrive - Ericsson\Ericsson\Python_Home'

extension = 'txt'
file_dictionary ={}

txt_files = [i for i in os.listdir(folder_path)]  #if i.endswith(extension)]

# print files

for i in txt_files:
    key_number = (txt_files.index(i)+1)
    file_dictionary[key_number] = i

print(file_dictionary)
