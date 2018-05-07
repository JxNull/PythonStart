# Python011
#Author: Jingxiong Wu

#May/05/2018   
#Python exercise project 11
''' variable example'''

a="I am global variable"

def print_v_a():
  print(a)

def print_v_b(x):
  print(x)

print_v_a()       # result in  "I am global variable"
print_v_b(a)      # result in "I am global variable"

'''if variable write in the function ifself, then it becames a local variable'''

def print_v_c():
  a="I am a local variable"
  print(a)

def print_v_d(x):
  print(x)
 
print_v_c()      # result in "I am local variable"
print_v_d(a)      # result in "I am global variable"
