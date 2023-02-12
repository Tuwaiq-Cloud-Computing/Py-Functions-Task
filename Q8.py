def rearrange_list(list):
    zeros = []
    non_zeros = []
    for i in list:
        if i == 0:
            zeros.append(i)
        else:
            non_zeros.append(i)
    return non_zeros + zeros
