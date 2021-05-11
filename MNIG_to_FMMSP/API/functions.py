import numpy as np

def c_range(llim, ulim):
    """
    c_range es por correct range, llim es por lower limit, ulim es por upper limit.

    Esta functión toma un range que empieza en llim y devuelve un range que empieza en llim - 1.
    """

    return range(llim - 1, ulim)

def PT(T):
    """
    P es por ponderación.

    PT es por Ponderación de Todos los trabajos en todas las máquinas.

    Esta función devuelve la ponderación de las tres partes de un número triangular difuso
    """

    P = [[(T[i][u][0] + 2*T[i][u][1] + T[i][u][2])/4 for u in range(len(T[0]))] for i in range(len(T))]

    return P

def makespan(pi, T, U_s, P):
    """
    pi es una secuencia de trabajos.

    T son los tiempos de producción.

    U_s es el conjunto de máquinas o unidades de la etapa s.

    P es la ponderación de los números triangulares.

    Esta función calcula el makespan de una secuencia en el modelo FMMSP
    """

    # L es la cantidad total de etapas del sistema de producción.
    L = len(U_s)

    # I es el conjunto de trabajos.
    I = range(len(T))

    # S es el conjunto de etapas.
    S = range(L)

    # EsC es por Early start Comparación, esta variable guarda los tiempos ponderados (para hacer comparaciones entre tiempos diferentes) más tempranos en que un trabajo puede iniciar en cada máquina dada u
    EsC = [[0 for u in U_s[s]] for s in S]
    Es = [[(0, 0, 0) for u in U_s[s]] for s in S]

    Ts = [[None for s in S] for i in I]
    Tf = [[None for s in S] for i in I]

    for s in S:
        for i in I:
            if s == 0 and i == 0:
                v = np.argmin([P[i][u] for u in U_s[s]])
                EsC[s][v] += P[i][U_s[s][v]]
                Es[s][v] = np.add(Es[s][v], T[i][U_s[s][v]])

                Ts[i][s] = (0, 0, 0)
                Tf[i][s] = np.add(Ts[i][s], T[i][U_s[s][v]])
            if s == 0 and i > 0:
                v = np.argmin([P[i][u] + EsC[s][u - U_s[s][0]] for u in U_s[s]])
                EsC[s][v] += P[i][U_s[s][v]]
                Es[s][v] = np.add(Es[s][v], T[i][U_s[s][v]])

                Ts[i][s] = Es[s][v]
                Tf[i][s] = np.add(Ts[i][s], T[i][U_s[s][v]])
            if s > 0 and i == 0:
                v = np.argmin([P[i][u] for u in U_s[s]])
                EsC[s][v] += P[i][U_s[s][v]]
                Es[s][v] = np.add(Es[s][v], T[i][U_s[s][v]])

                Ts[i][s] = Tf[i][s - 1]
                Tf[i][s] = np.add(Ts[i][s], T[i][U_s[s][v]])
            if s > 0 and i > 0:
                v = np.argmin([P[i][u] + EsC[s][u - U_s[s][0]] for u in U_s[s]])
                EsC[s][v] += P[i][U_s[s][v]]
                Es[s][v] = np.add(Es[s][v], T[i][U_s[s][v]])

                if (Tf[i][s - 1][0] + 2*Tf[i][s - 1][1] + Tf[i][s - 1][2])/4 > EsC[s][v]:
                    Ts[i][s] = Tf[i][s - 1]
                else:
                    Ts[i][s] = Es[s][v]

                Tf[i][s] = np.add(Ts[i][s], T[i][U_s[s][v]])

    j = np.argmax(PT([[Tf[i][L - 1]] for i in I]))

    return Tf[j][L - 1]