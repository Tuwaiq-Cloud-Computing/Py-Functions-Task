# Question 1

def function(a ,b ):
    return a + b 

print(function(4 , 4))

# Question 2

List=[1,2,3,4]

for item in List:
    print(item)

# Question 3

total = sum(List)
print("The Total Sum:", total)

# Question 4

print("The Largest number:", max(List))

# Question 5

def partial_list(List, num):
    return List[:num]

print(partial_list(List,3))

# Question 6

my_string = "Tuwaiq_Academy"
for i in my_string:
    print(i)

 # Question 7
    
list = ["Python", "C++", "Java"]

for x in list:
    if x == "C++":
        break
    print(x)

# Question 8

def rearrange_list(lst):
    non_zero_elements = [x for x in lst if x != 0]
    zero_elements = [x for x in lst if x == 0]
    return non_zero_elements + zero_elements

my_list = [1,0,4,2,0]
print(rearrange_list(my_list))


# Additional Challenge

contactTable=[{"name":"Ahmed","Phone":"0551112222"},
              {"name":"Saad","Phone":"0551113333"},
              {"name":"Sultan","Phone":"0551114444"},
              {"name":"Morad","Phone":"0551115555"},
              {"name":"Abdullah","Phone":"0551116666"}] 


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


phone_number = input("Enter a 10-digit phone number: ")

find_owner(phone_number)