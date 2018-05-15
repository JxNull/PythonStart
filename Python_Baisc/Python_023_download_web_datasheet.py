# Python023
#Author: Jingxiong Wu

#May/010/2018   
#Python exercise project 23

'''download data sheet from web example'''

from urllib import request

BABA_link='https://query1.finance.yahoo.com/v7/finance/download/BABA?period1=1523774199&period2=1526366199&interval=1d&events=history&crumb=kXQOOj/XU1Z'

def download_datasheet(url):
    response= request.urlopen(url)
    data_read= response.read()
    data_str=str(data_read)
    lines= data_str.split.('\\n')
    data_file= r'stock_data'
    file=open(data_file,'w')
    for line in lines:
        file.write(line+'\n')
    file.close()

download_datasheet(BABA_link)    
