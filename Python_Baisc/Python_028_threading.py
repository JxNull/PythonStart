# Python028
#Author: Jingxiong Wu

#May/15/2018   
#Python exercise project 28

''' threading'''
import threading

class RunningMan(threading.Thread):
    def run(self):
        for x in range(5):
            print(x)
            print(threading.currentThread().getName())


x= RunningMan(name='Deng Chao\n')
y= RunningMan(name='Chen He\n')
x.start()
y.start()
