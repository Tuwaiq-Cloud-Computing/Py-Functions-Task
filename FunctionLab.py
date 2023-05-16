# Question 1: Write a function that takes two numbers and return their sum
def _sum(x, y):
    return x + y


print(_sum(5, 6))

# Question 2: Prints all the elements in the list using a for loop
myList = []

i = 0

for i in range(10):
    myList.append(i)

print("my list :", myList)
print("\n---------------------------------------------\n")
for j in myList:
    print(myList[j])


# Question 3: Write a Python program to sum all the items in the list
print("\n---------------------------------------------\n")


print(sum(myList))
# Question 4: Write a Python program to get the largest number from the list
print(max(myList))

# Question 5: write a function that take a list and a number then return a new partial list starting from index 0 to index "number"

def _partial_list(list, num):
    return list[:num+1]

number = 3
new_list = _partial_list(myList, number)
print(new_list)


# Question 6: Loop through the letters in the string: "Tuwaiq_Academy
tuwaiqAcademy ="Tuwaiq_Academy"
for i in tuwaiqAcademy:
    print(i)

print("\n---------------------------------------------\n")

# Question 7: Consider this list = ["Python", "C++", "Java"] Exit the loop when x is equal to "C++"
programmingLanguage = ["Python", "C++", "Java"]

for j in programmingLanguage:
    print(j,end=" , ")
    if(j=="C++"):
        break


print("\n---------------------------------------------\n")

# Question 8: Write a function that receives a list containing different numbers, rearranges the list so that the zeros are the end of the list, and finally returns the arranged list
import random

myNumbers=[0]
num =1
for num in range(11):
    # x = random.randint(-100, 100)
    x = random.randint(0, 100)
    myNumbers.append(x)


print("step 1",myNumbers)


myNumbers.sort()
print("step 2",myNumbers)

myNumbers.reverse()
print("step 3",myNumbers)

