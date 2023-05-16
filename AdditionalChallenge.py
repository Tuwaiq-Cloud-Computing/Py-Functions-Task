def _phoneBook(phoneNumber):
    contactTable = [{"name": "Ahmed", "Phone": "0569861476"}, {"name": "Saad", "Phone": "0551113333"},
                    {"name": "Sultan", "Phone": "0551114444"}, {"name": "Morad", "Phone": "0551115555"},
                    {"name": "Abdullah", "Phone": "0551116666"}]

    if (len(phoneNumber) != 10):
        print("This is invalid number")
    else:
        if (not phoneNumber.isdigit()):
            print("This is invalid number ")
        else:
            for checkNumber in contactTable:
                if (checkNumber["Phone"] == phoneNumber):
                    print("The owner of the number is", checkNumber["name"])
                    return

            if (checkNumber["Phone"] != phoneNumber):
                    print("Sorry, the number is not found")






num_1 =_phoneBook("0569861476")
num_2 =_phoneBook("0569861000")
num_3 =_phoneBook("dfghjk")
num_4 =_phoneBook("0551115555")

num_1

num_2

num_3

num_4
