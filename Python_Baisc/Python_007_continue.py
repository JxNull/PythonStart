# Python007
#Author: Jingxiong Wu

#May/3rd/2018   
#Python exercise project 7
# continue function
''' Continue function example'''
token_used=[1,3,5,7,9,11,13,15]

print('Here are tokens are still available')

for x in range(1,20):
    if x in token_used:
        continue
    print(x)

