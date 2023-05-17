# Py-Functions-Task

List=[1,2,3,4]
## Tasks:


- Question 1: Write a function that takes two numbers and return their sum 
n1=input("enter first num: ")
n1=int(n1)
n2=input("enter second num: ")
n2=int(n2)
def _sum(nn1,nn2):
    print(nn1+nn2)
_sum(n1,n2)

- Question 2: Prints all the elements in the list using a for loop
ListA=[1,2,3,4]
for x in ListA :
    print(x)
- 
- Question 3: Write a Python program to sum all the items in the list
ListA=[1,2,3,4]
sumX = 0
for x in ListA :
    sumX =x+sumX
print(sumX)

- Question 4: Write a Python program to get the largest number from the list
import math

ListA=[1,2,3,4]
x=max(ListA)
print(x)
    
- Question 5: write a function that take a list and a number then return a new partial list starting from index 0 to index "number"
n1 = input("enter the range :")
n1 = int(n1)

def pn(x):
    y=[]
    for i in range(0, x):
        y=i
        print(y)

pn(n1)

- Question 6: Loop through the letters in the string: "Tuwaiq_Academy
for i in "Tuwaiq_Academy":
    print(i)

- Question 7: Consider this ``` list = ["Python", "C++", "Java"] ``` Exit the loop when x is equal to "C++"
-for x in listA:
    if(x =="C++"):
        break
    print(x)
- Question 8: Write a function that receives a list containing different numbers, rearranges the list so that the zeros are the end of the list, and finally returns the arranged list
ListA = [3,0,4,0,5]

def rang(x):
    for i in x:
        if i == 0:
            x.remove(i)
            x.append(0)
    return print(x)



rang(ListA)


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
contactTable=[{"name":"Ahmed","Phone":"0551112222"},{"name":"Saad","Phone":"0551113333"}
              ,{"name":"Sultan","Phone":"0551114444"}
              ,{"name":"Morad","Phone":"0551115555"},
              {"name":"Abdullah","Phone":"0551116666"}] 


def find_contact_owner(number):
    if not number.isdigit() or len(number) != 10:
        return "This is an invalid number"
    
    for contact in contactTable:
        if contact["Phone"] == number:
            return f"The owner of the number {number} is {contact['name']}"
    
    return "Sorry, the number is not found"

number = input("Enter a 10-digit number: ")
result = find_contact_owner(number)
print(result)




## Submission:


- After finishing the task upload your Python script file to the forked repo and then create a pull request.

