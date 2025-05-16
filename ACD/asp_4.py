from numpy import exp, arange
import pandas as pd

E = 5
R = 3
i_0 = 1.2*(10**(-10))
phi_t = 0.025
epsilon = 0.001

def f(phi): # стартовая функция
    return abs((E - phi) / R - (i_0 * (exp(phi / phi_t) - 1)))

def dichotomy():
    table = []
    a, b = 0, 5
    iteration = 1
    while (b-a) >= epsilon:
        interval = [a + (b - a) * i / 4 for i in arange(5)]
        phis = [f(i) for i in interval]
        min_index = phis.index(min(phis))
        table.append([iteration, a, interval[1], interval[2], interval[3], b, f(a), f(interval[1]), f(interval[2]), f(interval[3]), f(b)])
        if min_index == 0:
            a, b = interval[0], interval[1]
        elif min_index == 4:
            a, b = interval[3], interval[4]
        else:
            a, b = interval[min_index - 1], interval[min_index + 1]
        iteration+=1
    return table


def golden_ratio():
    table = []
    a, b = 0, 5
    iteration = 1
    gamma = (1+(5**(0.5)))/2
    while (b-a) >= epsilon:
        x1 = b - (b-a)/gamma
        x2 = a + (b-a)/gamma
        f_1, f_2 = float(f(x1)), float(f(x2))
        table.append([iteration, a, x1, x2, b, float(f(a)), f_1, f_2, float(f(b))])
        if f_1 < f_2:
            b, x2, f_2 = x2, x1, f_1
        else:
            a, x1, f_1 = x1, x2, f_2
        iteration+=1
    return table

def double_step():
    a, b = 0, 5
    table = []
    x0, h0 = a, epsilon
    x, h = b, h0
    direction = 1
    iteration = 1
    f1, f2 = f(x0), f(x)
    while True:
        x = x0 + direction * h
        f1, f2 = f(x0), f(x)
        table.append([iteration, h, x0, x, f1, f2])
        iteration += 1
        if abs(x - x0) < epsilon:
            break
        if f2<f1:
            x0 = x
            f1 = f2
            h *= 2
        else:
            direction *= -1
            h /= 2
    return table


print('Golden Ratio method')
g_r = golden_ratio()
df = pd.DataFrame(g_r, columns = ['iteration', 'a', 'x1', 'x2', 'b', 'f(a)', 'f(x1)', 'f(x2)', 'f(b)'])
table_printed = df.to_string(index=False)
print(table_printed)

print('Dichotomy method')
dch = dichotomy()
df = pd.DataFrame(dch, columns = ['iteration', 'a', 'x1', 'x2', 'x3', 'b', 'f(a)', 'f(x1)', 'f(x2)', 'f(x3)','f(b)'])
table_printed = df.to_string(index=False)
print(table_printed)

print('Step doubling method')
ds = double_step()
df = pd.DataFrame(ds, columns = ['iteration', 'h', 'x0', 'x', 'f1', 'f2'])
table_printed = df.to_string(index=False)
print(table_printed)