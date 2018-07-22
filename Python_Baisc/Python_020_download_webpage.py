# Python020
#Author: Jingxiong Wu

#May/08/2018   
#Python exercise project 20

'''download a web page example'''
import urllib.request

address_url=r'https://www.google.ca'

def download_webpage(url):
    #open the url file
    fileOpen=urllib.request.urlopen(url)
    #read the file
    data= fileOpen.read()
    # convert into string
    data_str = str(data)
    # split the lines into the file
    data_lines= data_str.split('\\n')
    # creates a new file to save data
    fhandle=open("download_wevpage.html","w")   # save web page in local
    # store everything in created file
    for line in  data_lines:
        fhandle.write(line + '\n')
    # close the file to save memory
    fhandle.close()

# run the code
download_webpage(address_url)
