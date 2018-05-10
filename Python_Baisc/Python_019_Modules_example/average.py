# Python019
#Author: Jingxiong Wu

#May/08/2018   
#Python exercise project 19

''' modules example'''

def ave(*args):
  i=0
  total=0
  for x in args:
    total+=x
    i+=1
  print( 'Average=',total/i)
