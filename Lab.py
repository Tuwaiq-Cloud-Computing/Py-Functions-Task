
def formaty(n):
    print("Q:", n)


def line():
    print("____________________")


# Q1:
formaty(1)


def SumN(num1, num2):
    print(num1 + num2)


SumN(1, 9)
line()

# Q2:
formaty(2)
my_list = [0, 7, 9, 0, 5]
for element in my_list:
    print(element)
line()

# Q3:
formaty(3)


def sum_list(lst):
    print(sum(lst))


sum_list(my_list)
line()

# Q4:
formaty(4)


def maxNum(lst):
    print(max(lst))


maxNum(my_list)
line()

# Q5:
formaty(5)


def partiallist(lst, number):
    print(lst[:number])


partiallist(my_list, 3)
line()

# Q6:
formaty(6)
Tuwaiq_list = "Tuwaiq_Academy"
for i in Tuwaiq_list:
    print(i)
line()

# Q7:
formaty(7)
list = ["Python", "C++", "Java"]
for x in list:
    print(x)
    if x == "C++":
        break
line()
# Q8:
formaty(8)


def rearrange_zeros(lst):
    zeros = []
    non_zeros = []
    for num in lst:
        if num == 0:
            zeros.append(num)
        else:
            non_zeros.append(num)
    print(non_zeros + zeros)


rearrange_zeros(my_list)
line()
