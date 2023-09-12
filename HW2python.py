import math
List=[1,2,3,4]
#Q1
def function1(num1,num2):
     result = num1 + num2 
     return result
print( function1(5,10) )
print("____________________________")

#Q2
for i in List:
     print(i)
print("____________________________")
#Q3
print( math.fsum(List))
print("____________________________")

#Q4
print("The largest number in the list is:",max(List))
print("____________________________")
 
#Q5

def function2(List,num):
     return List[ :num]
print(function2(List,2))
print("____________________________")

#Q6
for i in "Tuwaiq_Academy":
     print(i)
print("____________________________")

#Q7
list = ["Python", "C++", "Java"] 
for x in list:
     if x=="C++":
       print("break")
       break
     print(x)
print("____________________________")

#Q8

def function3(list):
    noZeros = [num for num in list if num != 0]
    zeros = [num for num in list if num == 0]
    return noZeros + zeros
print(function3(list=[3,0,2,0,1,0]))

