import random

#Genera datasets y ejemplos para listas dependiendo de algun rango entre el inicio el fin para crear una lista completamente desordenada
def generar_lista(inicio, fin, nombre):
    lista_numeros = list(range(inicio, fin + 1))
    random.shuffle(lista_numeros)
    lista_como_texto = ', '.join(map(str, lista_numeros))
    with open(nombre, 'w') as archivo:
        archivo.write(lista_como_texto)

#Genera datasets y ejemplos para listas dependiendo de algun rango entre el inicio el fin para crear una lista parcialmente desordenada con un grado modificable
def lista_parcial(inicio, fin, porcentaje_ordenado, nombre_archivo):
    lista_numeros = list(range(inicio, fin + 1))
    cantidad_ordenada = int(len(lista_numeros) * (porcentaje_ordenado / 100))
    

    lista_ordenada = lista_numeros[:cantidad_ordenada]
    lista_desordenada = lista_numeros[cantidad_ordenada:]
    
    random.shuffle(lista_desordenada)
    
    lista_final = lista_ordenada + lista_desordenada
    
    lista_como_texto = ', '.join(map(str, lista_final))
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(lista_como_texto)

#Genera datasets y ejemplos para listas dependiendo de algun rango entre el inicio el fin para crear una lista semi desordenada con un grado modificable
def lista_semi(inicio, fin, porcentaje_desordenado, nombre_archivo):
    lista_numeros = list(range(inicio, fin + 1))
    cantidad_desordenada = int(len(lista_numeros) * (porcentaje_desordenado / 100))
    
    lista_semi_ordenada = lista_numeros[:-cantidad_desordenada]
    lista_a_desordenar = lista_numeros[-cantidad_desordenada:]
    
    random.shuffle(lista_a_desordenar)
    
    lista_final = lista_semi_ordenada + lista_a_desordenar
    
    lista_como_texto = ', '.join(map(str, lista_final))
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(lista_como_texto)


#Aqui se llaman a las funciones y como estan en un rango lo podremos cambiar a nuestro gusto para generar los casos de prueba .txt

#Para la lista semi podemos decir algun % del desorden que queremos dentro de la lista
lista_semi(1, 100000, 20, 'dataset_semi.txt')

#En la lista parcial podremos decir el % de orden de los numeros dentro de la lista
lista_parcial(1, 100000, 50, 'dataset_parcialmente.txt')

generar_lista(1, 100000, 'dataset_completamente.txt')

