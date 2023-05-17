contactTable = [{"name": "Ahmed", "phone": "0551112222"},
                {"name": "Saad", "phone": "0551113333"},
                {"name": "Sultan", "phone": "0551114444"},
                {"name": "Morad", "phone": "0551115555"},
                {"name": "Abdullah", "phone": "0551116666"}]

search_phone = input("enter the number: ")

if search_phone == "0551112222":
    print("tha name is: Ahmed")
elif search_phone == "0551113333":
    print("tha name is: Saad")
elif search_phone == "0551114444":
    print("tha name is: Sultan")
elif search_phone == "0551115555":
    print("tha name is: Morad")
elif search_phone == "0551116666":
    print("tha name is: Abdullah")
else: 
    print("Name is not found in contacts")