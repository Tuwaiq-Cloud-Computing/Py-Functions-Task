def total_num(n1,n2): #Question 1
    sum = n1 + n2
    return sum
print("the sum :", total_num(3,4))

List=[1,2,3,4]

for x in range(len(List)):  #Question 2
    print (List[x])

print("the sum of all items in list : ", sum(List)) #Question 3


print("largest number from the list", max(List)) #Question 4


def partial_ist(list, number):
    return list[:number]
    result = partial_ist(list, 2)
    print(result)


string = "Tuwaiq_Academy" #Question 6
for i in "Tuwaiq_Academy":
    print(i)

list1 = ["Python", "C++", "Java"] #Question 7
for i in list1:
    print(i)
    if i == "C++":
        break

list2 = [1,0,7,1,0]
def movs(list2): #Question 8
    non_zeros = [num for num in list2 if num != 0]
    zeros = [num for num in list2 if num == 0]
    return non_zeros + zeros
print( movs(list2))

contactTable=[{"name":"Ahmed","Phone":"0551112222"},
              {"name":"Saad","Phone":"0551113333"},
              {"name":"Sultan","Phone":"0551114444"},
              {"name":"Morad","Phone":"0551115555"},
              {"name":"Abdullah","Phone":"0551116666"}]

def Find_Woner(phone_number):
    if not phone_number.isdigit() or len(phone_number) != 10:
        print("this is an invalid number")
        return
    for contact in contactTable:
        if contact["Phone"] == phone_number:
            print("owner: ", contact["name"])
            return
    print("Sorry, the number is not found")
phone_number = input("enter a phone number : ")
Find_Woner(phone_number)






