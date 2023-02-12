

#Question 1: Write a function that takes two numbers and return their sum
def sum_num(*args):
	return sum(args)

#Question 2: Prints all the elements in the list using a for loop
lst=list(range(11))
for item in lst:
	print(item)

#Question 3: Write a Python program to sum all the items in the list
print(sum(lst))

#Question 4: Write a Python program to get the largest number from the list
print(max(lst))

#Question 5: write a function that take a list and a number then return a new partial list starting from index 0 to index "number"

def partial_list(input_list, number):
    return input_list[:number]

print(partial_list([1,2,3,5,67,0,8,9],3))

#Question 6: Loop through the letters in the string: "Tuwaiq_Academy
name="Tuwaiq_Academy"
for char in name:
	print(char)

#Question 7: Consider this list = ["Python", "C++", "Java"] Exit the loop when x is equal to "C++"

lst2= ["Python", "C++", "Java"] 
for item in lst2:
	 if item == "C++":
	 	continue
	 else:
	  	print(item)

#Question 8: Write a function that receives a list containing different numbers, rearranges the list so that the zeros are the end of the list, and finally returns the arranged list

def func(item):
	return sorted(item)

print(func([0,40,4,0]))

	
	