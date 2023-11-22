List=[1,2,3,4]


#Q1 
def sum(n1,n2):
  result=n1+n2 
  return result

print(sum(10,100))
#Q2

for i in List:
  print(i)

#Q3
List=[1,2,3,4]
sum=0
for i in List:
    sum+=i
print(sum)
#Q4
List=[1,2,3,4]

print(max(List))

#Q5
def lists(list, number):
    lists = list[:number]
    return lists
print (lists([1, 2, 3, 4], 3))

#Q6
for letter in "Tuwaiq_Academy":
  print(letter)

#Q7
list = ["Python", "C++", "Java"]
for i in list:
    if i=="C++" :
        print("break")
        break
   
#Q8
 def N(list):
    for l in list:
        if l == 0:
            list.remove(l)
            list.append(0)
    return list

print(N([3, 0, 2, 0, 0, 1]))  