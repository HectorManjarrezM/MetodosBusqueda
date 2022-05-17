import pprint
import os

# Pprint para mostrar de forma Pretty
pp = pprint.PrettyPrinter(indent=4)

# Grafo principal
grafo_principal = {}

# Lee el archivo .txt y carga el grafo_principal
with open('mapa.txt', 'r') as f:
    for l in f:
        ciudad_a, ciudad_b, costo = l.split()
        if ciudad_a not in grafo_principal:
            grafo_principal[ciudad_a] = {}
        grafo_principal[ciudad_a][ciudad_b] = int(costo)
        if ciudad_b not in grafo_principal:
            grafo_principal[ciudad_b] = {}
        grafo_principal[ciudad_b][ciudad_a] = int(costo)


pprint.pprint(grafo_principal, None, 1, 1)