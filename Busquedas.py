import pprint
import os
from queue import PriorityQueue

# Pprint para mostrar de forma Pretty
pp = pprint.PrettyPrinter(indent=4)

# Grafo principal
grafo_principal = {}
heuris = {}

# Lee el archivo .txt y carga el grafo_principal
with open('heu.txt', 'r') as f:
    for l in f:
        ciudad_a1, ciudad_b1, costofic = l.split()
        if ciudad_a1 not in heuris:
            heuris[ciudad_a1] = {}
        heuris[ciudad_a1][ciudad_b1] = int(costofic)
        if ciudad_b1 not in heuris:
            heuris[ciudad_b1] = {}
        heuris[ciudad_b1][ciudad_a1] = int(costofic)

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


# Breadth First Search Method (Busqueda en Amplitud)
def BreadthFirstSearch(grafo, inicio, destino):
    cola = [(inicio, [inicio], 0)]
    visitado = {inicio}
    nodosGenerados = 1
    cerrado = []
    listaAbiertos = []

    while cola:
        (node, camino, costo) = cola.pop(0)
        print()
        print("Ciudad Origen: " + str(node))
        cerrado.append(node)
        if listaAbiertos.__len__() is not 0:
            listaAbiertos.remove(node)

        for temp in grafo[node].keys():
            if temp == destino:
                nodosGenerados = nodosGenerados + 1
                #print()
                #print("Ciudad Origen: " + str(node))
                print("     Nodo generado: " + str(temp))
                print()
                print("NODO FINAL: " + str(temp))
                print("TOTAL DE NODOS GENERADOS: " + str(nodosGenerados))
                return ""
                #return camino + [temp], costo + grafo[node][temp]
            else:
                if temp not in visitado:
                    nodosGenerados = nodosGenerados + 1
                    print("     Nodo generado: " + str(temp))
                    listaAbiertos.append(temp)
                    visitado.add(temp)
                    cola.append((temp, camino + [temp], costo + grafo[node][temp]))
                else:
                    print("     Ciudad Destino: " + str(temp))
        print()
        print("Nodos abiertos: " + str(listaAbiertos))
        print("Nodos cerrados:" + str(cerrado))


# Depth First Search Method (Busqueda en Profundidad)
def DepthFirstSearch(grafo, inicio, destino):
    pila = [(inicio, [inicio], 0)]
    visitado = {inicio}
    nodosGenerados = 1
    cerrado = []
    listaAbiertos = []

    while pila:
        (node, camino, costo) = pila.pop(0)
        print()
        print("Ciudad Origen: " + str(node))
        cerrado.append(node)
        
        if listaAbiertos.__len__() is not 0:
            listaAbiertos.remove(node)

        for temp in grafo[node].keys():
            if temp == destino:
                nodosGenerados = nodosGenerados + 1
                #print()
                #print("Ciudad Origen: " + str(node))
                print("     Nodo generado: " + str(temp))
                print()
                print("NODO FINAL: " + str(temp))
                print("TOTAL DE NODOS GENERADOS: " + str(nodosGenerados))
                return ""
                #return camino + [temp], costo + grafo[node][temp]
            else:
                if temp not in visitado:
                    nodosGenerados = nodosGenerados + 1
                    print("     Nodo generado: " + str(temp))
                    listaAbiertos.append(temp)
                    visitado.add(temp)
                    pila.insert(0,(temp, camino + [temp], costo + grafo[node][temp]))
                else:
                    print("     Ciudad Destino: " + str(temp))
        print()
        print("Nodos abiertos: " + str(listaAbiertos))
        print("Nodos cerrados:" + str(cerrado))


# Metodo de busqueda A*
def a_star_search(grafo, inicio, destino,heuristica):
    pila = [(inicio, [inicio], 0)]
    visitado = {inicio}
    abierto={inicio}
    pq = PriorityQueue()
    pq.put((0, inicio))
    nodosGenerados = 1
    distanciaTotal = 0
    cerrado = []
    listaAbiertos = []
    nodoMenor = None
    costoNodoMenor = 99999999

    while pq.empty() == False:
        ciudadOrigen = pq.get()[1]
        print()
        print("Ciudad Origen: " + str(ciudadOrigen))
        cerrado.append(ciudadOrigen)

        if listaAbiertos.__len__() is not 0:
            listaAbiertos.remove(ciudadOrigen)
        #print(ciudadOrigen, end=" ")
        if ciudadOrigen == destino:
            nodosGenerados = nodosGenerados + 1
            #print("Ciudad Origen: " + str(ciudadOrigen))
            #print("     Nodo generado: " + str(ciudadOrigen))
            print()
            print("NODO FINAL: " + str(ciudadOrigen))
            print("TOTAL DE NODOS GENERADOS: " + str(nodosGenerados))
            print("DISTANCIA TOTAL RECORRIDA: " + str(distanciaTotal))
            
            
            return ""

        listaCiudadesDestino = list(grafo[ciudadOrigen].keys())
        listaCostos = list(grafo[ciudadOrigen].values())
        listaCostosfic = list(heuristica[ciudadOrigen].values())
        #print(list(grafo[ciudadOrigen].keys()))
        #print(list(grafo[ciudadOrigen].values()))
        bandera = False
        for i in range(len(listaCiudadesDestino)):
            
            ciudadDestino = listaCiudadesDestino[i]
            estimacion= listaCostosfic[i]
            costo = listaCostos[i]
            TotalC=costo + estimacion
            if ciudadDestino not in visitado:
                if bandera == False:
                    distanciaTotal = distanciaTotal + TotalC
                    bandera = True
                
                nodosGenerados = nodosGenerados + 1
                print("     Nodo generado: " + str(ciudadDestino) + " - Costo: " + str(TotalC))
                listaAbiertos.append(ciudadDestino)               
                visitado.add(ciudadDestino)
                pq.put((costo,ciudadDestino)) 
                
                             
            else:
                print("     Nodo generado: " + str(ciudadDestino) + " - Costo: " + str(TotalC))
        
        print()
        print("Nodos abiertos: " + str(listaAbiertos))
        print("Nodos cerrados:" + str(cerrado))

   
# Metodo de busqueda Primero el mejor
def best_first_search(grafo, inicio, destino):
    pila = [(inicio, [inicio], 0)]
    visitado = {inicio}
    pq = PriorityQueue()
    pq.put((0, inicio))
    nodosGenerados = 1
    distanciaTotal = 0

    visitado = {inicio}
    cerrado = []
    listaAbiertos = []
    nodoMenor = None
    costoNodoMenor = 99999999

    while pq.empty() == False:
        ciudadOrigen = pq.get()[1]
        print()
        print("Ciudad Origen: " + str(ciudadOrigen))
        cerrado.append(ciudadOrigen)
        
        if listaAbiertos.__len__() is not 0:
            listaAbiertos.remove(ciudadOrigen)
        #print(ciudadOrigen, end=" ")
        if ciudadOrigen == destino:
            nodosGenerados = nodosGenerados + 1
            #print("Ciudad Origen: " + str(ciudadOrigen))
            #print("     Nodo generado: " + str(ciudadOrigen))
            print()
            print("NODO FINAL: " + str(ciudadOrigen))
            print("TOTAL DE NODOS GENERADOS: " + str(nodosGenerados))
            print("DISTANCIA TOTAL RECORRIDA: " + str(distanciaTotal))
            return ""

        listaCiudadesDestino = list(grafo[ciudadOrigen].keys())
        listaCostos = list(grafo[ciudadOrigen].values())
        #print(list(grafo[ciudadOrigen].keys()))
        #print(list(grafo[ciudadOrigen].values()))
        bandera = False
        for i in range(len(listaCiudadesDestino)):
            ciudadDestino = listaCiudadesDestino[i]
            costo = listaCostos[i]
            #print("Costo: " + str(listaCostos[i]))
            if ciudadDestino not in visitado:
                if bandera == False:
                    distanciaTotal = distanciaTotal + costo
                    bandera = True
                nodosGenerados = nodosGenerados + 1
                print("     Nodo generado: " + str(ciudadDestino) + " - Costo: " + str(costo))
                listaAbiertos.append(ciudadDestino)
                visitado.add(ciudadDestino)
                pq.put((costo,ciudadDestino))
            else:
                print("     Ciudad Destino: " + str(ciudadDestino) + " - Costo: " + str(costo))
        
        print()
        print("Nodos abiertos: " + str(listaAbiertos))
        print("Nodos cerrados:" + str(cerrado))

n = 1
inicio = "Culiacan"
while n == 1:
    os.system("CLS")
    print("""============================================ Grafo Completo ============================================""")
    pp.pprint(grafo_principal)
    print("""===================== MENU =============================================================================
                [1] Amplitud
                [2] Profundidad
                [3] A Star
                [4] Primero el mejor
                [0] Salir
========================================================================================================""")
    x = input("Opcion: ")
    if x == '1':
        destino = input("Ingresa el Destino: ")
        while destino not in grafo_principal:
            print("Ciudad no encontrada intenta nuevamente")
            destino = input("Ingresa el Destino: ")
        print("""============================================ 
                Resultados 
============================================""")
        print(BreadthFirstSearch(grafo_principal, inicio, destino))
        print("============================================")
        os.system("pause")

    elif x == '2':
        destino = input("Ingresa el Destino: ")
        while destino not in grafo_principal:
            print("Ciudad no encontrada intenta nuevamente")
            destino = input("Ingresa el Destino: ")
        print("""============================================
                Resultados
============================================""")
        print(DepthFirstSearch(grafo_principal, inicio, destino))
        print("============================================")
        os.system("pause")

    elif x == '3':
        destino = input("Ingresa el Destino: ")
        while destino not in grafo_principal:
            print("Ciudad no encontrada intenta nuevamente")
            destino = input("Ingresa el Destino: ")
        print("""============================================
                Resultados
============================================""")
        print(a_star_search(grafo_principal, inicio, destino,heuris))
        print("============================================")
        os.system("pause")

    elif x == '4':
        destino = input("Ingresa el Destino: ")
        while destino not in grafo_principal:
            print("Ciudad no encontrada intenta nuevamente")
            destino = input("Ingresa el Destino: ")
        print("""============================================
                Resultados
============================================""")
        print(best_first_search(grafo_principal, inicio, destino))
        print("============================================")
        os.system("pause")

    elif x == '0':
        break
