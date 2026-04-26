# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

# f=open('C:\Mirai Sem2\Python\Lec5\s.txt','r')

# print(f.readline())
import os


f=open('C:\Mirai Sem2\Python\Lec5\s.txt','w')

# print(f.readline())

# f.write('chal chup')

os.remove('C:\Mirai Sem2\Python\Lec5\s.txt')

