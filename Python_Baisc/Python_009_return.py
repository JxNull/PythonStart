# Python009
#Author: Jingxiong Wu

#May/3rd/2018   
#Python exercise project 9

''' Return example'''

traded_point=[0.111,0.135,0.334,0.56544]
new_trade_point=[]

def earning_point(value):
    sale_point=value*1.01
    return sale_point

for x in traded_point:
    a=earning_point(x)
    new_trade_point.append(a)
print(new_trade_point)
