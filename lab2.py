List=[1,2,3,4]
print ("Q1")
def num_sum(a, b):

    return (a + b)

result = num_sum ( 532 , 619 )

print("**", result , "**")
print ("Q2")
for a in List :
    print(a)


print("Q3")


def lst_sum(lst):
        return sum(lst)

result2 = lst_sum(List)
print("**", result2 , "**")


print("Q4")

def lrg_num(lst):
    if len(lst) == 0:
        return None

    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest

result3 = lrg_num(List)
print("**", result3 , "**")

print("Q5")

def partial_list(lst, number):
    if number < 0:
        return []
    elif number >= len(lst):
        return lst
    else:
        return lst[:number+1]

result4 = partial_list(List, 1)
print(result4)

print("Q6")

String = "Tuwaiq_Academy"
for letter in String:
    print(letter)


print("Q7")


lang_list = ["Python", "C++", "Java"]

for lang in lang_list:

    print(lang)
    if lang == "C++":
      break

print("Q8")

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
print("**", result5 , "**")