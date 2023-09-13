# Q1
def sumnum(a, b):
    return a+b
print(sumnum(3,3))

# Q2
list=[1,2,3,4]
for item in list:
    print(item)
    
# Q3
total = sum(list)
print("Sum:", total)

# Q4
print(max(list))

# Q5
def part(lis, num):
    return list[:num]
print(part(list,2))

# Q6
str = "Tuwaiq_Academy"
for let in str:
    print(let)
    
# Q7
langs = ["Python", "C++", "Java"]
for language in langs:
    if language == "C++":
        break
    print(language)

# Q8
def arrange(les):
    non_zero_elements = [x for x in les if x != 0]
    zero_elements = [x for x in les if x == 0]
    return non_zero_elements + zero_elements
listAr = [0,2,0,3,0,1]
print(arrange(listAr))

#Additional Challenge
cont_Table = [
    {"name": "Ahmed", "Phone": "0551112222"},
    {"name": "Saad", "Phone": "0551113333"},
    {"name": "Sultan", "Phone": "0551114444"},
    {"name": "Morad", "Phone": "0551115555"},
    {"name": "Abdullah", "Phone": "0551116666"}
]

def find_name(phone_number):
    # Input validation
    if not phone_number.isdigit() or len(phone_number) != 10:
        print("This is invalid number")
        return

    for contact in cont_Table:
        if contact["Phone"] == phone_number:
            print("Name:", contact["name"])
            return

    print("Sorry, the number is not found")
    
    
phone_number = input("Enter 10-digit phone number: ")
find_name(phone_number)
    