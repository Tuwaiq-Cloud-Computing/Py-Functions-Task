#Q1

def add_numbers(a, b):
    return a + b

#Q2
my_list = [1, 2, 3, 4]
for item in my_list:
    print(item)

#Q3
my_list = [1, 2, 3, 4]
total = sum(my_list)
print("Sum:", total)

#Q4
my_list = [1, 2, 3, 4]
max_number = max(my_list)
print("Largest number:", max_number)

#Q5
my_list= [1,2,3,4]
def get_partial_list(my_list, number):
   return  my_list[:number]

print(get_partial_list(my_list,3))

#Q6
my_string = "Tuwaiq_Academy"
for letter in my_string:
    print(letter)

#Q7
programming_languages = ["Python", "C++", "Java"]
for language in programming_languages:
    if language == "C++":
        break
    print(language)

#Q8
def rearrange_list_with_zeros(lst):
    non_zero_elements = [x for x in lst if x != 0]
    zero_elements = [x for x in lst if x == 0]
    return non_zero_elements + zero_elements


#Additional Challenge: 
contactTable = [
    {"name": "Ahmed", "Phone": "0551112222"},
    {"name": "Saad", "Phone": "0551113333"},
    {"name": "Sultan", "Phone": "0551114444"},
    {"name": "Morad", "Phone": "0551115555"},
    {"name": "Abdullah", "Phone": "0551116666"}
]

def find_owner(phone_number):
    # Input validation
    if not phone_number.isdigit() or len(phone_number) != 10:
        print("This is an invalid number")
        return
    
    for contact in contactTable:
        if contact["Phone"] == phone_number:
            print("Owner:", contact["name"])
            return
    
    print("Sorry, the number is not found")

# Get phone number input from the user
phone_number = input("Enter a 10-digit phone number: ")

# Call the function to find the owner
find_owner(phone_number)