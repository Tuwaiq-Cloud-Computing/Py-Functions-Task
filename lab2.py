#Q1
print("---------------------------")
def addnum(a, b):
    return a + b
result = addnum(3,2)
print(result)

#Q2
print("---------------------------")
List = [1, 2, 3, 4]

for element in List:
    print(element)

#Q3
print("---------------------------")
List = [1, 2, 3, 4]

list_sum = sum(List)
print(list_sum)

#Q4
print("---------------------------")
List = [1, 2, 3, 4]

x = max(List)
print(x)

#Q5
print("---------------------------")

def get_partial_list(lst, number):
    return lst[:number]

my_list = [1, 2, 3, 4, 5]
partial_list = get_partial_list(my_list, 3)
print(partial_list)  # Output: [1, 2, 3]


#Q6
print("---------------------------")
s = "Tuwaiq_Academy"
for letter in s:
    print(letter)

#Q7
print("---------------------------")
listl = ["Python", "C++", "Java"]

for x1 in listl:
    if x1 == "C++":
        break
    print(x1)

#Q8
print("---------------------------")
def rearrange_zeros(lst):
    zeros = [x2 for x2 in lst if x2 == 0]
    non_zeros = [x2 for x2 in lst if x2 != 0]
    return non_zeros + zeros

list2 = [1, 0, 5, 0, 3, 0, 8]
rearranged_list = rearrange_zeros(list2)
print(rearranged_list)


# the additional challange
print("---------------------------")

def phone_book(contact_table, number):
    if len(number) != 10:
        return "This is an invalid number. It should have exactly 10 digits."
    
    if not number.isdigit():
        return "This is an invalid number. It should only contain digits."
    
    for contact in contact_table:
        if contact["Phone"] == number:
            return "Owner: " + contact["name"]
    
    return "Sorry, the number is not found."

contact_table = [
    {"name": "Ahmed", "Phone": "0551112222"},
    {"name": "Saad", "Phone": "0551113333"},
    {"name": "Sultan", "Phone": "0551114444"},
    {"name": "Morad", "Phone": "0551115555"},
    {"name": "Abdullah", "Phone": "0551116666"}
]

number = input("Enter the phone number: ")
result = phone_book(contact_table, number)
print(result)
