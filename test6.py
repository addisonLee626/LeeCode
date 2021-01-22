def rotateArray(array):
    for i in range(len(array)):
        if array[i] > array[i+1]:
            return array[i+1]

arr = [6,7,8,2,3,4,5]
print(rotateArray(arr))