from API.functions import makespan, ct

import numpy as np

def destruction_reconstruction(pi_input, d, T, U_s, P):
    """
    pi_input es la secuencia a la que se le aplica este algoritmo

    d es el número de trabajos que son removidos aleatoriamente de pi

    Esta función aplica el algoritmo destruction_reconstruction
    """

    import random


    # Paso 1

    pi_r = pi_input.copy()

    pi_d = []
    for i in range(d):
        t = random.choice(pi_r)
        pi_d.append(t)
        pi_r.remove(t)


    # Paso 2

    Tss = [T for j in pi_d]
    U_ss = [U_s for j in pi_d]
    Ps = [P for j in pi_d]
    ex = []
    pi_r2 = pi_r.copy()
    for j in pi_d:


    # Paso 3

        pi_r.append(j)
        pi_rs = ct(pi_r, j)

        fitness1s = list(map(makespan, pi_rs, Tss, U_ss, Ps))
        fitness1 = min(fitness1s)


    # Paso 4

        j_min = np.argmin(fitness1s)
        k = pi_r.index(j)

        pi_r[j_min], pi_r[k] = pi_r[k], pi_r[j_min]


    # Paso 5

        for j2 in pi_r2:


    # Paso 6

            pi_rs2 = ct(pi_r, j2)
            fitness2s = list(map(makespan, pi_rs2, Tss, U_ss, Ps))
            fitness2 = min(fitness2s)


    # Paso 7

            if (fitness2 < fitness1):


    # Paso 8

                j2_min = np.argmin(fitness2s)
                k2 = pi_r.index(j2)

                pi_r[j2_min], pi_r[k2] = pi_r[k2], pi_r[j2_min]


    # Paso 9

        pi_desrec = pi_r


    # Paso 10

    return pi_desrec