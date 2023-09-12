
def sume(x,y):
    return x+y
    

print(sume(5,4))


list = [1,2,3,4]
for i in range (0,len(list)): 
    print(list[i])

sum = 0 
for i in range (0,len(list)): 
    sum += list[i]

print(sum)##4

print(max(list)) ##5

def fun(list,x):##6
     
     new1 = [None]* x

     for i in range(0,len(new1)):
             new1[i] = list[i]
         
         
     return new1
       

print(fun(list,2))

T = "Tuwaiq_Academy"
for i in T:
     print(i)#6

list1  = ["Python", "C++", "Java"]
for i in range (0,len(list1)): #7
     if list1[i] == "C++":
          break
     else: 
          print(list1[i])



def Arange(arr):##8
    temp = []
    zeros = 0

    for i in range(len(arr)):
        if arr[i] == 0:
            zeros += 1
        else:
            temp.append(arr[i])

    arr = temp + [0] * zeros
    return arr




Arrang = [1,2,0,3,0,4,0,5,6]
print(Arange(Arrang))















    