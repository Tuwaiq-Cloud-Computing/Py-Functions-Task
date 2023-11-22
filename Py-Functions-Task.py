list=[1,2,3,4]
#Q1
def sum_num(num1, num2):
    return num1 + num2

result = sum_num(1, 2)
print("Sum:", result)

#Q2
for i in list:
    print(i)
#Q3    
list_sum = sum(list)
print("sum of all numbers in list ", list_sum)

#Q4
largest_num = max(list)
print("Largest number in the list:", largest_num)

#Q5
def partial_list(lst, num):
    partial = lst[:num]
    return partial

my_list = [1, 2, 3, 4, 5]
result = partial_list(my_list, 3)
print("Partial List:", result)

#Q6
list1 = "Tuwaiq_Academy"
for i in list1:
    print(i)

#Q7    
list2 = ["Python", "C++", "Java"]
for x in list2:
    print(x)
    if x =="C++":
        break
    
#Q8
def rearrange_zeros(lst):
  
    non_zero_elements = [num for num in lst if num != 0]
    count_zeros = len(lst) - len(non_zero_elements)
    arranged_list = non_zero_elements + [0] * count_zeros
    return arranged_list

mixed_list = [2, 0, 5, 8, 0, 3, 0, 1]
result = rearrange_zeros(mixed_list)

print("Arranged List:", result)


 
