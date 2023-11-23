def num_sum(a, b):
    return (a + b)

result = num_sum(25, 27)
print ("this is the result ", result) 

list = [1, 2, 3, 4]

for x in list:
  print(x)

def calculate_sum(list):
    total_sum = 0
    for item in list:
        total_sum += item
    return total_sum

total_sum = calculate_sum(list) 
print("The sum of all elements in the list:", total_sum)

large_num = max(list)
print("the large number in the lis is ", large_num)


def partial_list(lst, number):
    if number < 0:
        return []
    elif number >= len(lst):
        return lst
    else:
        return lst[:number+1]

result4 = partial_list(list, 1)
print(result4)

String = "Tuwaiq_Academy"
for letter in String:
    print(letter)

lang_list = ["Python", "C++", "Java"]

for lang in lang_list:

    print(lang)
    if lang == "C++":
      break

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
