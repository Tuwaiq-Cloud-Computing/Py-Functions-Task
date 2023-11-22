
#Question 1:
def sum_of_two_numbers(num1, num2):
  sum = num1 + num2
  return sum

#Question 2:
List = [1, 2, 3, 4]
for element in List:
  print(element)

#Question 3:
List = [1, 2, 3, 4]
total_sum = sum(List)
print(total_sum)

#Question 4:
List = [1, 2, 3, 4]
largest_number = max(List)
print(largest_number)

#Question 5:
def partial_list(input_list, number):
  partial_list = input_list[:number]
  return partial_list

#Question 6:
string = "Tuwaiq_Academy"
for letter in string:
  print(letter)

#Question 7:
list = ["Python", "C++", "Java"]
for x in list:
  if x == "C++":
    break
  print(x)

#Question 8:
def rearrange_list(input_list):
  zeros_list = []
  non_zeros_list = []
  for number in input_list:
    if number == 0:
      zeros_list.append(number)
    else:
      non_zeros_list.append(number)
  arranged_list = non_zeros_list + zeros_list
  return arranged_list

#Question 9:
import re

def find_contact(phoneNumber):
    if not re.match(r"\d{10}", phoneNumber):
        print("This is an invalid number.")
        return

    # Search for the contact in the contact table
    for contact in contactTable:
        if contact["Phone"] == phoneNumber:
            print(f"The owner of the phone number {phoneNumber} is {contact['name']}.")
            return

    # If the number is not found, print a message
    print("Sorry, the number is not found.")

contactTable = [{"name": "Ahmed", "Phone": "0551112222"},
              {"name": "Saad", "Phone": "0551113333"},
              {"name": "Sultan", "Phone": "0551114444"},
              {"name": "Morad", "Phone": "0551115555"},
              {"name": "Abdullah", "Phone": "0551116666"}]

# Get the phone number from the user
phoneNumber = input("Enter a phone number: ")

find_contact(phoneNumber)
