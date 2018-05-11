# Python022
#Author: Jingxiong Wu

#May/09/2018   
#Python exercise project 22

'''read and write file example'''
file_a= open("sample.txt","w")      #creat a file and write sth in it
file_a.write("This is a sample file.\n")
file_a.write("I am learning python, hope you like my examples.\n")
file_a.close()                      #close file to save memory
    
file_b=open("sample.txt","r")       #read file that created above
text = str(file_b.read())           #convert things inside file to string
print(text)                         #print out read result 
file_b.close()                      #close file to save memory
