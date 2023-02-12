
'''Write a function that takes two numbers and return their sum'''
firstnum=eval(input("insert first number:\n"))
secondnum=eval(input("insert second number:\n"))

def sum1(firstnum,secondnum):
    return firstnum+secondnum

print(sum1(firstnum,secondnum))

'''Prints all the elements in the list using a for loop'''
list1=['Java','Python','C++']
for i in list1:
    print(i)

'''Write a Python program to sum all the items in the list'''
numbers=[1,2,3,4]
sumitems=sum(numbers)
print(sumitems)

'''Write a Python program to get the largest number from the list'''
max_height = max(numbers)
print(max_height)


''' write a function that take a list and a number then return a new partial list starting from index 0 to index "number"'''
def my_function(mylist,number):
    newlist=fruits[0:number]
    return newlist

fruits = ["apple", "banana", "cherry","Orange","Strawberry"]

print(my_function(fruits,2))

'''Loop through the letters in the string: "Tuwaiq_Academy"'''
str="Tuwaiq_Academy"
for i in str:
    print(i)

'''Exit the loop when x is equal to "C++"'''
list = ["Python", "C++", "Java"]
for i in list:
    print(i)
    if i =="C++":
      break
print("End of loop")


''' Write a function that receives a list containing different numbers, rearranges the list so that the zeros are the end of the list,
and finally returns the arranged list'''

listnum = [0,11,2,4,0,5,0]

def fun1(listnum):

    nonzeros= [i for i in listnum if i != 0] 

    zeros = [j for j in listnum if j == 0] 

    listnum = nonzeros + zeros
    return listnum

print(fun1(listnum))

