import numpy as np
import cProfile
import pstats
import io
import matplotlib.pyplot as plt

#Aqui se leen las matrices en formato que cada uno este separado por un ","
def leer_matriz(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split("\n")
        matrix = [list(map(int, row.split(','))) for row in data]
    return matrix

#Esta funcion calcula el rendimiento de cada algoritmo de multiplicacion
def profile_multiplication(algorithm, A, B):
    profiler = cProfile.Profile()
    profiler.enable()
    
    algorithm(A, B)
    
    profiler.disable()
    
    s = io.StringIO()
    ps = pstats.Stats(profiler, stream=s).sort_stats('cumulative')
    total_calls = ps.total_calls
    total_time = ps.total_tt
    
    #Mostrar sólo el número de llamadas y el tiempo total
    return f"{total_calls} function calls in {total_time:.3f} seconds\n"

#Alogirtmo cubico iterativo tradicional
def cubic_multiply(A, B):
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

#Algoritmo cúbico optimizado (transponiendo la segunda matriz)
def cubic_optimized_multiply(A, B):
    B_T = np.transpose(B)
    return np.dot(A, B_T)

#Algoritmo de Strassen para matrices de tamaño n x n definidos
def strassen(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    
    mid = n // 2

    A11 = [[A[i][j] for j in range(mid)] for i in range(mid)]
    A12 = [[A[i][j] for j in range(mid, n)] for i in range(mid)]
    A21 = [[A[i][j] for j in range(mid)] for i in range(mid, n)]
    A22 = [[A[i][j] for j in range(mid, n)] for i in range(mid, n)]
    
    B11 = [[B[i][j] for j in range(mid)] for i in range(mid)]
    B12 = [[B[i][j] for j in range(mid, n)] for i in range(mid)]
    B21 = [[B[i][j] for j in range(mid)] for i in range(mid, n)]
    B22 = [[B[i][j] for j in range(mid, n)] for i in range(mid, n)]

    M1 = strassen(add(A11, A22), add(B11, B22))
    M2 = strassen(add(A21, A22), B11)
    M3 = strassen(A11, subtract(B12, B22))
    M4 = strassen(A22, subtract(B21, B11))
    M5 = strassen(add(A11, A12), B22)
    M6 = strassen(subtract(A21, A11), add(B11, B12))
    M7 = strassen(subtract(A12, A22), add(B21, B22))

    C11 = add(subtract(add(M1, M4), M5), M7)
    C12 = add(M3, M5)
    C21 = add(M2, M4)
    C22 = add(subtract(add(M1, M3), M2), M6)

    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(mid):
        for j in range(mid):
            C[i][j] = C11[i][j]
            C[i][j+mid] = C12[i][j]
            C[i+mid][j] = C21[i][j]
            C[i+mid][j+mid] = C22[i][j]
    
    return C

#Funcion que utiliza strassen para sumar matrices
def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A))] for i in range(len(A))]

##Funcion que utiliza strassen para restar matrices
def subtract(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A))] for i in range(len(A))]

