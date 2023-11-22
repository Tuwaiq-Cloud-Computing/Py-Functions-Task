contactTable = [
    {"name": "Ahmed", "Phone": "0551112222"},
    {"name": "Saad", "Phone": "0551113333"},
    {"name": "Sultan", "Phone": "0551114444"},
    {"name": "Morad", "Phone": "0551115555"},
    {"name": "Abdullah", "Phone": "0551116666"},
]

phone_number = input("Enter phone number: ")

def find_name_by_phone_number(phone_number):
    if len(phone_number) != 10:
        return "This is invalid number"

    for contact in contactTable:
        if contact["Phone"] == phone_number:
            return contact["name"]

    return "Sorry, the number is not found"

name = find_name_by_phone_number(phone_number)

if name:
    print("The name of the owner is:", name)
else:
    print(name)


