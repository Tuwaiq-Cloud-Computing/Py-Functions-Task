list=[1, 2, 3,4]


# def add_numbers(a, b):
#     return a + b
# result = num (1, 2)
# print(result)




# List = [1, 2, 3, 4]
# for element in List:
#     print(element)




# for item in list:
#     print(item)




# total = sum(list)
# print(total)




# largest = max (list)
# print(largest)




# def partial_list(list, number):
#     return list [:number]
# result = partial_list( [1, 2, 3, 4, 5], 3)
# print(result)



# my_string = "Tuwaiq_Academy"
# for letter in my_string:
#     print(letter)



# list = ["Python", "C++", "Java"]
# for Lang in list:
#     if Lang == "c++":
#         break
#     print(Lang)




def rearrange_zeros(list):
    non_zeros = [x for x in list if x != 0]
    zeros = [x for x in list if x == 0]
    return non_zeros + zeros
result = rearrange_zeros( [1, 0, 2, 0, 3, 4, 0, 5])
print(result)
