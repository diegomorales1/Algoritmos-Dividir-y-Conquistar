import random
import time

#Aqui se leen los datasets separados por una ","
def read_dataset(file_path):
    with open(file_path, 'r') as f:
        data = f.readline().strip().split(',')
        return list(map(int, data))

#Algoritmo de ordenamiento cuadratico
def bubble_sort(lista):
    n = len(lista)
    iteraciones = 0  #Contador de iteraciones
    for i in range(n):
        for j in range(0, n-i-1):
            iteraciones += 1
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista, iteraciones

#Algoritmo de ordenamiento por defecto de python
def python_sort(lista):
    iteraciones = 0
    lista.sort()
    iteraciones = len(lista) * (len(lista) - 1) // 2  # Aproximación de comparaciones en promedio
    return lista, iteraciones

#Algoritmo de ordenamiento dividir y conquistar
def merge_sort(lista):
    def merge(lista, mitad_izquierda, mitad_derecha):
        i = j = k = 0
        iteraciones = 0

        while i < len(mitad_izquierda) and j < len(mitad_derecha):
            iteraciones += 1
            if mitad_izquierda[i] < mitad_derecha[j]:
                lista[k] = mitad_izquierda[i]
                i += 1
            else:
                lista[k] = mitad_derecha[j]
                j += 1
            k += 1

        while i < len(mitad_izquierda):
            lista[k] = mitad_izquierda[i]
            i += 1
            k += 1

        while j < len(mitad_derecha):
            lista[k] = mitad_derecha[j]
            j += 1
            k += 1

        return iteraciones

    if len(lista) <= 1:
        return lista, 0

    mitad = len(lista) // 2
    mitad_izquierda = lista[:mitad]
    mitad_derecha = lista[mitad:]

    izquierda_ordenada, iteraciones_izquierda = merge_sort(mitad_izquierda)
    derecha_ordenada, iteraciones_derecha = merge_sort(mitad_derecha)

    iteraciones_mezcla = merge(lista, izquierda_ordenada, derecha_ordenada)

    return lista, iteraciones_izquierda + iteraciones_derecha + iteraciones_mezcla

#Algoritmo de ordenamiento dividir y conquistar con pivote
def quick_sort(lista):
    iteraciones = 0

    def quick_sort_recursivo(lista):
        nonlocal iteraciones
        if len(lista) <= 1:
            return lista
        else:
            pivote = random.choice(lista)  #Seleccionar un pivote aleatorio
            menores_que_pivote = [x for x in lista if x < pivote]
            iguales_al_pivote = [x for x in lista if x == pivote]
            mayores_que_pivote = [x for x in lista if x > pivote]
            iteraciones += len(lista) - 1  #Comparaciones hechas en esta llamada
            return quick_sort_recursivo(menores_que_pivote) + iguales_al_pivote + quick_sort_recursivo(mayores_que_pivote)

    lista_ordenada = quick_sort_recursivo(lista)
    return lista_ordenada, iteraciones

#Esta funcion nos permite sacar un performance de tiempo entre que se completa la lista a ordenar
def measure_time(func, lista):
    start_time = time.perf_counter()
    func(lista)
    end_time = time.perf_counter()
    return end_time - start_time