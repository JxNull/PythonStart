# Python000
#Author: Jingxiong Wu

#April/11/2018   
#Python exercise project 0

# String exercise
print("Hello World")

# Multiple repeat strings
print("Hello"*3)

# single & double quote
print("I don't know.")
print('He said:"I don\'t know"')  # backslash makes whatever behind as part of string
print('He said:\n"I don\'t know"') # \n use case
print('c:\user\desktop\nothing') # backslash mass up case
print(r'c:\user\desktop\nothing') # r before string, backslash no special meaning, file path,etc.

#String can be variable
name= 'JxNull '
print(name)
print(name+'Wu\n')
print((name+'Wu\n')*3)

# Slicing strings
print(name[0])    # J
print(name[1])    # x
print(name[3])    # u
print(naem[5])    # l
print(name[-1])   # l
print(name[-3])   # u
print(name[:4])   # JxNu
print(name[2:5])  # xNull
print(name[:2])   # JxN
print(name[:])    # JxNull

# length of string 
len(name)   # returns 6
