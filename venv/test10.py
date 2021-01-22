def rectCover(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return rectCover(n-1) + rectCover(n-2)

num = 5
print(rectCover(num))