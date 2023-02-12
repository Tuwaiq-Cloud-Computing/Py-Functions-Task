#Py-Functions-Task

#Question1 :

first_num = int(input("Enter the first number\n"))
second_num = int(input("Enter the second number\n"))

def Addition(num1,num2):
    Total = num1 + num2
    return Total

print("the total sum of ",first_num,"and",second_num,"is", Addition(first_num,second_num))

#Question2 :
names = ["Fatma" , "Atheer" , "Roba"]
for i in names:
    print (i)


#Question3 :
counter=0
Totalsum =0
numbers = [ 1 , 2 , 3 , 4 ,100] 

for y in numbers:
    if len(numbers)>= counter:
        Totalsum += y
        counter+=1
print("the total sum is ",Totalsum)    


#Question4 :
print ("The Largest number of the list is :",max(numbers))

#Question5 :
num = [ 2 , 4 , 6 , 8 , 10 ]
def Generator (num2,list1):
    updatednum=[0]
    for z in list1:
        if z != num2:
            updatednum.append(z)
        elif z == num2:
            updatednum.append(z)
            break
    return updatednum

print ("Your list :\n",num,"\nThe list after update the numbers :\n",Generator(6,num))            


#Question6 :
text = "Tuwaiq_Academy"
for r in text:
    if r != "_":
        print(r)

#Question7 :
languge = ["Python", "C++", "Java"]

for x in languge:
    if x == "C++":
        break
    else:
        print(x)


#Question8 :

randomnum = [2,6,0,4,0,9,0,3]   

def sorting (list3):
    zeros=[]
    other=[]
    for i in list3:
        if i != 0 :
            other.append(i)
        else:
            zeros.append(i)  
        final=other+zeros     
    return final         

    

print ("Your list:\n",randomnum,"\nYour list after sorting the zeros:\n",sorting(randomnum))