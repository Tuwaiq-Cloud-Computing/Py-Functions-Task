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

print("-----Q1-----")
def sumfun(a,b):
    sum= a + b
    return sum
print("the summation of two numbers= ",sumfun(3,4) )

print("-----Q2-----")
List=[1,2,3,4]
for i in List:
    print(i)

print("-----Q3-----")
print(sum(List))

print("-----Q4-----")
print(max(List))

print("-----Q5-----")
def indfun():
    a=input("enter your list: ")
    a=list(a)
    for a in range(0,5):
        print(a)
print(indfun())

print("-----Q6-----")
Nacd="Tuwaiq_Academy"
for i in Nacd:
    print(i)

print("-----Q7-----")
list = ["Python", "C++", "Java"]
for x in list:
    if x=="C++":
        break
    print(x)

print("-----Q8-----")
def storfun(strlst):
    strlst.sort()
    for st in strlst:
        if st == 0:
            strlst.remove(st)
            strlst.append(0)
    return print(strlst) 
strlst=[2,0,1,0,3,0]
storfun(strlst)


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

