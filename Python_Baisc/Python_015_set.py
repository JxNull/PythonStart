# Python015
#Author: Jingxiong Wu

#May/07/2018   
#Python exercise project 15

''' set example'''

cryptoset={'btc','eth','neo','eos','ont','bnb'}
checkset={'neo','dbc'}

print(cryptoset)

for x in checkset:
    if x in cryptoset:
        print(x,"is in this set")
    else:
        print(x,'is not in the set')
