#Q1''''''''''''''''''''''''''''''''

def sum11(x, y):
    
    sum = x + y
    
    print(sum) 
    
sum11(5, 6)

#Q2''''''''''''''''''''''''''''''
list = [1,2,3,4]
for x in list:
    print(x)

#Q3''''''''''''''''''''''''''''''

list7 = [1, 2, 3, 4]
total = 0

for ele in list7:
	total = total + ele

print("Sum of all elements in given list: ", total)

    
#Q4''''''''''''''''''''''''''''''''
 
z = [1,2,3,4]
    
print(max(z))
      
#Q5''''''''''''''''''''''''''''''''

def func(number):
    
    list2 = [*range(0, number, 1)]
    
    print(list2)

func(5)

#Q6'''''''''''''''''''''''''''''''''

for x in "Tuwaiq_academy":
    
    print(x)
    
 
#Q7''''''''''''''''''''''''''''''''''

list3 = ['python', 'C++', 'Java']

for x in list3:
    if x == list3[1]:
        break
    
    print(x)
    
#8''''''''''''''''''''''''''''''''''''''


list4 = [0, 10, 2, 0, 8]
list4.sort()
list4.reverse()

print(list4)


#Additional Challenge''''''''''''''''''''''''''''''


def find_owner(phone_number, contact_table):
    
    int(phone_number)
    if  len(phone_number) != 10:
        return "This is an invalid number"

    for x in contact_table:
        if x["Phone"] == phone_number:
            return x["name"]

    return "Sorry, the number is not found"


contact_table = [
    {"name": "Ahmed", "Phone": "0551112222"},
    
    {"name": "Saad", "Phone": "0551113333"},
    
    {"name": "Sultan", "Phone": "0551114444"},
    
    {"name": "Morad", "Phone": "0551115555"},
    
    {"name": "Abdullah", "Phone": "0551116666"},
]

phone_number = input("Enter a phone number: ")
print(find_owner(phone_number, contact_table))



    
