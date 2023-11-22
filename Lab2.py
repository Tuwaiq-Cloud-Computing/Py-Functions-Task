##################################################################
def add_numbers(a, b):
    return a + b

list = [1, 2, 3, 4]
result = add_numbers(list[0], list[1])
print("Result:", result)

###############
for item in list:
    print(item)
###############

 print("Sum of the list:", sum(list))
###############


 print("Largest number in the list:", max(list))

###############
def partial_list(list, number):
    return list[:number]
result = partial_list(list, 3)
print("Partial list:", result)
###############
my_string = "Tuwaiq_Academy"
for letter in my_string:
    print(letter)

###############

programming_languages = ["Python", "C++", "Java"]
for language in programming_languages:
    if language == "C++":
        print(language)
        break
###############
my_list = [1, 2, 0, 3, 4]

def rearrange_zeros(my_list):
    non_zeros = [num for num in my_list if num != 0]
    zeros = [num for num in my_list if num == 0]

    arranged_list = non_zeros + zeros
    return arranged_list
result = rearrange_zeros(my_list)

print("Rearranged list with zeros at the end:", result)

###############
contactTable = [
    {"name": "Ahmed", "Phone": "0551112222"},
    {"name": "Saad", "Phone": "0551113333"},
    {"name": "Sultan", "Phone": "0551114444"},
    {"name": "Morad", "Phone": "0551115555"},
    {"name": "Abdullah", "Phone": "0551116666"}
]

###############

def find_owner(phone_number):
    if not phone_number.isdigit() or len(phone_number) != 10:
        print("This is an invalid number.")
        return

    for contact in contactTable:
        if contact["Phone"] == phone_number:
            print(f"The owner of the number {phone_number} is {contact['name']}.")
            return
    print("Sorry, the number is not found.")

################






