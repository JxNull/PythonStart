# Python024
#Author: Jingxiong Wu

#May/11/2018   
#Python exercise project 10

''' Class and Objects'''

class Token:
    supply= 5

    def buyticket(self):
        print('1 token used\n')
        self.supply-=1

    def checktoken(self):
        if self.supply<=0:
            print("You should buy more token.\n")
        else:
            print("Token avaliable:" + str(self.supply))


person_a=Token()
person_b=Token()

person_a.buyticket()
person_b.buyticket()
person_a.checktoken()
person_b.buyticket()
person_b.checktoken()
