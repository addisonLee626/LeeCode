def power(base, exponent):
    temp = base
    if base == 0.0 and exponent <= 0:
        return -1
    if base == 0.0:
        return 0
    if exponent == 0:
        return 1
    if exponent < 0:
        for i in range(-exponent-1):
            base *= temp
        return 1.0/base
    else:
        for i in range(exponent-1):
            base *= temp
        return base

b=4.0
e=2
print(power(b,e))