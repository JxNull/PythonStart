# Python001
#Author: Jingxiong Wu

#April/16/2018   
#Python exercise project 1

# List
Student=[]                        # list of student created
Student.append(1)                 #append BTI function only can add one at a time
print(Student)                    # print [1]
Student.append(3)                 # return [1,3]
Student[:] = []                   # return []
Student + [5,7,9]                 # instant list/variable, return [1,3,5,7,9]
print(Student)                    # return [1,3]
newStudent=Student+[5, 7,9]       # return [1,3,5,7,9]
print(newStudent[:2])             # print [1,3,5]
newStudent[:2]=[]                 # return [7,9]
