from functools import reduce

def intersection(*A):
    return list(reduce(set.intersection, [set(x) for x in A]))


n = int(input())
l = []
j = 0
while j != n:
    a = input().split()
    for i in range(len(a)):
        a[i] = int(a[i])
    l.append(a)
    j += 1

print(intersection(*l))
