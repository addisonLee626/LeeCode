def longfind(tar,arr):
    for b in arr:
        if tar in b:
            return True
        else:
            return False

arr1=([1,2,3,4],[5,6,7,8],[9,10,11,12])
tar1=7
if longfind(tar1,arr1):
    print("在队列里")
else:
    print("不再队列里")