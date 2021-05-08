def DNEH_SMR(tT, U_s):
    """
    tT es la lista de números triangulares difusos del tiempo de producción del trabajo i en la unidad o máquina u. El prefijo 't' es por triangular difuso.

    U_s es el conjunto de máquinas o unidades de la etapa s.

    Esta función aplica el algoritmo DNEH_SMR.
    """

    import math
    import numpy as np

    # L es la cantidad total de etapas del sistema de producción.
    L = len(U_s)

    # I es el conjunto de trabajos.
    I = range(len(tT))

    # S es el conjunto de etapas.
    S = range(L)

    # n_s es la cantidad de unidades o máquinas de la etapa s.
    n_s = [len(U_s[s]) for s in S]


    # Paso 1

    k = math.floor(L/2)


    # Paso 2

    # tTa es la lista de los tiempos de producción promedio del trabajo i en la etapa s.
    tTa = [1/n_s[s]*np.sum([[tT[i][u] for i in I] for u in U_s[s]], axis = 0) for s in S]

    # reordenar tTa
    tTa = [[tTa[s][i] for s in S] for i in I]


    # Paso 3

    # tT1 es la lista de los tiempos promedio de la primera mitad de etapas.
    tT1 = [1/k*np.sum([tTa[i][l] for l in c_range(1, k)], axis = 0) for i in I]

    # tT2 es la lista de los tiempos promedio de la segunda mitad de etapas.
    tT2 = [1/(L - k)*np.sum([tTa[i][l] for l in c_range(k + 1, L)], axis = 0) for i in I]


    # Paso 4

    

    return tT1

def c_range(llim, ulim):
    """
    c_range es por correct range, llim es por lower limit, ulim es por upper limit.

    Esta functión toma un range que empieza en llim y devuelve un range que empieza en llim - 1.
    """

    return range(llim - 1, ulim)