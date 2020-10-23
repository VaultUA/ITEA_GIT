def magic(a):
    b = []
    if a != 0:
        while 1 <= a:
            tmp = a // 2
            b.append(a - tmp * 2)
            a = tmp
    return b[::-1]


if __name__ == "__main__":
    x = ""
    while x != 0:
        x = int(input("Введите число для перевода: "))
        print(magic(x))
        if x == 0:
            break