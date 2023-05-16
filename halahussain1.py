#answer1
def sum_two_numbers(num1,num2):
    return num1+num2
list=[1,2,3,4]
result=sum(list)
print(result)
#answer2
list=[1,2,3,4]
for element in list:
  print(element)
#answer3
list=[1,2,3,4]
sum_list=sum(list)
print(sum_list)
#answer4
list=[1,2,3,4]
largest_num=max(list)
print(largest_num)
#answer5
def listfunc():
   newlist=[]
   lastIndex=int(input("Enter last Index"))
   i=0
   for i in range(i,lastIndex):
      newlist.append(i)
   print("My list", newlist)
   cut=int(input("Enter cut list"))
   print(newlist[0:cut+1])
   print(newlist[0:cut+1])
listfunc()
#answer6
string="Tuwaiq academy"
for letter in string:
  print(letter)
#answer7
list=["python","c++","java"]
for language in list:
   if language =="c++":
      break
   print(language)
#answer8
def arrange(list1):
   for i in list1:
      if i ==0:
         list1.remove(i)
         list1.append(0)
   return print(list1)
list1=[0,1,3,0,5,7,9]
arrange(list1)
