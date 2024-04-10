from functools import reduce


def intersection(*sets: tuple) -> list:
    return list(reduce(set.intersection, [set(x) for x in sets]))


n = int(input())
l = []
j = 0
while j != n:
    try:
        a = input().split()
        for i in range(len(a)):
            a[i] = int(a[i])
    except ValueError:
        print("Повторите ввод.")
    else:
        l.append(a)
        j += 1

print(intersection(*l))
