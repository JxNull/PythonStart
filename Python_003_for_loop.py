# Python003
#Author: Jingxiong Wu

#April/30/2018   
#Python exercise project 3
#for loop

menu=['meat','vegetable','fruit']
meat=['bacon', 'beef', 'chicken','tuna','salmon']
vege=['carrot','beans','potato','mushroom']
fruit=['apple','banana','coconut','orange']
for a in menu[:1]:
    print(a)
    print(len(a))
    for m in meat:
        print(m)
        print(len(m))
for b in menu[1:2]:
    print(b)
    print(len(b))
    for v in vege:
        print(v)
        print(len(v))

for c in menu[2:3]:
    print(c)
    print(len(c))
    for f in fruit:
        print(f)
        print(len(f))
