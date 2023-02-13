#Q1: Write a function that takes two numbers and return their sum
def add_num(a,b):
    sum=a+b
    return sum
num1=int(input("Enter the first number : "))
num2=int(input("Enter the second number  :"))
print("The sum is",add_num(num1,num2)) 

#-----------------

#Q2: Prints all the elements in the list using a for loop
list = ["Nujud", "Abdulaziz", "Ababtain"]
i=0
while i < len(list):
  print(list[i])
  i = i + 1

#-----------------

#Q3: Sum all the items in the list
list2 = [10,20,30,40]
print("The sum of List2 is", sum(list2))

#-----------------

#Q4: Get the largest number from the list
list2.sort() 
print("Largest number is:", list2[-1])

#-----------------

#Q5: write a function that take a list and a number then return a new partial list starting from index 0 to index "number"
list3=["Carrot", "Lemon", "Tomato"]
def my_function(list3,number):
    list3=list3[0:number]
    return list3

print(my_function(list3,1))

#-----------------

#Q6: Loop through the letters in the string: "Tuwaiq Academy"
t = 'Tuwaiq Academy'

for i in range(len(t)):
    print(t[i])

#-----------------
#Q7: Exit the loop when x is equal to "C++"
list3 = ["Python", "C++", "Java"]
for x in list3:
    print(x)
    if x == "C++":
        break

#-----------------
#Q8
list4 = [0,4,3,5,6,0,2,0]
  
def fun1(list4):

    nonzeros= [i for i in list4 if i != 0] 

    zeros = [j for j in list4 if j == 0] 

    list4 = nonzeros + zeros
    return list4

print(fun1(list4))


