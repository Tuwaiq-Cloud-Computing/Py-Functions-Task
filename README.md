#Question 1: Write a function that takes two numbers and return their sum
def sum_num(a,b):

    sum=a+b;
    return sum;
number1=int(input("Enter the first number: "))
number2=int(input("Enter the secound number: "))
print("The results are",sum_num(number1,number2))


#Question 2: Prints all the elements in the list using a for loop
List=[1,2,3,4]
for x in range(len(List)):
    print (List[x])

    
#Question 3: Write a Python program to sum all the items in the list
sum_all=(0)

List=[1,2,3,4]
for x in range(0, len(List)):
    sum_all=sum_all + List[x]
print("List all elements: ", sum_all)


#Question 4: Write a Python program to get the largest number from the list
List=[1,2,3,4]
List.sort()
print(" The Largest number is: ", List[-1])


#Question 5: write a function that take a list and a number then return a new partial list starting from index 0 to index "number"

def listfunc():
    newlist=[]
    lastindex = int(input("Enter last index: "))
    i = 0

    for i in range(i, lastindex+1):
        newlist.append(i)
        print("my list: ", newlist)
        cut = int(input("Enter cut list: "))
        print(newlist[0:cut+1])

listfunc()


#Question 6: Loop through the letters in the string: "Tuwaiq_Academy

string_name = "Tuwaiq Academy"
for element in string_name[0:14:1]:
    print(element, end =" ")

#Question 7: Consider this list = ["Python", "C++", "Java"] Exit the loop when x is equal to "C++"

list = ["python", "C++", "java"]
for x in list:
    if x == "C++":
        break
    print(x)

#Question 8: Write a function that receives a list containing different numbers, rearranges the list so that the zeros are the end of the list, and finally returns the arranged list

def arrange(list1):
    for i in list1:
        if i == 0:
            list1.remove(i)
            list1.append(0)
        return print(list1)
list1 = [0,1,8,0,5,7,9]
arrange(list1)
