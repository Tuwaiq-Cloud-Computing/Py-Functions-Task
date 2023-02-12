list = [1, 2, 3, 4, 5]

def get_largest_number(list):
    largest_number = list[0]
    for i in list:
        if i > largest_number:
            largest_number = i
    return largest_number

result = get_largest_number(list)
print(result)

