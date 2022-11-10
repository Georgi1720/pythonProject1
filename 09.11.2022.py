stroka = input('Введите число: ')
for i in stroka:
    if i == i.isdigit():
        a.append(i)
    elif i != i.isdigit() and i == '*':
        result = a[int(i) - 1] * a[int(i)+1]
print(result)

def mult(x, y):
    result = x * y
    return result

def division(x, y):
    result = x * y
    return result

def plus(x, y):
    result = x * y
    return result

def minus(x, y):
    result = x * y
    return result






