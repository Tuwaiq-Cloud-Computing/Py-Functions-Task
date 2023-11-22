list = [1, 2, 3, 4]

print("------------Q1------------")
print("")

def num_sum(a, b):
    
    return (a + b)

result = num_sum ( 203 , 72 )

print("******", result , "******")

print("------------Q2------------")
print("")

for a in list :
    print(a)

print("")
print("------------Q3------------")
print("")

def lst_sum(lst):
        return sum(lst)
    
result2 = lst_sum(list)
print("******", result2 , "******")
print("")

print("------------Q4------------")
print("")

def lrg_num(lst):
    if len(lst) == 0:
        return None
    
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest

result3 = lrg_num(list)        
print("******", result3 , "******")

print("------------Q5------------")
print("")

def partial_list(lst, number):
    if number < 0:
        return []
    elif number >= len(lst):
        return lst
    else:
        return lst[:number+1]

result4 = partial_list(list, 1)
print(result4)

print("------------Q6------------")
print("")

String = "Tuwaiq_Academy"
for letter in String:
    print(letter)
    

print("------------Q7------------")
print("")

lang_list = ["Python", "C++", "Java"]

for lang in lang_list:

    print(lang)

    if lang == "C++":
      break
    
print("------------Q8------------")

my_list = [1, 0, 5, 0, 3, 0, 8, 0 ,2, 3,0]

def end_zeros(lst):
    zeros = []
    non_zeros = []
    
    for num in lst:
        if num == 0:
            zeros.append(num)
        else:
            non_zeros.append(num)
    
    return non_zeros + zeros

result5 = end_zeros(my_list)
print("")

print("******", result5 , "******")

print("")
print("------------Additional Challenge------------")

contactT=[{"name":"Abdullah","Phone":"0554413327"},{"name":"Ahmed","Phone":"0551112222"},{"name":"Saad","Phone":"0551113333"},{"name":"Sultan","Phone":"0551114444"},{"name":"Morad","Phone":"0551115555"},{"name":"Abdullah","Phone":"0551116666"}]
def num_book(phone_number):
  if not Pnum.isdigit() or len(Pnum) != 10:
        return "This is an invalid number"
  for contact in contactT:
        if contact["Phone"] == Pnum:
            return contact["name"]

    # If the number is not found
        return "Sorry, the number is not found"
    
Pnum = input("Enter a phone number: ")
result6 = num_book(Pnum)
print(result6)