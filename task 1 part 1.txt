# Question 1: Write a function that takes two numbers and return their sum
def add_two_numbers(num1, num2):
    sum = num1 + num2
    return sum

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = add_two_numbers(num1, num2)
print("The sum of the two numbers is:", result)
print("----------")

# Question 2: Prints all the elements in the list using a for loop
list = [1, 2, 3, 4]
print(" The orginal list is : ",list)
def print_list_elements(list):
    for i in list:
        print(i)
print_list_elements(list)
print("----------")

#Question 3: Write a Python program to sum all the items in the list
def sum_list(list):
    sum = 0
    for i in list:
        sum += i
    return sum


total_sum = sum_list(list)
print("The sum of the list is:", total_sum)
print("----------")


#Question 4: Write a Python program to get the largest number from the list
def get_largest_number(list):
    largest = list[0]
    for i in list:
        if i > largest:
            largest = i
    return largest


largest_number = get_largest_number(list)
print("The largest number in the list is:", largest_number)
print("----------")



#Question 5: write a function that take a list and a number then return a new partial list starting from index 0 to index "number"

def get_partial_list(list):
    end_index = int(input("Please enter the end index of the partial list: "))
    partial_list = list[:end_index]
    return partial_list


partial_list = get_partial_list(list)
print("The partial list is:", partial_list)
print("----------")


#Question 6: Loop through the letters in the string: "Tuwaiq_Academy"
str1 = "Tuwaiq_Academy"
for i in str1:
    print(i)
print("----------")


#Question 7: Consider this list = ["Python", "C++", "Java"] Exit the loop when x is equal to "C++"
list = ["Python", "C++", "Java"]

for x in list:
  if x == "C++":
   # print("Found C++")
    break
  else:
    print(x)
    
print("----------")


#Question 8: Write a function that receives a list containing different numbers, rearranges the list so that the zeros are the end of the list, and finally returns the arranged list
def move_zeros_to_end(list):
    n = len(list)
    count = 0
    for i in range(n):
        if list[i] != 0:
            list[count] = list[i]
            count += 1
    for i in range(count, n):
        list[i] = 0
    return list

list = [1, 2, 0, 4, 0, 5]
print("The original list is",list)
list = move_zeros_to_end(list)
print("The rearranged list is:", list)
print("----------")