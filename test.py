

def find(array,target):
    if not array:
        return False
    rows=len(array)
    columns=len(array[0])
    row=0
    column=columns-1
    while row<rows and column>=0:
        if array[row][column]==target:
            return True
        if array[row][column]>target:
            column=column-1
        else :
            row=row+1
    return False
array1=([1,2,3,4],[5,6,7,8],[9,10,11,12])
target1=4
if find(array1,target1):
    print("in the array")
else:
    print("not in the array")







