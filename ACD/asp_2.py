from numpy import exp, arange
#import pandas as pd

E = 5
R = 3
i_0 = 1.2*(10**(-10))
phi_t = 0.025
epsilon = 0.001

def f(e, phi): # стартовая функция
    return ((e - phi) / R) - (i_0 * (exp(phi / phi_t) - 1))

def f_prime(phi): # производная
    return ((-1 / R) - ((i_0 / phi_t) * exp(phi / phi_t)))

def d(e, phi): # отношение стартовой функции и её производной
    return -(f(e, phi) / f_prime(phi))

def newton(c=0.1, phi_zero=0.0): # метод Ньютона
    phis, i, ds = [phi_zero], 0, [0]
    while (abs(d(E, phis[-1])) > epsilon):
        phis.append(float(phis[-1] + d(E, phis[-1])))
        ds.append(float(d(E, phis[-1])))
        i+=1
    return phis, i, ds

def newton_boosted(c=0.1, phi_zero=0.0): # ускоренный метод
    E_i = 0
    sum = []
    phi_array, ds = [phi_zero], [0]
    phis_end = [phi_zero]
    while E_i <= E:
        i = 0
        E_i += 1
        while abs( d(E_i, phi_array[-1]) ) > epsilon:
            phi_array.append(float(phi_array[-1] + d(E_i, phi_array[-1])))
            ds.append(float(d(E_i, phi_array[-1])))
            i += 1
        phis_end.append(phi_array[-1])
        sum.append(i)
    return phis_end, sum, ds

def newton_raphson_alpha_constant(c=0.1, phi_zero=0.0): # метод Ньютона-Рафсона с постоянной альфой
    alpha = 0.1
    phi_array, d_array = [], []
    phi_array.append(phi_zero)
    d_array.append(0)
    i = 0
    while abs(d(E, phi_array[-1])) > epsilon:
        phi_array.append(float(  phi_array[-1] + (alpha * d(E, phi_array[-1]))  ))
        d_array.append(float(d(E, phi_array[-1])))
        i+=1
    return phi_array, i,  d_array

def newton_raphson_alpha_changeable(c=0.1, phi_zero=0.0): # с изменяющейся альфой
    phi_array, d_array = [], []
    phi_array.append(phi_zero)
    d_array.append(0)
    i = 0
    while abs(d(E, phi_array[-1])) > epsilon:
        alpha = 1 if abs(d(E, phi_array[-1])) < c else c/d(E, phi_array[-1])
        phi_array.append(float(  phi_array[-1] + alpha * d(E, phi_array[-1])  ))
        d_array.append(float(d(E, phi_array[-1])))
        i+=1
    return phi_array, i,  d_array

with open("data_asp_2.txt", "w") as file:
    c_i = 0.25
    for phi_i in [0.0, 0.6, 0.7]:
        file.write(f"phi = {phi_i} V\n")
        phi_newton, i_n, d_n = newton(c=c_i, phi_zero=phi_i)
        phi_nb, i_nb, d_nb = newton_boosted(c=c_i, phi_zero=phi_i)
        phi_aconst, i_aco, d_aco = newton_raphson_alpha_constant(c=c_i, phi_zero=phi_i)
        phi_achange, i_ach, d_ach = newton_raphson_alpha_changeable(c=c_i, phi_zero=phi_i)
        file.write(f'Newton:\t\t\t\t\t\t\t\t{phi_newton[-1]} ({i_n} iterations)\n'
                   f'Newton boosted:\t\t\t\t\t\t{(phi_nb[-1])} ({sum(i_nb)} iterations)\n'
                   f'Newton-Raphson (constant alpha):\t{phi_aconst[-1]} ({i_aco} iterations)\n'
                   f'Newton-Raphson (changeable alpha):\t{phi_achange[-1]} ({i_ach} iterations)\n')
        file.write("\n")
    file.close()

c_i = 0.1
phi_i = 0.0
phi_newton, i_n, d_n = newton(c=c_i, phi_zero=phi_i)
phi_nb, i_nb, d_nb = newton_boosted(c=c_i, phi_zero=phi_i)
phi_aconst, i_aco, d_aco = newton_raphson_alpha_constant(c=c_i, phi_zero=phi_i)
phi_achange, i_ach, d_ach = newton_raphson_alpha_changeable(c=c_i, phi_zero=phi_i)
print(f"Newton, phi={phi_i}")
for i in range(i_n):
    print(f'{phi_newton[i]}\t{i+1}\t{d_n[i]}')
print(f"Newton boosted, phi={phi_i}")
for i in range(len(i_nb)):
    print(f'{phi_nb[i]}\t{i_nb[i]}\t{d_nb[i]}')
print(f"Newton-Raphson (constant alpha), phi={phi_i}")
for i in range(i_aco):
    print(f"{phi_aconst[i]}\t{i+1}\t{d_aco[i]}")
print(f"Newton-Raphson (changeable alpha), phi={phi_i}")
for i in range(i_ach):
    print(f"{phi_achange[i]}\t{i+1}\t{d_ach[i]}")