# Py-Functions-Task

List=[1,2,3,4]
## Tasks:


- Question 1: Write a function that takes two numbers and return their sum 
- Question 2: Prints all the elements in the list using a for loop
- Question 3: Write a Python program to sum all the items in the list 
- Question 4: Write a Python program to get the largest number from the list
- Question 5: write a function that take a list and a number then return a new partial list starting from index 0 to index "number"
- Question 6: Loop through the letters in the string: "Tuwaiq_Academy
- Question 7: Consider this ``` list = ["Python", "C++", "Java"] ``` Exit the loop when x is equal to "C++"
- Question 8: Write a function that receives a list containing different numbers, rearranges the list so that the zeros are the end of the list, and finally returns the arranged list

# Task2
List=[1,2,3,4,]

#Q1
def sum(x,y):
    print(x+y)

x= input("enter x: ")
x= int(x) #to convert input from string to int
y= input("enter y: ")
y=int(y)
sum(x,y)

#Q2
for i in List:
    print(i)

#Q3
print("the sum of the list: ", sum(List))

#Q4
print ("the largest number is: ", max(List))

#Q5
def list():

    newList =[]
    Lindex = int(input("Enter the last index: "))
    i=0

    for i in range (i,Lindex+1):
        newList.append(i)
    print("my new list: ", newList)

    cut = int(input("Enter the cut index: "))
    print(newList[0:cut+1])

list()


#Q6
A= "Tuwaiq_Academy"
for x in A:
    print(x)

#Q7
list = ["Python", "C++", "Java"]
for i in list:
    if i == "C++":
        break
    print (i)

#Q8
def arrange(Alist):
    for i in Alist:
        if i ==0:
            Alist.remove(i)
            Alist.append(0)
    return print(Alist)

Alist = [0,3,5,4,0,6,0,4]
arrange(Alist)

## Additional Challenge:


- Build a phone book program that receives the phone number, and returns the name of the owner.
You can follow the table below:

## Contact Table

| Name | Number |
| --- | ------------- |
| Ahmed | 0551112222 |
| Saad | 0551113333 |
| Sultan | 0551114444 |
| Morad | 0551115555 |
| Abdullah| 0551116666 |

This is the list of dictionaries you can use to build this function:

```contactTable=[{"name":"Ahmed","Phone":"0551112222"},{"name":"Saad","Phone":"0551113333"},{"name":"Sultan","Phone":"0551114444"},{"name":"Morad","Phone":"0551115555"},{"name":"Abdullah","Phone":"0551116666"}] ```

- If the number exists, print the owner. Otherwise, print "Sorry, the number is not found".
- If the number is less or more than 10 numbers, print "This is invalid number".
- If the number contains letters or symbols, print "This is invalid number".


## Submission:


- After finishing the task upload your Python script file to the forked repo and then create a pull request.

