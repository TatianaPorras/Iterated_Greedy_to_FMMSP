from API.functions import c_range, makespan, PT

def DNEH_SMR(T, U_s, P):
    """
    T es la lista de números triangulares difusos del tiempo de producción del trabajo i en la unidad o máquina u. El prefijo 't' es por triangular difuso.

    U_s es el conjunto de máquinas o unidades de la etapa s.

    P es la ponderación de los números triangulares.

    Esta función aplica el algoritmo DNEH_SMR.
    """

    import math
    import numpy as np

    # L es la cantidad total de etapas del sistema de producción.
    L = len(U_s)

    # I es el conjunto de trabajos.
    I = range(len(T))

    # sec es la secuencia natural de trabajos: 1, 2, 3, ...
    sec = range(1, len(T) + 1)

    # S es el conjunto de etapas.
    S = range(L)

    # n_s es la cantidad de unidades o máquinas de la etapa s.
    n_s = [len(U_s[s]) for s in S]


    # Paso 1

    k = math.floor(L/2)


    # Paso 2

    # Ta es la lista de los tiempos de producción promedio del trabajo i en la etapa s.
    Ta = [1/n_s[s]*np.sum([[T[i][u] for i in I] for u in U_s[s]], axis = 0) for s in S]

    # reordenar Ta
    Ta = [[Ta[s][i] for s in S] for i in I]


    # Paso 3

    # T1 es la lista de los tiempos promedio de la primera mitad de etapas.
    T1 = [1/k*np.sum([Ta[i][l] for l in c_range(1, k)], axis = 0) for i in I]

    # T2 es la lista de los tiempos promedio de la segunda mitad de etapas.
    T2 = [1/(L - k)*np.sum([Ta[i][l] for l in c_range(k + 1, L)], axis = 0) for i in I]


    # Paso 4

    # P2 es la lista de tiempos ponderados de la segunda mitad de etapas.
    P2 = [(T2[i][0] + 2*T2[i][1] + T2[i][2])/4 for i in range(len(T2))]

    # dP2 es P2 en forma de diccionario, donde la llave del diccionario son los trabajos en orden natural (1, 2, 3, ...)
    dP2 = dict(zip(sec, P2))

    # dP2_ord es dP2 en orden ascendente de P2
    dP2_ord = dict(sorted(dP2.items(), key = lambda arg1: arg1[1]))

    # Pi_re1 es la secuencia de trabajos en orden ascendente de P2
    Pi_re1 = list(dP2_ord.keys())


    # Paso 5

    Pi_re2 = []
    for j in I:
        if j % 2 == 0:
            Pi_re2.append(Pi_re1[0])
            Pi_re1.remove(Pi_re1[0])
        else:
            Pi_re2.append(Pi_re1[math.ceil(len(Pi_re1)/2) - 1])
            Pi_re1.remove(Pi_re1[math.ceil(len(Pi_re1)/2) - 1])


    # Paso 6

    Pi_re3 = Pi_re2.copy()


    # Paso 7

    Cmax = makespan(Pi_re3, T, U_s, P)

    return Cmax