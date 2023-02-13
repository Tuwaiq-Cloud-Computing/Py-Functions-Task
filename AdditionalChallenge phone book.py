# phone book program
#Q1
contactTable=[{"name":"Ahmed","Phone":"0551112222"},
{"name":"Saad","Phone":"0551113333"},
{"name":"Sultan","Phone":"0551114444"},
{"name":"Morad","Phone":"0551115555"},
{"name":"Abdullah","Phone":"0551116666"}]
def CheckOwner():
#Q2,3,4
    for phonebook in contactTable:
     Num = input('Enter phone Number:\n')
     if len(Num) != 10 or not (Num.isdigit()):
        print("invalid phone number")
        continue
     for Contacts in contactTable :
        if Contacts.get("Phone") == Num:
            print(Contacts["name"])
            return   
    print("Sorry, the number is not found")      
CheckOwner()


