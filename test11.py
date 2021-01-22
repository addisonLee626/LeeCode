def numberOf1(n):
    count = 0
    if n < 0:
        n = n & 0xfffffff
        #return n
    while n:
        if(n & 1):
            count += 1
        n = n >> 1

    return count

num = 5
print(numberOf1(num))

def demo(m):
    i = 0
    while m > 0:
        m = m & (m-1)
        i+= 1
    print(i)

mun = 5
print(demo(mun))




