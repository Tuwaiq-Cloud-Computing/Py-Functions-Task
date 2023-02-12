#question1
def Sum_value(x,y):
    sum=x+y
    return sum
 
Val1=int(input("Enter the first number : "))
Val2=int(input("Enter the second number  :"))

print("The sum is",Sum_value(Val1,Val2))

#question2
list = ["Apple", "Banana", "Berry"]
for x in list:
  print(x)

#question3
Lab_list = [1,3,5,2,4]
print ("The sum of my_list is",sum(Lab_list))

#question4

Lab_list = [1,3,5,2,4]
print("Largest element is:", max(Lab_list))

#question5
Lab_list = [1,3,5,2,4]

def my_function(Lab_list,number):
    newlist=Lab_list[0:number]
    return newlist

print(my_function(Lab_list,3))

#question6

string_name = "Abdul"

for i, v in enumerate(string_name):
    print(v)
#question7
list_Test = ["Python", "C++", "Java"]
for x in list_Test:
    print(x)
    if x == "C++":
        break
    #Question8
    
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
