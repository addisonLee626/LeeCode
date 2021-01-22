def findkthtotail(arr,k):
    length = len(arr)
    return arr[length-k]

array = [1,2,3,4,5]
k = 1
print(findkthtotail(array,k))
