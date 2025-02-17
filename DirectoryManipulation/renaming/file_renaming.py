'''
Found on youtube, Corey Schafer
https://www.youtube.com/watch?v=ve2pmm5JqmI
'''
import os
print('working_dir ' + os.getcwd())
#folder_path = r'c:\\Python_Home\\DirectoryManipulation\renaming'
#folder_path = r'c:/Python_Home/DirectoryManipulation/renaming'

os.chdir('c:\\Python_Home\\DirectoryManipulation\\renaming')

#print('new wd ' + os.getcwd())

for f in os.listdir():
    #print(f)

    #splits the text into 2 parts, filename and extension into a tuple
    # print(os.path.splitext(f))
    f_name, f_ext = (os.path.splitext(f))
    # print(file_name.split('-'))

    f_title, f_course, f_num = f_name.split('-')
    #remove whitespace
    f_title = f_title.strip()
    f_course = f_course.strip() 
    #strip hash and add zeros
    f_num = f_num.strip()[1:].zfill(2)
    
    #print(f_title)
    #print('{}-{}-{}{}'.format(f_num,f_course, f_title, f_ext))
    print('{}-{}{}'.format(f_num, f_title, f_ext))
    new_name = ('{}-{}{}'.format(f_num, f_title, f_ext))
    os.rename(f, new_name)