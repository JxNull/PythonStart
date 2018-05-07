# Python012
#Author: Jingxiong Wu

#May/06/2018   
#Python exercise project 12
''' keyword arguement example'''


def simple_sentence(name='a',action='b',item='c'):
  print(name,action,item)

simple_sentence()                           # result in " a b c "
simple_sentence("e", "f", "g")                    # result in " e f g "
simple_sentence(item='f',action='e')        # result in " a e f "
