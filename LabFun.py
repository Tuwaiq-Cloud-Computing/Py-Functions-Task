#Q1
def sumfunction(n1,n2):
    sumnumber = n1 + n2
    return print(sumnumber)
sumfunction(3,4)

#Q2
def listP():
    a = [1,2,3,4,5]
    for x in range(len(a)):
        print(a[x])
listP()

#Q3
def listsum():
    z = [1,2,3,4]
    print(z)
    sumlist = 0
    for i in range(len(z)):
        sumlist = sumlist + z[i]
        print(sumlist)
listsum()

#Q4
def maxnumber():
    list1 = [10,20,30,40,100]
    print("Largest Number is: ", max(list1))
maxnumber()

#Q5
def functionQfive(list,x):
    for i in range(list[x]-1):
        print(list[i])

list = [4,7,1,3,9]
functionQfive(list,2)

#6
def letterfunction():
    string_name = "Tuwaiq_Academy"
    for i in string_name:
        print(i)
letterfunction()


#7
def exitfunction():
    list = ["Python", "C++", "Java"]
    for i in list:
        print(i)
        if i == "C++":
            break
exitfunction()

#8
def movezerofunction(list):
    list.sort()
    new_list = [num for num in list if num != 0] + [num for num in list if num == 0]
    print(new_list)
list = [4,8,0,6,0,3,0,2]    
movezerofunction(list)

