from algorithms import DNEH_SMR, destruction_reconstruction, local_search
from API.functions import PT, c_range

import numpy as np
import random
import math

# Datos de la instancia de prueba
# Tn = [   
#     [(10,12,13), (7,8,10), (10,11,12), (8,9,10), (6,7,8), (4,5,6), (11,13,15), (10,11,12), (5,6,8), (15,17,20)], 
#     [(11,12,14), (8,9,10), (9,10,12), (6,7,8), (8,9,10), (2,3,4), (1,2,3), (18,19,23), (4,5,6), (12,14,15)],
#     [(9,10,12), (5,6,8), (2,3,4), (7,8,9), (4,5,6), (15,16,19), (11,13,14), (5,6,7), (14,15,16), (16,17,20)],
#     [(6,7,9), (4,5,6), (5,6,8), (4,5,6), (6,7,8), (13,14,15), (10,11,13), (6,7,9), (19,21,25), (17,18,21)],
#     [(8,9,10), (4,5,6), (5,6,7), (5,6,8), (6,7,9), (15,16,20), (9,10,12), (7,8,10), (10,12,13), (18,19,21)]
# ]

Tn = [
    [(10, 12, 13), (11, 12, 14), (9, 10, 12), (6, 7, 9), (8, 9, 10)],
    [(7, 8, 10), (8, 9, 10), (5, 6, 8), (4, 5, 6), (4, 5, 6)],
    [(10, 11, 12), (9, 10, 12), (2, 3, 4), (5, 6, 8), (5, 6, 7)],
    [(8, 9, 10), (6, 7, 8), (7, 8, 9), (4, 5, 6), (5, 6, 8)],
    [(6, 7, 8), (8, 9, 10), (4, 5, 6), (6, 7, 8), (6, 7, 9)],
    [(4, 5, 6), (2, 3, 4), (15, 16, 19), (13, 14, 15), (15, 16, 20)],
    [(11, 13, 15), (1, 2, 3), (11, 13, 14), (10, 11, 13), (9, 10, 12)],
    [(10, 11, 12), (18, 19, 23), (5, 6, 7), (6, 7, 9), (7, 8, 10)],
    [(5, 6, 8), (4, 5, 6), (14, 15, 16), (19, 21, 25), (10, 12, 13)],
    [(15, 17, 20), (12, 14, 15), (16, 17, 20), (17, 18, 21), (18, 19, 21)]
]

# Tn tiene la estructura [ máquina1, máquina2, máquinaM ], a su vez cada máquina tiene la forma [trabajo1, trabajo2, trabajoN], y cada trabajo tiene la forma (tiempo_pesimista, tiempo_promedio, tiempo_optimista).

# U_s es el conjunto de máquinas o unidades de la etapa s.
U_s = [[0, 1], [2, 3, 4]]

# L es el total de etapas
L = len(U_s)

# Pn es la ponderación de los números triangulares.
Pn = PT(T_i_u)

# T_0 es un parametro para crear variación en el algoritmo, diferente de cero 
T_0 = 1.1

# Paso 1

pi_re3, Ta = DNEH_SMR(Tn, U_s, Pn)


# Paso 2

pi_result = pi_re3.copy()
pi_temp = pi_re3.copy()
iter1 = 1


# Paso 3

UT = np.sum([len(U_s[s]) for s in c_range(1, L)])
TT = T_0*(np.sum(Ta))/(10 * N * L)

while (iter1 <= N**2 * L * UT):


# Paso 4

    pi_temp = local_search(pi_temp)


# Paso 5

    if (makespan(pi_temp, Tn, U_s, Pn) < makespan(pi_re3, Tn, U_s, Pn)):


# Paso 6

        pi_re3 = pi_temp.copy()


# Paso 7

        if (makespan(pi_temp, Tn, U_s, Pn) < makespan(pi_result, Tn, U_s, Pn)):


# Paso 8

            pi_result = pi_temp.copy()


# Paso 9

    else:


# Paso 10

        if ( random.random() < math.exp(-(makespan(pi_temp, Tn, U_s, Pn) - makespan(pi_re3, Tn, U_s, Pn))/TT) ):


# Paso 11

            pi_re3 = pi_temp.copy()
    

# Paso 12

    pi_temp = destruction_reconstruction(pi_temp, d, Tn, U_s, Pn)


# Paso 13

print(pi_result)