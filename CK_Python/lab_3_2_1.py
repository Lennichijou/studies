def reducer(m, n):
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
        if m > n:
            print("Ошибка: M > N!")
        else:
            print(reducer(m, n))
            break