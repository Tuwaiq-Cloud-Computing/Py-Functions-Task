#Additional Challenge
cont_Table = [
    {"name": "Ahmed", "Phone": "0551112222"},
    {"name": "Saad", "Phone": "0551113333"},
    {"name": "Sultan", "Phone": "0551114444"},
    {"name": "Morad", "Phone": "0551115555"},
    {"name": "Abdullah", "Phone": "0551116666"}
]

def lookup_owner(phone_number):
    if len(phone_number) != 10:
        return "This is an invalid number"

    if not phone_number.isdigit():
        return "This is an invalid number"

    for contact in cont_Table:
        if contact["Phone"] == phone_number:
            return contact["name"]

    return "Sorry, the number is not found"

# Example usage
number = input("Enter a phone number: ")
owner = lookup_owner(number)
print("Owner:", owner)