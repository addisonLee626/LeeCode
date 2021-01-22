def jumpFloor(number):
    if number == 1:
        return 1
    elif number == 2:
        return 2

    else:
        return jumpFloor(number-1) + jumpFloor(number-2)

n = 3
print(jumpFloor(n))

