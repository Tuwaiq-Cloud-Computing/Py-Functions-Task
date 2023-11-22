
def sum_NO(a, b):
    return a + b

list = [1, 2, 3, 4]
elements = sum_NO(list[0], list[1])

print("Result:", elements)
for item in list:
    print(item)

def sum_list(list):
    return sum(list)
    
print("Total:", sum(list))  
  
print("Largest number is:", max(list))

def partial_list(list, number):
    return list[:number]
result = partial_list(list, 3)
print("Partial list:", result)
    
string = "Tuwaiq_Academy"
for letter in string:
    print(letter)

    my_list = ["Python", "C++", "Java"]
for language in my_list:
    if language == "C++":
        break
    print(language)
    
my_list = [1, 0, 3, 0, 5, 0, 7]

def rearrange_zeros(my_list):
    non_zeros = [num for num in my_list if num != 0]
    zeros = [num for num in my_list if num == 0]

    arranged_list = non_zeros + zeros
    return arranged_list
result = rearrange_zeros(my_list)

print("Zeros at the end:", result)

contactTable = [
    {"name": "Ahmed", "Phone": "0551112222"},
    {"name": "Saad", "Phone": "0551113333"},
    {"name": "Sultan", "Phone": "0551114444"},
    {"name": "Morad", "Phone": "0551115555"},
    {"name": "Abdullah", "Phone": "0551116666"}
]

def find_owner(phone_number):
    if not phone_number.isdigit() or len(phone_number) != 10:
        print("This is an invalid number.")
        return

    owner = next((contact["name"] for contact in contactTable if contact["Phone"] == phone_number), None)

    if owner:
        print(f"The owner of the number {phone_number} is {owner}.")
    else:
        print("Sorry, the number is not found.")


user_input = input("Enter a 10-digit phone number: ")
find_owner(user_input)

    
