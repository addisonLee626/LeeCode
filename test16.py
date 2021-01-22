def putarrayupsidedown(arr):
    length = len(arr)
    newArr =  []
    while length > 0:
        newArr.append(arr[length-1])
        length -= 1
    return newArr

array = [3,4,5]
print(putarrayupsidedown(array))

