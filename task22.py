#1
def sumfunction (num1,num2):
  sum =num1 + num2
  print("answer: ", sum )

sumfunction(3+6)


#q2
list = [1,2,3,4]
for x in list:
   print(x)

#3
List=[1,2,3,4]
print(sum(List))

#4
List=[1,2,3,4]
print(max(List))


#5 
def listFunc():

    newList =[]
    lastIndex = int(input("enter last index: "))
    i = 0

    for i in range(i, lastIndex+1):
        newList.append(i)
        print ("my new list: ", newList)

        cut = int (input("enter cut list: "))

        print(newList[0:cut+1])
      
      
listFunc() 
 

#6
for x in "TuwaiqAcademy":
    
     print(x) 


#7
list = ["Python", "C++", "Java"]
for x in list:
   if x == "C++":
      break
   print(x) 
#8

def arrange(list1):
   
   for i  in list1:
      if i == 0:
            list1.remove(i)
            list1.append(0)
            list1.append(0)
      return print(list1)      
        
  
list1 = [0,1,3,0,5,7,9]
arrange(list1)