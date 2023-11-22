# Py-Functions-Task

List=[1,2,3,4]
## Tasks:


- Question 1: Write a function that takes two numbers and return their sum

def function (a,b):
    result=a+b
    return result
print (function (1,3))
  _____________________________________________________________________________________
- Question 2: Prints all the elements in the list using a for loop
 list = [1,2,3,4]
for x in list:
  print(x)
  ____________________________________________________________________________________
- Question 3: Write a Python program to sum all the items in the list
  num = [1,2,3,4]
sum_all_items=sum(num)
print (f"the sum is:{sum_all_items}")
______________________________________________________________________________________
- Question 4: Write a Python program to get the largest number from the list
  num = [1,2,3,4]
largest=max(num)
 print ({largest})
______________________________________________________________________________________
- Question 5: write a function that take a list and a number then return a new partial list starting from index 0 to index "number"
 def function (list,number):
 new_list = list[:number]
 return new_list
list=[2,4,6,8,10]
print( function(list,4))
print( function(list,2))
__________________________________________________________________________________________
  
- Question 6: Loop through the letters in the string: "Tuwaiq_Academy"
 for x in "Tuwaiq_Academy":
  print(x)
  ____________________________________________________________________________________________
- Question 7: Consider this ``` list = ["Python", "C++", "Java"] ``` Exit the loop when x is equal to "C++"
list = ["Python", "C++", "Java"]
for x in list:
  print (x)
  if x=="C++":
    break
  ______________________________________________________________________________________________
- Question 8: Write a function that receives a list containing different numbers, rearranges the list so that the zeros are the end of the list, and finally returns the arranged list

def function(list):
      # zcount=list.count(0)
      for x in list:
          list.remove(0)
          list.append(0)
      return list

newlist=[0,3,7,0,7]
result = function(newlist)
print(result)
__________________________________________________________________________________________________________________



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

