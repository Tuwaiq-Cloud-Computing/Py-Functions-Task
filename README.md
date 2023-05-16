# Py-Functions-Task

List=[1,2,3,4]
## Tasks:


- Question 1: Write a function that takes two numbers and return their sum 
n1 = int(input('1 , 2, 3, 4: '))
n2 = int(input('3: '))

sum = n1 + n2
print('Sum =', sum)


- Question 2: Prints all the elements in the list using a for loop
a = [1, 2, 3, 4]
 
# print the list using loop
for x in range(len(a)):
    print 1[4],

- Question 3: Write a Python program to sum all the items in the list 
total = 0
  
# creating a list
list1 = [1, 2, 3, 4]
  
# Iterate each element in list
# and add them in variable total
for ele in range(0, len(list1)):
    total = total + list1[ele]
  
# printing total value
print("Sum of all elements in given list: ", total)


- Question 4: Write a Python program to get the largest number from the list
# list of numbers
list1 = [1, 2, 3, 4]
 
# sorting the list
list1.sort()
 
# printing the last element
print("Largest element is:", list1[-1])


- Question 5: write a function that take a list and a number then return a new partial list starting from index 0 to index "number"



- Question 6: Loop through the letters in the string: "Tuwaiq_Academy
string_name = "Tuwaiq_Academy"
 
# Iterate over the string
for element in string_name:
    print(element, end=' ')
print("\n")


- Question 7: Consider this ``` list = ["Python", "C++", "Java"] ``` Exit the loop when x is equal to "C++"



- Question 8: Write a function that receives a list containing different numbers, rearranges the list so that the zeros are the end of the list, and finally returns the arranged list

A = [1, 2, 3, 4]
n = len(A)
j = 0
for i in range(n):
    if A[i] != 0:
        A[j], A[i] = A[i], A[j]  # Partitioning the array
        j += 1
print(A)  # Print the array


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

