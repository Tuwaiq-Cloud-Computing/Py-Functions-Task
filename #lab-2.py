#Q1

print("Q1---------------")
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 4)
print(result)


#Q2
print("Q2---------------")
my_list = [1, 2, 3, 4]
for item in my_list:
    print(item)


#Q3

print("Q3---------------")
List = [1, 2, 3, 4]

list_sum = sum(List)
print(list_sum)




#Q4
print("Q4---------------")
List = [1, 2, 3, 4]

max_number = max(List)
print(max_number)

#Q5
print("Q5---------------")
def get_partial_list(lst, number):
    return lst[:number]

my_list = [1, 2, 3, 4, 5]
partial_list = get_partial_list(my_list, 3)
print(partial_list) 

#Q6
print("Q6---------------")
my_string = "Tuwaiq_Academy"
for letter in my_string:
    print(letter)

#Q7
print("Q7---------------")
my_list = ["Python", "C++", "Java"]
for x in my_list:
    if x == "C++":
        break
    print(x)

#Q8
print("Q8---------------")
def rearrange_zeros(lst):
    zeros = [x for x in lst if x == 0]
    non_zeros = [x for x in lst if x != 0]
    return non_zeros + zeros

my_list = [1, 0, 5, 0, 3, 0, 8]
rearranged_list = rearrange_zeros(my_list)
print(rearranged_list)


# The additional 
print ('------------------')
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

    

