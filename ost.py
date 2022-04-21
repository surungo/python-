import os

newDir='newDir'
curDir = os.getcwd()
print(curDir)
#if os.path.exists(newDir):
# os.rmdir(newDir)
if True!=os.path.exists(newDir):
 os.mkdir(newDir)
dir_list = os.listdir(curDir)
print(dir_list)

os.chdir(newDir)
curDir = os.getcwd()
print(curDir)

if True!=os.path.exists(newDir):
 os.mkdir(newDir)
dir_list = os.listdir(curDir)
print(dir_list)


if os.path.exists(newDir):
 os.rmdir(newDir)



print('hi')