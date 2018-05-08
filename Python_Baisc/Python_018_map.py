# Python018
#Author: Jingxiong Wu

#May/07/2018   
#Python exercise project 18

''' map example'''

a=[1,2,3,4,5]
b=[4,3,2,1]
c=[1,2,3]


def square(x):
    return x**2

print(list(map(square,a)))
print(list(map(lambda x,y: x+y,b,c)))
