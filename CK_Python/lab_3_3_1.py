def F(n: int) -> int:
    if n == 0:
        return 1
    return n - M(F(n - 1))


def M(n: int) -> int:
    if n == 0:
        return 0
    return n - F(M(n - 1))


def hofstadter_f_m(n: int) -> tuple:
    return F(n), M(n)


while True:
    try:
        n = int(input())
    except ValueError:
        print("Повторите ввод.")
    else:
        endstr = ", "
        for i in range(n):
            if i == n-1:
                endstr = ""
            print(hofstadter_f_m(i), end=endstr)
        break
