from API.functions import makespan, ct

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

    T = [Tn[pi[i] - 1] for i in I]
    P = [Pn[pi[i] - 1] for i in I]

    pi_ins = pi.copy()

    Tss = [T for i in I]
    U_ss = [U_s for i in I]
    Ps = [P for i in I]

    for i in pi:
        pis = ct(pi_ins, i)
        Cmax = list(map(makespan, pis, Tss, U_ss, Ps))

        Cmax_pi = makespan(pi_ins, T, U_s, P)
        i_min = np.argmin(Cmax)        

        if (Cmax[i_min] < Cmax_pi):
            k = pi_ins.index(i)
            pi_ins[i_min], pi_ins[k] = pi_ins[k], pi_ins[i_min]

    return pi_ins

def swap()
    return 11

def local_search(pi_input):
    """
    pi_input es una secuencia de trabajos
    """


    # Paso 1

    pi_modif = pi_input
    l_max = 2
    l = 1


    # Paso 2

    while (l <= l_max):
        if (l == 1):
            pi_temp = insertion(pi_modif)

    return 1888