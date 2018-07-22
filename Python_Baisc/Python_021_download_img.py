# Python021
#Author: Jingxiong Wu

#May/08/2018   
#Python exercise project 21

'''download a image from web page example'''
import random
import urllib.request

def download_web_img(url):
    name= random.randrange(1,500)
    file_name= str(name)+'.jpg'
    urllib.request.urlretrieve(url,file_name)

    
download_web_img('https://media-cdn.tripadvisor.com/media/photo-s/00/1b/51/d4/phot-of-cottages-from.jpg')
