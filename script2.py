#Question1
def sum(a,b):
    result = a+b
    return print(result)

#Question2
def printElement():
    list = [10,20,30,40]
    for i in list:
        print(i)

#Question3
def sumItems():
    list = [10,20,30,40]
    result = 0
    for i in list:
        result += i
    return print(result)

#Question4
def largest():
    list = [10,20,30,40]
    x = 0
    for i in list:
        if i > x:
            x = i
    return print(x)

#Question5
def partialList(list , x):
    for i in range(list[x]-1):
        print(list[i])


MyList = [7,2,3,4,5,6]
#partialList(MyList, 3)

#Question6
def letterLoop():
    text = "Tuwaiq_Academy"
    for i in text:
        print(i)

#Question7
def listLoop():
    list = ["Python", "C++", "Java"]
    for i in list:
        if i == "C++":
            break

#Question8
def arrange(list1):
    for i in list1:
        if i == 0:
            list1.remove(i)
            list1.append(0)
    return print(list1)
list1 = [0,1,3,0,5,7,9]
#arrange(list1)

