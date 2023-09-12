List=[1,2,3,4]
#Question 1:
print(List)
def add_num(a, b):
    return a + b
print(add_num(5,5))
#Question 2:
for element in List:
    print(element)
#Question 3:
sum_of_list=sum(List)
print(sum_of_list)
#Question 4:
largest_num=max(List)
print(largest_num)
#Question 5:
def get_partial_list(lst, number):
 return lst[:number]
my_list6 = [1, 2, 3, 4, 5]
partial_list = get_partial_list(my_list6 , 3)
print(partial_list)

#Question 6
my_string = "Tuwaiq_Academy"
for letter in my_string:
 print(letter)

#Question 7
my_list = ["Python", "C++", "Java"]
for x in my_list:
   if x == "C++":
     break
   print(x)

#Question 8:
def rearrange_zeros(lst):
 zeros = [x for x in lst if x == 0]
 non_zeros = [x for x in lst if x != 0]
 return non_zeros + zeros

my_list = [1, 0, 5, 0, 3, 0, 8]
rearranged_list = rearrange_zeros(my_list)
print(rearranged_list)