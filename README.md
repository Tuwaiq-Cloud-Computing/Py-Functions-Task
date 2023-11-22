# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#........................1
def add_numbers(a, b):
    return a + b

list = [1, 2, 3, 4]
result = add_numbers(list[0], list[1])
print("Result:", result)
#......................2
for item in list:
    print(item)
#....................3

print("Sum of the list:", sum(list))
#.......................4
print("Largest number in the list:", max(list))

#.....................5
def partial_list(list, number):
    return list[:number]
result = partial_list(list, 3)
print("Partial list:", result)
#.........................6
my_string = "Tuwaiq_Academy"
for letter in my_string:
    print(letter)
    
#....................7

programming_languages = ["Python", "C++", "Java"]
for language in programming_languages:
    if language == "C++":
        print(language)
        break
#........................8
my_list = [1, 2, 0, 3, 4]

def rearrange_zeros(my_list):
    non_zeros = [num for num in my_list if num != 0]
    zeros = [num for num in my_list if num == 0]

    arranged_list = non_zeros + zeros
    return arranged_list
result = rearrange_zeros(my_list)

print("Rearranged list with zeros at the end:", result)

#...............................................................................................
contactTable = [
    {"name": "Ahmed", "Phone": "0551112222"},
    {"name": "Saad", "Phone": "0551113333"},
    {"name": "Sultan", "Phone": "0551114444"},
    {"name": "Morad", "Phone": "0551115555"},
    {"name": "Abdullah", "Phone": "0551116666"}
]

#.........................................

def find_owner(phone_number):
    if not phone_number.isdigit() or len(phone_number) != 10:
        print("This is an invalid number.")
        return

    for contact in contactTable:
        if contact["Phone"] == phone_number:
            print(f"The owner of the number {phone_number} is {contact['name']}.")
            return
    print("Sorry, the number is not found.")

#.........................
find_owner("0551113333")  
find_owner("0551111234")  
find_owner("12345")       





    
