from API.functions import makespan, ct, st, PT

import numpy as np

def insertion(pi, Tn, U_s, Pn):
    """
    pi es una secuencia de trabajos

    Tn son los tiempos de producción en orden de secuencia natural, 1, 2 ,3, ...

    U_s es el conjunto de máquinas o unidades de la etapa s.

    Pn es la ponderación de los números triangulares en orden de secuencia natural, 1, 2, 3, ...

    Esta función reinserta cada trabajo para obtener la posición con el mínimo makespan
    """

    I = range(len(pi))

    pi_ins = pi.copy()

    Tss = [Tn for i in I]
    U_ss = [U_s for i in I]
    Ps = [Pn for i in I]

    for i in pi:
        pis = ct(pi_ins, i)
        Cmax = list(map(makespan, pis, Tss, U_ss, Ps))

        Cmax_pi = makespan(pi_ins, Tn, U_s, Pn)

        P_Cmax = PT(Cmax)
        i_min = np.argmin(P_Cmax)

        if (PT(Cmax[i_min]) < PT(Cmax_pi)):
            k = pi_ins.index(i)
            pi_ins[i_min], pi_ins[k] = pi_ins[k], pi_ins[i_min]

    return pi_ins

def swap(pi, Tn, U_s, Pn):
    """
    pi es una secuencia de trabajos

    Tn son los tiempos de producción en orden de secuencia natural, 1, 2 ,3, ...

    U_s es el conjunto de máquinas o unidades de la etapa s.

    Pn es la ponderación de los números triangulares en orden de secuencia natural, 1, 2, 3, ...

    Esta función intercambia pares de trabajos para obtener las posiciones con el mínimo makespan
    """

    I = range(len(pi))

    pi_sw = pi.copy()

    Tss = [Tn for i in I]
    U_ss = [U_s for i in I]
    Ps = [Pn for i in I]

    for i in pi:
        pis = st(pi_sw, i)
        Cmax = list(map(makespan, pis, Tss, U_ss, Ps))

        Cmax_pi = makespan(pi_sw, Tn, U_s, Pn)

        P_Cmax = PT(Cmax)
        i_min = np.argmin(P_Cmax)

        if (PT(Cmax[i_min]) < PT(Cmax_pi)):
            k = pi_sw.index(i)
            pi_sw[i_min], pi_sw[k] = pi_sw[k], pi_sw[i_min]

    return pi_sw

def local_search(pi_input, Tn, U_s, Pn):
    """
    pi_input es una secuencia de trabajos

    Tn son los tiempos de producción en orden de secuencia natural, 1, 2 ,3, ...

    U_s es el conjunto de máquinas o unidades de la etapa s.

    Pn es la ponderación de los números triangulares en orden de secuencia natural, 1, 2, 3, ...

    Esta función aplica el algoritmo local_search
    """


    # Paso 1

    pi_modif = pi_input.copy()
    l_max = 2
    l = 1


    # Paso 2

    while (l <= l_max):


    # Paso 3

        if (l == 1):


    # Paso 4

            pi_temp = insertion(pi_modif, Tn, U_s, Pn)


    # Paso 5

        elif (l == 2):


    # Paso 6

            pi_temp = swap(pi_modif, Tn, U_s, Pn)


    # Paso 7

        if (PT(makespan(pi_temp, Tn, U_s, Pn)) < PT(makespan(pi_modif, Tn, U_s, Pn))):


    # Paso 8

            pi_modif = pi_temp
            l = 1


    # Paso 9

        else:


    # Paso 10

            l = l + 1


    # Paso 11

    pi_multivec = pi_modif

    return pi_multivec