#Question 1
def sumQ1(x,y):
    return x+y

#Question 2
def printQ2(x: list):
    for i in x:
        print(i)

#Question 3
def sumQ3(x: list):
    sum=0
    for i in x:
        sum+=i
    return sum

#Question 4
def largestQ4(x:list):
    largest=x[0]
    for i in x:
        if i >largest:
            largest=i
    return largest

#Question 5
def splitQ5(x:list, n:int):
    return x[:n]

#Question 6
def loopStringQ6():
    for i in "Tuwaiq_Academy":
        print(i)
        
#Question 7
def loopListQ7():
    list = ["Python", "C++", "Java"]
    for i in list:
        if i == "C++":
            break
        print(i)

#Question 8
def arrangeQ8(x:list):
    index=0
    for i in range(len(x)):
        if x[i] != 0:
            x[index]=x[i]
            index+=1
    while index < len(x):
        x[index]=0
        index+=1
    return x

