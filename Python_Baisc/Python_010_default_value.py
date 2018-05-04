# Python010
#Author: Jingxiong Wu

#May/04/2018   
#Python exercise project 10

''' Default value for arguments example'''

def trading_statement(state='N/A'):
    if state is 'green':
        state='earn'
    elif state is 'red':
        state='lost'
    print(state)

trading_statement()
trading_statement('green')
trading_statement("red")
