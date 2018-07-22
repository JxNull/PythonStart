# Python027
#Author: Jingxiong Wu

#May/13/2018   
#Python exercise project 27

''' inheritance'''

class Token:
    token=0
    def __init__(self,name):
        self.name=name
        print(str(self.name)+'\n')

    def recieve_tk(self,x):
        self.token=self.token+x
        print('recieved '+str(x)+' in wallet\n')
        print(str(self.name)+ " : " +str(self.token)+'\n')

    def send_tk(self,x): 
        if self.token-x<=0:
            print("no enough tokens.\n")
            print(str(self.name)+ " : "+str(self.token)+'\n')
        else:
            self.token=self.token-x
            print(str(x)+' transfered\n')
            print(str(self.name)+" : "+str(self.token)+'\n')
    def balance():
        self.token=self.token
        print(str(self.name)+" : "+str(self.token)+'\n')
        
class Wallet(Token):
    def get_info(self):
        print(str(self.name)+" : "+str(self.token)+'\n')

address1=Wallet("NEO")
address2=Wallet("ONT")

address1.recieve_tk(50)
address1.send_tk(10)
address1.get_info()

address2.recieve_tk(10)
address2.send_tk(20)
address2.get_info()
