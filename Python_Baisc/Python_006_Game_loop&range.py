# Python006
#Author: Jingxiong Wu

#May/2nd/2018   
#Python exercise project 6
# game combines for loop, range
''' Print out all number in range of 105 can divded by 3
if find out magic number then game exit
'''
magicnumber=100
for x in range(0,105):
    if x%3 is 0:
        print(x,"Can divied by 3")
    elif x is magicnumber:
        print(x,'is magic number')
        break
    else:
        print(x,"cann't divied by 3")
