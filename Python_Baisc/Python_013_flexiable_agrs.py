# Python013
#Author: Jingxiong Wu

#May/06/2018   
#Python exercise project 13
''' flexiable number arguement example'''


def add_number(*args):
    total=0
    for a in args:
        total+=a
    print(total)


add_number(1)
add_number(2,5)
add_number(3,6,4,8,5,6,9,21)
