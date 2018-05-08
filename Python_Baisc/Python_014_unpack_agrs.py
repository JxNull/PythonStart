# Python014
#Author: Jingxiong Wu

#May/06/2018   
#Python exercise project 14
''' unpacking args example'''


def rate_calculator(last_price,price,last_volume,volume):
    rate=100*((price-last_price)*0.25+(last_volume-volume)*0.0075)
    print(rate)


data=[110,112,4300,4350]
rate_calculator(data[0],data[1],data[2],data[3])
rate_calculator(*data)
