#from numpy import arange, average, diff, zeros
import numpy as np
from math import exp
import pandas as pd
import matplotlib.pyplot as plt

R1 = 10
R2 = 5000
i_0 = 1.2e-10
phi_t = 0.025
epsilon = 0.1
max_iteration = 4
C = 4e-12
time_sim = 100
td, tr, pw, tf = 10, 5, R2*C*(1e+9), 5
h = (1e-8)

def f_1(e, phi1_n, phi1_np1, phi2_n, phi2_np1):
    return ((e - phi1_np1)/R1 - i_0*(exp(phi1_np1/phi_t) - 1) - (C/h * ((phi1_np1 - phi1_n) - (phi2_np1 - phi2_n))))

def f_2(e, phi1_n, phi1_np1, phi2_n, phi2_np1):
    return ((C/h * ((phi1_np1 - phi1_n) - (phi2_np1 - phi2_n))) - ((phi2_n) / R2))

E_end = 5
E_start = 0
t = [i for i in np.arange(0, time_sim, 0.5)]
table = []


def jacobi_stuff(y11, y12, y21, y22, f1, f2):
    max_iter = 1000
    tol = 1e-6
    x1, x2 = 0.0, 0.0
    x1s, x2s = [x1], [x2]
    for k in range(max_iter):
        x1_new = (-f1 - y12 * x2) / y11
        x2_new = (-f2 - y21 * x1) / y22
        x1s.append(x1_new)
        x2s.append(x2_new)
        if np.abs(x1s[-1] - x1s[-2]) < tol and np.abs(x2s[-1] - x2s[-2]) < tol:
            return x1_new, x2_new, k + 1
        x1, x2 = x1_new, x2_new
    return x1, x2, max_iter

def E_t(t, td, tr, pw, tf): # тут генерится массив напряжения
    E_max = 5
    E = []
    td_point = td
    tr_point = td + tr
    pw_point = td + tr + pw
    tf_point = td + tr + pw + tf
    for t_i in t:
        if t_i <= td_point:
            E.append(0)
        elif td_point < t_i <= tr_point:
            E.append((-td_point + t_i)*(E_max)/tr)
        elif tr_point < t_i <= pw_point:
            E.append(E_max)
        elif pw_point < t_i <= tf_point:
            E.append((tf_point - t_i)*(E_max)/tf)
        elif t_i > tf_point:
            E.append(0)
    return E

E = E_t(t, td, tr, pw, tf)
phi1, phi2 = [], []
#phi1_final, phi2_final = [], []

y12 = C / h
y21 = C / h
y22 = -C / h - 1 / R2

phi1, phi2 = [0], [0]

for i in range(len(t)):
    iteration = 1
    jacobi_iterations = 0
    p1, p2 = phi1[-1], phi2[-1]
    f1 = f_1(E[i], phi1[-1], p1, phi2[-1], p2)
    f2 = f_2(E[i], phi1[-1], p1, phi2[-1], p2)
    y11 = -1 / R1 - (i_0 / phi_t * exp(p1 / phi_t)) - C / h
    y11_const, f1_const, f2_const = y11, f1, f2
    x1, x2, iters = jacobi_stuff(y11, y12, y21, y22, f1, f2)
    discrep1, discrep2 = 1, 1
    while (discrep1 >= epsilon and discrep2 >= epsilon):
        if iteration <= max_iteration:
            f1 = f_1(E[i], phi1[-1], p1, phi2[-1], p2)
            f2 = f_2(E[i], phi1[-1], p1, phi2[-1], p2)
            y11 = -1 / R1 - (i_0 / phi_t * exp(p1 / phi_t)) - C / h
        x1, x2, iters = jacobi_stuff(y11, y12, y21, y22, f1, f2)
        jacobi_iterations += iters
        iteration += 1
        #iteration += (iters)
        phi1_i = p1
        phi2_i = p2
        p1 += x1
        p2 += x2
        discrep1, discrep2 = abs(p1 - phi1_i), abs(p2 - phi2_i)
    table.append([t[i], E[i], p1, p2, iteration, jacobi_iterations])
    phi1.append(p1)
    phi2.append(p2)
phi1.pop(0)
phi2.pop(0)

df = pd.DataFrame(table, columns = ['t, ns', 'E, V', 'phi1, V', 'phi2, V', "Newton iterations", "Jacobi iterations"])
table_printed = df.to_string(index=False)
print(table_printed)

phi2_scaled = [i for i in phi2]
plt.title("")
plt.xlabel("t, ns")
plt.ylabel("E, V")
plt.grid(True)
plt.plot(t, E,  label='E')
plt.plot(t, phi1,  label='phi1')
plt.plot(t, phi2_scaled, label='phi2')
plt.legend()
plt.show()