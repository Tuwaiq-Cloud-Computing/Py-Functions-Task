List=[1,2,3,4]
#Write a function that takes two numbers and return their sum
def Fun1(a,b):
    return a + b
#Prints all the elements in the list using a for loop
for PrintList in List:
    print(PrintList)
#Write a Python program to sum all the items in the list
SumList = sum(List)
print(SumList)
#Write a Python program to get the largest number from the list
largest_Num = max(List)
print(largest_Num)
#write a function that take a list and a number then return a new partial list starting from index 0 to index "number"
def Par_list(List1, number):
    return List1[:number]
    result = Par_list(List, 3)
    print(result)
#Loop through the letters in the string: "Tuwaiq_Academy"
StringLoop = "Tuwaiq_Academy"
for result in StringLoop:
   print(result) 
#Consider this list = ["Python", "C++", "Java"] Exit the loop when x is equal to "C++"
Language_List = ["Python", "C++", "Java"]
for result in Language_List :
     print(result)
     if result == "C++":
         break
#Write a function that receives a list containing different numbers, rearranges the list so that the zeros are the end of the list, and finally returns the arranged list
def Zero_List(Q):
    X = [A for A in Q if A == 0]
    Y = [A for A in Q if A != 0]
    return Y + X
    list_= [6, 0, 5, 0, 7]
    result = Zero_List(list_)
    print (result)
    
