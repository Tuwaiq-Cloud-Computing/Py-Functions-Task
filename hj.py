print("Q1")

def sumFunc(num1, num2):
    sum = num1 + num2
    print(sum)
sumFunc(20,7)
#----------------------------------------
print("Q2")
list = [1,2,3,4] #print elemnt using for
for elment in list:
   print(elment)
#--------------------------------------
print("Q3")
sum = 0 
list = [1,2,3,4] #sum all the items in the list 
for ele in range(0, len(list)):
    sum = sum + list[ele]
print (sum)
#-------------------------------------------
print("Q4")
def large_elment( list ): #print the largest elment in the list
    larg = list[ 0 ]
    for a in list:
        if a > larg:
            larg = a
    return larg
print(large_elment([1,2,3,4]))
#------------------------------------------
print("Q5")
def listfunc():

    newlist=[]
    lastIndex = int(input("Enter last index :"))
    i = 0

    for i in range(i, lastIndex+1):
        newlist.append(i)
        print("my new list ",newlist)

        cut = int(input("enter cut list: "))

        print(newlist[0:cut+1])

listfunc()
#---------------------------------------------------
print("Q6")
loop_letters = "Tuwaiq_Academy" #print loop letters
for letters in loop_letters:
    print(letters, end="\n")
#----------------------------------------
print("Q7")
list = ["python" , "c++" , "java"]

for x in list :
    if x== "c++":
        break
    print(x)
 #--------------------------------------
print("Q8") 
def arrange(list1):
    for i in list1:
        if i ==0:
             list1.remove(i)
             list1.append(0)
        return print(list1)
list1 = [0,1,3,0,5,7,9]
arrange(list1)
