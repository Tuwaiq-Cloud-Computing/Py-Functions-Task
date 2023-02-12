
contactTable=[{"name":"Ahmed","Phone":"0551112222"},
              {"name":"Saad","Phone":"0551113333"},
              {"name":"Sultan","Phone":"0551114444"},
              {"name":"Morad","Phone":"0551115555"},
              {"name":"Abdullah","Phone":"0551116666"}] 



val=input("Enter phone number:\n")
if not val.isdigit() or len(val) !=10:
    print("This is invalid number")
else:
   
  for dic in contactTable:
         
         if dic["Phone"] == val: 
           returnname=dic["name"]
           print(returnname)
           break
  else:
     print("Not Found")
             
