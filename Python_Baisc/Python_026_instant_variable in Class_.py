# Python026
#Author: Jingxiong Wu

#May/12/2018   
#Python exercise project 26

''' __init__,class, instant variable'''

class Token:
    supply=5
    def __init__(self,name):
        self.name= name
        print(str(self.name),"broughts "+str(self.supply)+' tokens.\n')
        

    def buyticket(self,x):
        print(str(self.name) + ' used '+ str(x)+" token\n")
        self.supply=self.supply-x

    def checktoken(self):
        if self.supply<=0:
            print(str(self.name)+" should buy more token.\n")
        else:
            print("Token avaliable: " + str(self.supply)+' for '+str(self.name)+"\n")


person_a=Token('a')
person_b=Token('b')

person_a.buyticket(1)
person_a.checktoken()
person_b.buyticket(2)
person_b.buyticket(3)
person_b.checktoken()
