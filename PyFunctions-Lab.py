#Question 1
def sum_two_numbers(num1, num2):
    return num1 + num2

#-----------------------------------#
#Question 2
def print_list_elements(my_list):
    for element in my_list:
        print(element)
    List = [1,2,3,4]
    print_list_elements(List)

#-----------------------------------#
#Question 3
List = [1,2,3,4]
sum_of_list = sum(List)
print("The sum of the list is:", sum_of_list)

#-----------------------------------#
#Question 4
List = [1,2,3,4]
largest_number = max(List)
print("The largest number is:", largest_number)

#-----------------------------------#
#Question 5
def get_partial_list(input_list, index):
    if index < 0 or index > len(input_list):
        return "Index out of range"
    else:
        return input_list[:index]

List = [1, 2, 3, 4]
number = 3
print(get_partial_list(List, number))

#-----------------------------------#
#Question 6
string = "Tuwaiq_Academy"
for letter in string:
    print(letter)

#-----------------------------------#
#Question 7
second_list = ["Python", "C++", "Java"]
for x in second_list:
    if x == "C++":
        print("Found 'C++', exiting the loop.")
        break
    print(x)

#-----------------------------------#
#Question 8
def move_zeros_to_end(liist):
    return sorted(liist, key=lambda x: x == 0)

print(move_zeros_to_end([0, 1, 0, 3, 12]))

#-----------------------------------#
#Question 9 (Additional Challenge)
contactTable = [
    {"name": "Ahmed", "Phone": "0551112222"},
    {"name": "Saad", "Phone": "0551113333"},
    {"name": "Sultan", "Phone": "0551114444"},
    {"name": "Morad", "Phone": "0551115555"},
    {"name": "Abdullah", "Phone": "0551116666"}
]

def find_owner(phone_number):
    
    if len(phone_number) != 10:
        return "This is an invalid number."

    if not phone_number.isdigit():
        return "This is an invalid number."

    
    for contact in contactTable:
        if contact['Phone'] == phone_number:
            return f"The owner of the phone number is {contact['name']}."

    return "Sorry, the number is not found."

#نجرب البحث عن رقم أحمد فقط
print(find_owner("0551112222"))
print(find_owner("0551116789"))
print(find_owner("05511122222"))
print(find_owner("05511A2222"))