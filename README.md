# Py-Functions-Task


## Tasks:


- Question 1: Write a function that takes two numbers and return their sum 
#Q1
first_number = int(input("Enter first number:  "))
second_number = int(input("Enter second number:  "))
def sum(first, second):
    return first + second
print("the sum of ",sum(first_number ,second_number))

- Question 2: Prints all the elements in the list using a for loop
#Q2
a = [1, 2, 3, 4, 5]
for i in a:
   print("Element: " + str(i) )

- Question 3: Write a Python program to sum all the items in the list
- Question 4: Write a Python program to get the largest number from the list
#Q3,4
def sum_of_list(l):
  total = 0
  for val in l:
    total = total + val
  return total
my_list = [1,3,5,2,4]
my_list.sort()
print ("The sum of my_list is", sum_of_list(my_list),"the largest element is :",my_list[-1])

- Question 5: write a function that take a list and a number then return a new partial list starting from index 0 to index "number"
#Q5
mylist = [ 1,2,3 ]
def Generator (num,list1):
     updatednum=[0]
     for x in list1:
         if x != num:
             updatednum.append(x)
         elif x == num:
             updatednum.append(x)
             break
     return updatednum
print ("\nThe list :\n",Generator(2,mylist)) 

- Question 6: Loop through the letters in the string: "Tuwaiq_Academy
#Q6
name = "Tuwaiq_Academy"
for element in name:
    print(element, end=' ')

- Question 7: Consider this ``` list = ["Python", "C++", "Java"] ``` Exit the loop when x is equal to "C++"
#Q7
languge = ["Python", "C++", "Java"]
for i in languge:
     if i == "C++":
         break
     else:
         print(i)

- Question 8: Write a function that receives a list containing different numbers, rearranges the list so that the zeros are the end of the list, and finally returns the arranged list
#Q8
a = [1, 2, 3, 0, 0, 4, 5]
def func(a):
    return sorted(a,reverse=True)
print(func(a))


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

