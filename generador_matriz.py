import random

#Funcion para generar matrices de distintos tamaños para probar su multiplicacion

def generar_matriz(filename, size, min_val=0, max_val=10):
    with open(filename, 'w') as f:
        for _ in range(size):
            row = [str(random.randint(min_val, max_val)) for _ in range(size)]
            f.write(','.join(row) + '\n')

generar_matriz('matrix_512_A.txt', 512, 1, 10)
generar_matriz('matrix_512_B.txt', 512, 1, 10)
