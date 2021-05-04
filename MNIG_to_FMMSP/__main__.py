from algorithms import DNEH_SMR, destruction_reconstruction, local_search

# Datos de la instancia de prueba
l_tT_i_u = 
[
    [(10,12,13), (7,8,10), (10,11,12), (8,9,10), (6,7,8), (4,5,6), (11,13,15), (10,11,12), (5,6,8), (15,17,20)], 

    [(11,12,14), (8,9,10), (9,10,12), (6,7,8), (8,9,10), (2,3,4), (1,2,3), (18,19,23), (4,5,6), (12,14,15)],

    [(9,10,12), (5,6,8), (2,3,4), (7,8,9), (4,5,6), (15,16,19), (11,13,14), (5,6,7), (14,15,16), (16,17,20)],

    [(6,7,9), (4,5,6), (5,6,8), (4,5,6), (6,7,8), (13,14,15), (10,11,13), (6,7,9), (19,21,25), (17,18,21)],

    [(8,9,10), (4,5,6), (5,6,7), (5,6,8), (6,7,9), (15,16,20), (9,10,12), (7,8,10), (10,12,13), (18,19,21)]
]
# l_tT_i_u tiene la estructura [ máquina1, máquina2, máquinaM ], a su vez cada máquina tiene la forma [trabajo1, trabajo2, trabajoN], y cada trabajo tiene la forma (tiempo_pesimista, tiempo_promedio, tiempo_optimista)

n_s = [2, 3]

L = len(n_s)

