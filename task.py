#Q1
def _sum(n1,n2):
    print(n1+n2)


num1=input("Enter number 1 : ")

num1=int(num1)

num2=input("Enter number 2 : ")

num2=int(num2)

print(_sum(num1,num2))

#Q2
list = (1,2,3,4)
for i in list: 
    print(i)

#Q3
print(sum(list))

#Q4
print(max(list))

#Q5
def _range(x):
    numbers = range(x)
    for i in numbers:
        print(i)



num=input("Enter a number  : ")
num=int(num)    
print(_range(num))

#Q6
result = "Tuwaiq_Academy"
for i in result:
    print (i)

#Q7
list = ["Python", "C++", "Java"]
for i in list:
    if i == "C++":
        break
    print (i)

#Q8
list = input('Enter elements of a list separated by space ')
print("\n")
user_list = list.split()
# print list
print('list: ', user_list)

# convert each item to int type
for i in range(len(user_list)):
    # convert each item to int type
    user_list[i] = int(user_list[i])

user_list.sort()
user_list.reverse()
print("Sorted list is = ", user_list)



