# replace' 'with 20%
def replace_space(s):
    result = ''
    for i in s:
        if i == ' ':
            result += '20%'
        else:
            result += i
    return result


ss = 'we love the world'
print(replace_space(ss))
