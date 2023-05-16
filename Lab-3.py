#lab-3


List=[1,2,3,4]

#Q1

def GetSum(x,y):
    return x+y

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))

print ("the Sum is :" , GetSum(num1,num2))

#Q2

for i in List:
    print(i)
    

#Q3 

def ListSum(list):
    l=len(list)
    sum=0
    for i in range(l) :
       sum=sum+list[i]
    
    print("The Sum is ",sum) 

ListSum(List)

#Q4

def GetLarg(list):
    return max(list)

print("The Largest number is ",GetLarg(List))


#Q5
#check phone photo

def CreatList(x):
    Listf=[]
    for i in range(0,x+1):
        Listf.append(i)

    return Listf

numf=int(input("enter index of list:"))
print(CreatList(numf))

#Q6

location="Tuwaiq_Academy"
for i in location:
       print(i)



#Q7

List7= ["Python", "C++", "Java"]
l7=len(List7)
for i in range(l7):
    #print(List7[i])
    if List7[i]=="C++":
        exit()


#Q8
#check phone photo

List8=[0,70,8,9,0,5,7]
List8.sort()
List8.reverse()
print (List8)
