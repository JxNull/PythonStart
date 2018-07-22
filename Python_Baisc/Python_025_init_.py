# Python025
#Author: Jingxiong Wu

#May/12/2018   
#Python exercise project 25

''' __init__'''

class Token:
    supply=5
    def __init__(self):
        print("Token brought :"+str(self.supply))
        

    def buyticket(self,x):
        print('used '+ str(x)+" token\n")
        temp = self.supply-x
        if temp<=0:
            print("You should buy more token.\n")
        else:
            self.supply=self.supply-x

    def checktoken(self):

            print("Token avaliable:" + str(self.supply))


person_a=Token()
person_b=Token()

person_a.buyticket(1)
person_a.checktoken()
person_b.buyticket(2)
person_b.buyticket(3)
person_b.checktoken()
