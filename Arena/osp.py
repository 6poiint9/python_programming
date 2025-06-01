#from os import system  
import os
print(os.name)

# print env variables 
output = os.environ['SHELL']
print(output)

# returns UID 
print(os.getuid()) 

# returns PID 
os.getpid()

# returns a List containing the directory listing 
print(os.listdir())

#print(os.uname())

# run shell commands 
#system("cat ok.py | less")

# get output of current dir 
print(os.getcwd())

# change dir
os.chdir("course_registration/")

print("After:", os.getcwd())

# create new directory 
os.mkdir('test')

os.listdir()
['test'] 

# rename file or dir 
os.rename('test','new_one')



