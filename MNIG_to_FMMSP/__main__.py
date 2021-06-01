from algorithms import DNEH_SMR, destruction_reconstruction, local_search
from API.functions import PT, c_range, makespan

import numpy as np
import random
import math

# Soluciones probadas:
# Makespan: (36, 44, 52)
# Secuencias:
# [7, 8, 6, 10, 1, 9, 5, 4, 2, 3]
# [7, 8, 6, 10, 5, 9, 1, 4, 2, 3]
# [6, 1, 9, 7, 8, 10, 4, 5, 2, 3]
# [1, 6, 9, 10, 7, 8, 5, 4, 2, 3]
# [6, 5, 10, 1, 9, 7, 8, 4, 2, 3]
# [6, 10, 1, 8, 9, 4, 5, 7, 2, 3]
# [6, 5, 7, 10, 8, 1, 4, 9, 2, 3]
# [9, 7, 1, 6, 8, 10, 4, 5, 2, 3]
# [5, 8, 7, 6, 10, 4, 1, 9, 2, 3]
# [7, 1, 6, 10, 5, 9, 8, 4, 2, 3]

# Datos de la instancia de prueba
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
# Tn tiene la estructura [ trabajo1, trabajo2, trabajoN ], a su vez cada trabajo tiene la forma [ máquina1, máquina2, máquinaM ], y cada máquina tiene la forma (tiempo_pesimista, tiempo_promedio, tiempo_optimista).

# U_s es el conjunto de máquinas o unidades de la etapa s.
U_s = [[0, 1], [2, 3, 4]]

# L es el total de etapas
L = len(U_s)

# Pn es la ponderación de los números triangulares.
Pn = PT(Tn)

# Parametros para las iteraciones, introducidos como argumentos a este programa

import argparse
parser1 = argparse.ArgumentParser()

parser1.add_argument("N", type = int)
parser1.add_argument("T_0", type = float)
parser1.add_argument("d", type = int)
parser1.add_argument("--debug", action = "store_true")

args1 = parser1.parse_args()

N = args1.N
T_0 = args1.T_0
d = args1.d
debug = args1.debug

# N es un parámetro para el número de iteraciones
# N = 5

# T_0 es un parámetro para crear variación en el algoritmo, diferente de cero 
# T_0 = 1.1

# d es un parámetro para la cantidad de trabajos a colocar en pi_d para el algoritmo destruction_reconstruction
# d = 4


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
    iter1 += 1


# Paso 4

    pi_temp = local_search(pi_temp, Tn, U_s, Pn)


# Paso 5

    if (PT(makespan(pi_temp, Tn, U_s, Pn)) < PT(makespan(pi_re3, Tn, U_s, Pn))):


# Paso 6

        pi_re3 = pi_temp.copy()


# Paso 7

        if (PT(makespan(pi_temp, Tn, U_s, Pn)) < PT(makespan(pi_result, Tn, U_s, Pn))):


# Paso 8

            pi_result = pi_temp.copy()


# Paso 9

    else:


# Paso 10

        if ( random.random() < math.exp(-(PT(makespan(pi_temp, Tn, U_s, Pn)) - PT(makespan(pi_re3, Tn, U_s, Pn)))/TT) ):


# Paso 11

            pi_re3 = pi_temp.copy()


# Paso 12

    pi_temp = destruction_reconstruction(pi_temp, d, Tn, U_s, Pn)

    if (debug == True):
        mk = makespan(pi_re3, Tn, U_s, Pn)
        iter1O = "%4d" % (iter1 - 1)
        print("Iter:", iter1O, "   Secuencia:", pi_re3, "   Makespan:", mk, "   P:", PT(mk))


# Paso 13

print("\n", pi_result, makespan(pi_result, Tn, U_s, Pn, debug))