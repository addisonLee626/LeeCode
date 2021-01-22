def power(base,exponent):
    temp = base
    if base == 0.0 and exponent < 0:
        return -1
    if base == 0.0 :
        return 0
    if exponent == 0:
        return 1
    if exponent <0:
        for i in range(0,-exponent-1):
            base *= temp
        return 1/base
    else:
        for i in range(0,exponent-1):
            base *= temp
        return base

b = 3
ex = -2
print(power(b,ex))
