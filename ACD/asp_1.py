import matplotlib.pyplot as plt
import math as m
import pandas as pd
import numpy as np

k = [i for i in range(11)]
U_c = 5
#print(*U)

R = 1
C = 3
h = int(input("h = "))

#def euler_exp(i):

def euler_explicit(): # явный метод Эйлера
    ee_array = list(np.zeros(len(k)))
    ee_array[0] = U_c
    for i in range(1, len(k)):
        ee_array[i] = ee_array[i-1] * (1 - h/(R*C))
    return ee_array

def euler_implicit(): # неявный метод Эйлера
    ei_array = list(np.zeros(len(k)))
    ei_array[0] = U_c
    for i in range(1, len(k)):
        ei_array[i] = ei_array[i-1] / (1 + h/(R*C))
    return ei_array

def precise(): # точный метод
    p_array = list(np.zeros(len(k)))
    p_array[0] = U_c
    for i in range(1, len(k)):
        t = i*h
        p_array[i] = U_c * m.exp(-t/(R*C))
    return p_array

def trapezoid(): # метод трапеций
    tr_array = list(np.zeros(len(k)))
    tr_array[0] = U_c
    for i in range(1, len(k)):
        tr_array[i] = (euler_explicit()[i] + euler_implicit()[i])/2
    return tr_array

array1 = euler_explicit()
array2 = euler_implicit()
array3 = precise()
array4 = trapezoid()

# вывод таблицы
table = []
for i in range(len(k)):
    table.append([k[i]*h, array1[i], array2[i], array3[i], array4[i]])
df = pd.DataFrame(table, columns = [' t, ns ', ' EEM, V ', 'EIM, V', ' Precise, V ', " Trapezoid, V "])
table_printed = df.to_string(index=False)
with open("data.txt", "w") as file:
    file.write(table_printed)
    file.close()

# вывод графиков
k_multiplied = [k[i]*h for i in range(len(k))]
plt.title("")
plt.xlabel("t, ns")
plt.ylabel("phi, V")
plt.grid(True)
plt.plot(k_multiplied, array1, label="Euler explicit method")
plt.plot(k_multiplied, array2, label="Euler implicit method")
plt.plot(k_multiplied, array3, label="Precise method")
plt.plot(k_multiplied, array4, label="Trapezoid method")
plt.legend()
plt.show()
