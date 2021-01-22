def reOrder(array):
    odd_list = []
    even_list = []
    for i in array:
        if i & 1:
            odd_list.append(i)
        else:
            even_list.append(i)
    return odd_list + even_list


array1 = [1, 3, 2, 4, 5, 7, 8]
print(reOrder(array1))
