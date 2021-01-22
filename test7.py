# def fibonacci(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     fone = 1
#     fzero = 0
#     for i in range(2, n+1):
#         fn = fone + fzero
#         fzero = fone
#         fone = fn
#     return fn


def fibonacci(n):
    if n < 0:
        return -1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def isNumber():
    n1 = input("请输入一个数字,输入#退出:")
    while not n1.isdigit():
        if n1 == '#':
            exit(0)
        else:
            n1 = input("请输入一个有效数字:")
    else:
        return int(n1)


print(fibonacci(isNumber()))
