# Python008
#Author: Jingxiong Wu

#May/3rd/2018   
#Python exercise project 8
# Function example
''' Function example'''
CryptoCurrency=['BTC','ETH','NEO','ONT']
Currencylist=['9600','775','85','10']
CClist=dict(zip(CryptoCurrency,Currencylist))

def readlist():
    for x in CClist:
        print(x)
            

def btc_usd(btc):
    m=int(Currencylist[0])
    usd=m*btc
    print('BTC = ', usd, 'USD')



readlist()
btc_usd(0.1)
btc_usd(0.47)
    
