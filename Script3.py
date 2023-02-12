#Task 1
print("Taske1: Write a function that takes two numbers and return their sum")

def sum1(first_number, second_number):
    return first_number + second_number


print(sum1(3,4)) 

#Task 2 
print("Taske2: Prints all the elements in the list using a for loop")
Mylist = [10, 12, 8 ,15]
for i in Mylist:
  print(i)

#Task 3 

print("Taske3: Write a Python program to sum all the items in the list")
# we will use previouse list 
total=0
for number in Mylist:
    total += number
#use sum function 
total2 = sum(Mylist)

print("use For loop:\n",total,"\n use Sum Function:\n", total2)

#Task 4 

print("Write a Python program to get the largest number from the list")
#use Max Function 
print(max(Mylist))

# Task 5 
# write a function that take a list and a number then return a new partial list starting from index 0 to index "number"
print("Enter index number:")
x=int(input())

if x > len(Mylist):
    print("numbers is greater than list")
else:
    print(Mylist[0:x])

#Task 6 
#Loop through the letters in the string: "Tuwaiq_Academy

Words="Tuwaiq_Academy"
for i in Words:
    print(i)

#Task 7 
#Consider this list = ["Python", "C++", "Java"] Exit the loop when x is equal to "C++"
list3 = ["Python", "C++", "Java"]
print("Please enter course")
cor=str(input())

for course in list3:
    if course==cor:
        break
    print(course)


#Task 8 
#Write a function that receives a list containing different numbers, 
# rearranges the list so that the zeros are the end of the list, and finally returns the arranged list
 
def pushZerosToEnd(arr, n):
	count = 0 
	for i in range(n):
		if arr[i] != 0:
			arr[count] = arr[i]
			count+=1
	
	while count < n:
		arr[count] = 0
		count += 1
		
arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
n = len(arr)
pushZerosToEnd(arr, n)
print("Array after pushing all zeros to end of array:")
print(arr)




