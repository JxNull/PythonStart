# Python021
#Author: Jingxiong Wu

#May/08/2018   
#Python exercise project 21

'''download a image from web page example'''
import urllib.request
import random

def dowload_web_img(url):
    name = random.randomrange(1,500)
    fname=str(name)+".jpg"
    urllib.request.urlretrieve(url,fname)
    
download_web_img(http:www.w3school.com.cn/i/eg_tulip.jpg)
