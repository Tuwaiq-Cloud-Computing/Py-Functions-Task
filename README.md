# Py-Functions-Task

List=[1,2,3,4]
## Tasks:


- Question 1: Write a function that takes two numbers and return their sum 
     def func(x,y):
     sum=x+y
     print(sum) ask about input
     func(3,2)
     
- Question 2: Prints all the elements in the list using a for loop
    for x in List:
     print (x) 
- Question 3: Write a Python program to sum all the items in the list 
     print(sum(list))
- Question 4: Write a Python program to get the largest number from the list
     print(max(list))
     
- Question 5: write a function that take a list and a number then return a new partial list starting from index 0 to index "number"

def split(x:list, i:int):
return x[:n]

- Question 6: Loop through the letters in the string: "Tuwaiq_Academy
     string_name = "Tuwaiq_Academy"
     for element in string_name:
        print(element, end='  ')
     print("\n")
     
- Question 7: Consider this ``` list = ["Python", "C++", "Java"] ``` Exit the loop when x is equal to "C++"
      for x in list:
          if x=="C++":
              break
          print(x) 
- Question 8: Write a function that receives a list containing different numbers, rearranges the list so that the zeros are the end of the list, and finally returns the arranged list 
 def arrange(list):
    for i in list:
        if i == 0:
            list.remove(i)
            list.append(0)
    return print(list)
list = [0,4,6,0,4,0,2]
arrange(list)
   


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

