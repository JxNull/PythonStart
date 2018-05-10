# Python020
#Author: Jingxiong Wu

#May/08/2018   
#Python exercise project 20

'''download a web page example'''
import urllib.request
import random

file=urllib.request.urlopen('http://google.com')

data= file.read()               # read all page

dataline=file.readline()        # read a line

fhandle=open("./1/html","wb")   # save web page in local
fhandle.write(data)
fhandle.close()
