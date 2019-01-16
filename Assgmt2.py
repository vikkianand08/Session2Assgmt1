# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 20:01:05 2019

@author: Nutan Anand
"""



list1=[];
inp1=input("accepts a sequence of comma-separated numbers");
list1=inp1.split(",")
print("Asgmt2 listing display:%s" %list1)




print("Asgmt2 Create the below pattern using nested for loop in Python")
for i in range(5):
    for j in range(i):
        print ('* ', end=" ")
    print('')
for i in range(5,0,-1):
    for j in range(i):
        print('* ', end=" ")
    print('')
    
    
print("Asgmt2 To reverse a word after accepting the input from the user")
str1=input("Accepting  word from user")
len1=len(str1)-1
for i in range(len1,-1,-1):
    print(str1[i],end="")
str2=input("Accepting another word from user:")
str3=str2[::-1]


print("Asgmt2 to print the given string in the format specified in the sample output")
stra=("WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a SOVEREIGN,!SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all its citizens")
print("WE, THE PEOPLE OF INDIA, \n\t\thaving solemnly resolved to constitute India into a SOVEREIGN,!\n\t\t\t\tSOCIALIST, SECULAR, DEMOCRATIC REPUBLIC\n\t\t\t\t and to secure to all its citizens")






    