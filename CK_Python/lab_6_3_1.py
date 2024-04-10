import concurrent.futures as cf
import time


N = 5000
matrix1 = [[0 for _ in range(N)] for _ in range(N)]
matrix2 = [[0 for _ in range(N)] for _ in range(N)]


def func(t):
    return t[0], t[1], 1 / (1 + abs(t[0] - t[1]))


def without_concurrent():
    time_start = time.time()
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            matrix1[i - 1][j - 1] = func((i, j))[2]
    return time.time() - time_start


def with_concurrent():
    time_start = time.time()
    with cf.ProcessPoolExecutor(max_workers=None) as executor:
        for i, j, result in executor.map(func, (range(1, N+1), range(1, N+1))):
            matrix2[i-1][j-1] = result
    return time.time() - time_start


if __name__ == '__main__':
    print(without_concurrent())
    print(with_concurrent())
