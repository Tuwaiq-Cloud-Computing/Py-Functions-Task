list = [1,2,3,4]

# Question 1: Write a function that takes two numbers and return their sum
def add(a,b):
    return a+b

print("Sum of 2 and 3 is ", add(2,3))

# Question 2: Prints all the elements in the list using a for loop
for x in list:
    print(x)

# Question 3: Write a Python program to sum all the items in the list
print("Sum of the following list ", list," is ", sum(list))

# Question 4: Write a Python program to get the largest number from the list
print("The largest number in the following list [1,2,3,4] is ", max(list))

# Question 5: write a function that take a list and a number then return a new partial list starting from index 0 to index "number"
def getPartialList(list, number):
    return list[:number]
print("Returning the list up to index 2 ", getPartialList(list, 2))

# Question 6: Loop through the letters in the string: "Tuwaiq_Academy"
print("Itterating through the string 'Tuwaiq_Academy'")
for x in "Tuwaiq_Academy":
    print(x)

# Question 7: Consider this list = ["Python", "C++", "Java"] Exit the loop when x is equal to "C++"
list2 = ["Python", "C++", "Java"]
print("Printing the list ", list2, " and breaks when it reaches C++")
for x in list2:
    print(x)
    if x == "C++":
        break

# Question 8: Write a function that receives a list containing different numbers, rearranges the list so that the zeros are the end of the list, and finally returns the arranged list
list3 = [1,0,7,0,8]
def rearrange(list3):
    non_zeros = [num for num in list3 if num != 0]
    zeros = [num for num in list3 if num == 0]
    return non_zeros + zeros
print("Rearrange the following array ", list3, " by printing the zeros at the end ", rearrange(list3))

# Additional Challenge:

contactTable=[
    {"Name":"Ahmed","Phone":"0551112222"},
    {"Name":"Saad","Phone":"0551113333"},
    {"Name":"Sultan","Phone":"0551114444"},
    {"Name":"Morad","Phone":"0551115555"},
    {"Name":"Abdullah","Phone":"0551116666"}]

# If the number exists, print the owner. Otherwise, print "Sorry, the number is not found".
def lookupOwner(phoneNum):
    for contact in contactTable:
        if contact["Phone"] == phoneNum:
            return contact["Name"]
    return "Sorry, the number is not found"

print("Check if the number 0551114444 is in the list ", lookupOwner("0551114444"))
print("Check if the number 0551114774 is in the list ", lookupOwner("0551114774"))

# If the number is less or more than 10 numbers, print "This is invalid number".
# If the number contains letters or symbols, print "This is invalid number".

for contact in contactTable:
    phone_number = contact["Phone"]
    if len(phone_number) != 10 or not phone_number.isdigit():
        print("This is an invalid number")