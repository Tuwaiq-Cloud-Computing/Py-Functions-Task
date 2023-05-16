#Additional Chllenge
def numberBook():
    num=""
    num=input("Please enter the phine number ")
    if len(num) != 10 or not (num.isdigit):
        print("This is invalid number")
    else:
        contactTable=[{"name":"Ahmed","Phone":"0551112222"},{"name":"Saad","Phone":"0551113333"},{"name":"Sultan","Phone":"0551114444"},{"name":"Morad","Phone":"0551115555"},{"name":"Abdullah","Phone":"0551116666"}] 
        x=[element for element in contactTable if element["Phone"] == num]
        if len(x)>0:
            print("The name of the owner is "+x[0]["name"])
        else:
            print("Sorry, the number is not found")