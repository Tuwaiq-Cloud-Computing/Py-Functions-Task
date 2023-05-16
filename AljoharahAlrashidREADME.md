# Py-Functions-Task

List=[1,2,3,4]
## Tasks:


- Question 1: Write a function that takes two numbers and return their sum 
def _mul(n1,n2):
    print(n1+n2)

num1=input("Enter number 1 : ")

num1=int(num1)

num2=input("Enter number 2 : ")

num2=int(num2)


- Question 2: Prints all the elements in the list using a for loop
List=[1,2,3,4]
for element in List:
 print(element)


- Question 3: Write a Python program to sum all the items in the list 
def sum_of_list(l):
  total = 0
  for val in l:
    total = total + val
  return total

List=[1,2,3,4]
print "The sum of my_list is", sum_of_list(List)


- Question 4: Write a Python program to get the largest number from the list

List = [1, 2, 3, 4]
max_num = max(List)
print("The largest number in the list is:", max_num)


- Question 5: write a function that take a list and a number then return a new partial list starting from index 0 to index "number"
def get_partial_list(lst, num):
    return lst[:num]

my_list = [1, 2, 3, 4]
partial_list = get_partial_list(my_list, 3)
print(partial_list)  


- Question 6: Loop through the letters in the string: "Tuwaiq_Academy
string = "Tuwaiq_Academy in python"

for letter in string:
    print(letter)


- Question 7: Consider this ``` list = ["Python", "C++", "Java"] ``` Exit the loop when x is equal to "C++"
list = ["Python", "C++", "Java"]
for x in list:
    if x == "C++":
        break
    print(x)


- Question 8: Write a function that receives a list containing different numbers, rearranges the list so that the zeros are the end of the list, and finally returns the arranged list
list [0,2,1,6,3]
print("The original list 1 is : " + str(list))

res = [ele for ele in list]

print("The list after sorting is : " + str(res))


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

