import math

def decor(func):

    def wrapper(*args, **kwargs):
        print('Работает декоратор')
        res = func(*args, **kwargs)
        return res

    return wrapper

@decor
def sq(a, b, c):
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(s)
    return s

a = 5
b = 6
c = 7

print(sq(a, b, c))