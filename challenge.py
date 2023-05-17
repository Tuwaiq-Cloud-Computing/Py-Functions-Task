#challenge 


# Build a phone book program that receives the phone number, 
# and returns the name of the owner

contactTable= [
               {"name":"Ahmed","Phone":"0551112222"},
               {"name":"Saad","Phone":"0551113333"},
               {"name":"Sultan","Phone":"0551114444"},
               {"name":"Morad","Phone":"0551115555"},
               {"name":"Abdullah","Phone":"0551116666"},
               {"name":"maymoonah","Phone":"0555652026"}
               ] 


num=input("Enter Phone Number: ")
IsNum=num.isnumeric()
numLen= len(num)


#If the number contains letters or symbols, print "This is invalid number".
if IsNum==False:
    print("This is invalid number")
    exit()

#If the number is less or more than 10 numbers, print "This is invalid number".
elif numLen != 10:
     print("This is invalid number")
     exit()

#If the number exists, print the owner. Otherwise, print "Sorry, the number is not found".
else:
   
    llen=len(contactTable)
    
    for i in range(llen) :
        
       if contactTable[i]['Phone']==num:
        print ("Phone owner name is ",contactTable[i]['name'])
        exit()
        
    
print("Sorry, the number is not found")





