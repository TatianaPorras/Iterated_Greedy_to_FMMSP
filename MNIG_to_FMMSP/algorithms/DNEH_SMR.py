from API.functions import c_range, makespan, PT, ct

def DNEH_SMR(Tn, U_s, Pn):
    """
    Tn es la lista de números triangulares difusos del tiempo de producción del trabajo i en la unidad o máquina u, en secuencia de números naturales, 1, 2, 3, ... El prefijo 't' es por triangular difuso.

    U_s es el conjunto de máquinas o unidades de la etapa s.

    Pn es la ponderación de los números triangulares en secuencia de números naturales, 1, 2, 3, ...

    Esta función aplica el algoritmo DNEH_SMR.
    """

    import math
    import numpy as np

    # L es la cantidad total de etapas del sistema de producción.
    L = len(U_s)

    # I es el conjunto de trabajos.
    I = range(len(Tn))

    # sec es la secuencia natural de trabajos: 1, 2, 3, ...
    sec = range(1, len(Tn) + 1)

    # S es el conjunto de etapas.
    S = range(L)

    # n_s es la cantidad de unidades o máquinas de la etapa s.
    n_s = [len(U_s[s]) for s in S]


    # Paso 1

    k = math.floor(L/2)


    # Paso 2

    # Ta es la lista de los tiempos de producción promedio del trabajo i en la etapa s.
    Ta = [1/n_s[s]*np.sum([[Tn[i][u] for i in I] for u in U_s[s]], axis = 0) for s in S]

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

    # pi_re1 es la secuencia de trabajos en orden ascendente de P2
    pi_re1 = list(dP2_ord.keys())


    # Paso 5

    pi_re2 = []
    for j in I:
        if j % 2 == 0:
            pi_re2.append(pi_re1[0])
            pi_re1.remove(pi_re1[0])
        else:
            pi_re2.append(pi_re1[math.ceil(len(pi_re1)/2) - 1])
            pi_re1.remove(pi_re1[math.ceil(len(pi_re1)/2) - 1])


    # Paso 6

    pi_re3 = pi_re2.copy()


    # Paso 7

    Tss = [Tn for j in pi_re3]
    U_ss = [U_s for j in pi_re3]
    Ps = [Pn for j in pi_re3]
    ex = []
    for j in pi_re2:
        pi_re3s = ct(pi_re3, j, ex)
        Cmax = list(map(makespan, pi_re3s, Tss, U_ss, Ps))

        P_Cmax = PT(Cmax)
        j_min = np.argmin(P_Cmax)
        k = pi_re3.index(j)

        pi_re3[j_min], pi_re3[k] = pi_re3[k], pi_re3[j_min]
        ex.append(j_min)

    return pi_re3, Ta