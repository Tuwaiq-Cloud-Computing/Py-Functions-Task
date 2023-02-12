# Question 1: Write a function that takes two numbers and return their sum
num1 = input ('Enter first number')
num2 = input ('Enter secod number')
total = int (num1) + int (num2)
print (f'total = {total}')
# Question 2: Prints all the elements in the list using a for loop
mylist = ['a', 'b', 'c']
for i in mylist:
    print (i)
# Question 3: Write a Python program to sum all the items in the list
numlist = [1, 2, 3]
print (sum (numlist))
# Question 4: Write a Python program to get the largest number from the list
larglist = [2, 5, 3, 7]
larglist.sort (reverse = True)
print (larglist [0])


# Question 5: write a function that take a list and a number then return a new partial list starting from index 0 to index "number"
def myfunc (someList: list, num: int):
    return someList.append (num)


# Question 6: Loop through the letters in the string: "Tuwaiq_Academy
tempStr = 'Tuwaiq_Academy'

for element in tempStr:
    print (element)
# Question 7: Consider this list = ["Python", "C++", "Java"] Exit the loop when x is equal to "C++"
list = ["Python", "C++", "Java"]
for i in list:
    if i == 'C++':
        break
    else:
        print (i)


# Question 8: Write a function that receives a list containing different numbers, rearranges the list so that the zeros are the end of the list, and finally returns the arranged list
def sortFunc (tempList: list):
    return tempList.sort (reversed = True)