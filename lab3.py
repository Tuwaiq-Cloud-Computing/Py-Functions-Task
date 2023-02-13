


#Q1
def my_function(x,y):
  return print(x * y)

my_function(3,5)

#Q2
List=[1,2,3,4,5]
for i in List:
         print(i)

#Q3
sum = 0
count = 0
 
list1 = [1, 1, 1, 1, 1]
 
while(count < len(list1)):
    sum = sum + list1[count]
    count += 1
     
# printing total value
print("Sum of all elements = : ", sum)

#Q4
list2 = [10, 20, 4, 45, 99]
print("Largest element is:", max(list2))

#Q5
def my_function(num = [], *x):
  for x in num:
    print(x)

list1 = [1, 2, 3]

my_function(list1,1)


#Q5
num = [1,2,3,4,5]
def my_function(num,list):
    liist=[0]
    for x in list:
        if x != num:
            liist.append(x)
        elif x == num:
            liist.append(x)
            break
    return liist
    
print ("list :\n",num,"\n the list after update the numbers :\n", my_function(3,num))
    
#Q6
string_name = "Tuwaiq_Academy"
 
for element in string_name:
    print(element, end=' ')
print("\n")


#Q7
list6 = ["Python", "C++", "Java"]

for element1 in list6:
  if element1 != "C++":
       print("list :\n",element1)
  else:
      break
  
  #Q8
  numberList = [3,2,0,7,0,5,9,0]   

def fun1 (listnum):
    zeros=[]
    other=[]
    for i in listnum:
        if i == 0 :
            zeros.append(i)
        else:
            other.append(i)  
        final=other+zeros     
    return final         

print ("Your list:\n",numberList,"\nYour list after sorting the zeros:\n",fun1(numberList))



