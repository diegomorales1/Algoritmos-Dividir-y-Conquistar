import numpy as np
import matplotlib.pyplot as plt
import sys

from matrices import leer_matriz, profile_multiplication, cubic_multiply, cubic_optimized_multiply, strassen

#Funcion para calcular el tiempo inicial de ejecucion de una funcion hasta terminar

def measure_time(algorithm, A, B):
    import time
    start = time.time()
    algorithm(A, B)
    end = time.time()
    return end - start

#Main principal donde se hacen el llamado de cada funcion para calcular la matriz resultante-producto

def main():
    if len(sys.argv) != 3:
        print("debes de colocar en este orden: python multiplicacion.py matrix_a.txt matrix_b.txt")
        return

    matrix_a_file = sys.argv[1]
    matrix_b_file = sys.argv[2]

    A = leer_matriz(matrix_a_file)
    B = leer_matriz(matrix_b_file)
    
    size = len(A)
    print(f"\nProfiling para matrices con tamaño {size}x{size}:")

    times_traditional = []
    times_optimized = []
    times_strassen = []

    print("Cúbico Tradicional:")
    print(profile_multiplication(cubic_multiply, A, B))
    times_traditional.append(measure_time(cubic_multiply, A, B) * 1000)

    print("Cúbico Optimizado:")
    print(profile_multiplication(cubic_optimized_multiply, A, B))
    times_optimized.append(measure_time(cubic_optimized_multiply, A, B) * 1000)

    print("Strassen:")
    print(profile_multiplication(strassen, A, B))
    times_strassen.append(measure_time(strassen, A, B) * 1000)

if __name__ == "__main__":
    main()
