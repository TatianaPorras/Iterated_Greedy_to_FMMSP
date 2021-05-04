def DNEH_SMR(l_tT_i_u, L, n_s):
    """
    l_tT_i_u es la lista de números triangulares difusos del tiempo de producción del trabajo i en la unidad o máquina u. El prefijo 'l_' es por lista de Python, 't' es por triangular difuso.

    L es la cantidad total de etapas del sistema de producción.

    n_s es la lista con la cantidad de unidades o máquinas por etapa s.
    """

    import math

    k = math.floor(L/2)

    # l_tTa_i_s es la lista de los tiempos de producción promedio del trabajo i en la etapa s
    l_tTa_i_s = 1/n * 5