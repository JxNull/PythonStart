# Python024
#Author: Jingxiong Wu

#May/11/2018   
#Python exercise project 25

''' Class and Objects'''

class Token:
    supply= 5

    def buyticket(self):
        print('1 token used\n')
        if self.supply>=1:
            self.supply-=1
        else:
            print("You should buy more token.\n")

    def checktoken(self):
            print("Token avaliable:" + str(self.supply))


person_a=Token()
person_b=Token()

person_a.buyticket()
person_b.buyticket()
person_a.checktoken()
person_b.buyticket()
person_b.checktoken()
