def reducer(m: int, n: int) -> tuple:
    k = n
    while k != 1:
        if m % k == 0 and n % k == 0:
            return m // k, n // k
        else:
            k -= 1
    return m, n


while True:
    try:
        m, n = int(input()), int(input())
    except ValueError:
        print("Повторите ввод.")
    else:
        if m > n or m <= 0 or n <= 0:
            print("Повторите ввод.")
        else:
            print(reducer(m, n))
            break