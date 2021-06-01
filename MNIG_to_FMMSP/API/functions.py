import numpy as np

def c_range(llim, ulim):
    """
    c_range es por correct range, llim es por lower limit, ulim es por upper limit.

    Esta functión toma un range que empieza en llim y devuelve un range que empieza en llim - 1.
    """

    return range(llim - 1, ulim)

def PT(T):
    """
    P es por ponderación, PT es por Ponderación de Todos los trabajos en todas las máquinas.

    Esta función devuelve la ponderación de las tres partes de un número triangular difuso
    """

    I = range(len(T))

    if (np.array(T).ndim == 3):
        P = [[(T[i][u][0] + 2*T[i][u][1] + T[i][u][2])/4 for u in range(len(T[0]))] for i in I]
    elif (np.array(T).ndim == 2):
        P = [(T[i][0] + 2*T[i][1] + T[i][2])/4 for i in I]
    elif (np.array(T).ndim == 1):
        P = (T[0] + 2*T[1] + T[2])/4
    return P

def ct(pi, i, ex = []):
    """
    pi es una secuencia de trabajos.

    i es uno de los trabajos.

    ex es una lista de trabajos excluidos cuya posición no es cambiada por i

    Esta función devuelve una lista de secuencias, poniendo i en cada puesto de la secuencia de trabajos. ct es por cambiar trabajos.
    """
    pi2 = pi.copy()
    pis = []

    if i not in pi2: pi2.append(i)
    for j in range(len(pi2)):
        if j not in ex:
            pi2[pi2.index(i)], pi2[j] = pi2[j], pi2[pi2.index(i)]
            pis.append(pi2.copy())
    return pis

def st(pi, i, ex = []):
    """
    pi es una secuencia de trabajos.

    i es uno de los trabajos.

    ex es una lista de trabajos excluidos cuya posición no es cambiada por i

    Esta función devuelve una lista de secuencias, intercambiando i por cada uno de los otros trabajos de la secuencia. st es por swap trabajos (porque esta función es creada por necesidad de la función swap del algoritmo MNIG).
    """
    pi2 = pi.copy()
    pis = []
    if i not in pi2: pi2.append(i)

    for j in range(len(pi2)):
        if j not in ex:
            k = pi2.index(i)
            pi2[k], pi2[j] = pi2[j], pi2[k]
            pis.append(pi2.copy())
            pi2[k], pi2[j] = pi2[j], pi2[k]
    return pis

def makespan(pi, Tn, U_s, Pn, debug = False):
    """
    pi es una secuencia de trabajos.

    Tn son los tiempos de producción en orden de secuencia natural, 1, 2 ,3, ...

    U_s es el conjunto de máquinas o unidades de la etapa s.

    Pn es la ponderación de los números triangulares en orden de secuencia natural, 1, 2, 3, ...

    Esta función calcula el makespan de una secuencia en el modelo FMMSP
    """

    # L es la cantidad total de etapas del sistema de producción.
    L = len(U_s)

    # I es el conjunto de trabajos.
    I = range(len(pi))

    T = [Tn[pi[i] - 1] for i in I]
    P = [Pn[pi[i] - 1] for i in I]

    # S es el conjunto de etapas.
    S = range(L)

    # EsC es por Early start Comparación, esta variable guarda los tiempos ponderados (para hacer comparaciones entre tiempos diferentes) más tempranos en que un trabajo puede iniciar en cada máquina dada u
    UT = np.sum([len(U_s[s]) for s in c_range(1, L)])
    U = range(UT)

    Ts = [[(0, 0, 0) for s in S] for i in I]
    Tf = [[(0, 0, 0) for s in S] for i in I]
    UI = [[(0, 0, 0) for s in S] for i in I]
    TfU = [[(0, 0, 0) for u in U] for i in I]

    for s in S:
        if (debug == True): print()
        for i in I:
            if s == 0 and i == 0:
                v = np.argmin([PT(np.add(TfU[i][u], T[i][u])) for u in U_s[s]]) + U_s[s][0]

                Ts[i][s] = (0, 0, 0)
                Tf[i][s] = np.add(Ts[i][s], T[i][v])
                for j in I: TfU[j][v] = Tf[i][s]
            if s == 0 and i > 0:
                v = np.argmin([PT(np.add(TfU[i][u], T[i][u])) for u in U_s[s]]) + U_s[s][0]

                Ts[i][s] = TfU[i][v]
                Tf[i][s] = np.add(Ts[i][s], T[i][v])
                for j in I: TfU[j][v] = Tf[i][s]
            if s > 0 and i == 0:
                for u in U_s[s]:
                    if (PT(Tf[i][s - 1]) > PT(TfU[i][u])):
                        TfU[i][u] = Tf[i][s - 1]
                v = np.argmin([PT(np.add(TfU[i][u], T[i][u])) for u in U_s[s]]) + U_s[s][0]

                Ts[i][s] = Tf[i][s - 1]
                Tf[i][s] = np.add(Ts[i][s], T[i][v])
                for j in I: TfU[j][v] = Tf[i][s]
            if s > 0 and i > 0:
                for u in U_s[s]:
                    if (PT(Tf[i][s - 1]) > PT(TfU[i][u])):
                        TfU[i][u] = Tf[i][s - 1]
                v = np.argmin([PT(np.add(TfU[i][u], T[i][u])) for u in U_s[s]]) + U_s[s][0]

                if (PT(Tf[i][s - 1]) > PT(TfU[i][v])):
                    Ts[i][s] = Tf[i][s - 1]
                else:
                    Ts[i][s] = TfU[i][v]

                Tf[i][s] = np.add(Ts[i][s], T[i][v])
                for j in I: TfU[j][v] = Tf[i][s]
            if (debug == True):
                piO = "%2d" % (pi[i])
                TsO = "(%2d, %2d, %2d)" % (Ts[i][s][0], Ts[i][s][1], Ts[i][s][2])
                TfO = "(%2d, %2d, %2d)" % (Tf[i][s][0], Tf[i][s][1], Tf[i][s][2])
                print("pi[i]:", piO, "   s:", s + 1, "   u:", v + 1, "   Ts:", TsO, "   Tf:", TfO)

    n = np.argmax(PT([[Tf[i][L - 1]] for i in I]))

    return Tf[n][L - 1]