
print("-----Q1-----")
def sumfun(a,b):
    sum= a + b
    return sum
print("the summation of two numbers= ",sumfun(3,4) )

print("-----Q2-----")
List=[1,2,3,4]
for i in List:
    print(i)

print("-----Q3-----")
print(sum(List))

print("-----Q4-----")
print(max(List))

print("-----Q5-----")
def indfun():
    a=input("enter your list: ")
    a=list(a)
    for a in range(0,5):
        print(a)
print(indfun())

print("-----Q6-----")
Nacd="Tuwaiq_Academy"
for i in Nacd:
    print(i)

print("-----Q7-----")
list = ["Python", "C++", "Java"]
for x in list:
    if x=="C++":
        break
    print(x)

print("-----Q8-----")
def storfun(strlst):
    strlst.sort()
    for st in strlst:
        if st == 0:
            strlst.remove(st)
            strlst.append(0)
    return print(strlst) 
strlst=[2,0,1,0,3,0]
storfun(strlst)
