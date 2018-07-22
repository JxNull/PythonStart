# Python023
#Author: Jingxiong Wu

#May/010/2018   
#Python exercise project 23

'''download data sheet from web example'''

import urllib.request


def download_datasheet(url):
    fileOpen= urllib.request.urlopen(url)
    data= fileOpen.read()
    data_str=str(data)
    data_lines= data_str.split('\\n')
    data_file= r'stock_data.txt'
    file=open(data_file ,'w')
    for line in data_lines:
        file.write(line+'\n')
    file.close()


data_link = r'https://coinmarketcap.com/currencies/neo/historical-data/?start=20130428&end=20180722'

download_datasheet(data_link)

