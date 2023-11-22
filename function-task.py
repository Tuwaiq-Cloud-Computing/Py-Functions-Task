#Tasks:
list=[1,2,3,4]
#Question 1
def add_num(a, b):
    return a + b

res = add_num(2, 3)
print(res) 
#Question 2
for item in list:
    print(item)
#Question 3
total = sum(list)
print(total) 
#Question 4
max_num = max(list)
print(max_num) 
#Question 5
def get_partial_list(lst, number):
    return lst[:number]

my_list = [1, 2, 3, 4, 5]
partial_list = get_partial_list(my_list, 3)
print(partial_list)
#Question 6
string = "Tuwaiq_Academy"

for letter in string:
    print(letter)
#Question 7
list = ["Python", "C++", "Java"]

for x in list:
    print(x)
    if x == "C++":
        break 
#Question 8 
def rearrange_list(lst):
    zeros = [x for x in lst if x == 0]
    non_zeros = [x for x in lst if x != 0]
    return non_zeros + zeros

my_list = [0, 2, 0, 1, 0, 3, 4, 0]
rearranged_list = rearrange_list(my_list)
print(rearranged_list)  # Output: [2, 1, 3, 4, 0, 0, 0, 0]