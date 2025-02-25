from functools import cache


@cache
def F(n):
    if n == 0:
        return 1
    return n - M(F(n - 1))


@cache
def M(n):
    if n == 0:
        return 0
    return n - F(M(n - 1))


def hofstadter_f_m(n):
    return F(n), M(n)


while True:
    try:
        n = int(input())
    except ValueError:
        print("Повторите ввод.")
    else:
        endstr = ", "
        for i in range(n + 1):
            if i == n:
                endstr = ""
            print(hofstadter_f_m(i), end=endstr)
        break