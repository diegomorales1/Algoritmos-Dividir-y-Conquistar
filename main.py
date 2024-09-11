import cProfile
import pstats
import io
import matplotlib.pyplot as plt

from algoritmos import bubble_sort, python_sort, merge_sort, quick_sort, measure_time, read_dataset


#Este algoritmo nos brinda en tiempo de respuesta y rendimiento del ordenamiento
def profile_sorting_algorithm(algorithm, dataset):
    profiler = cProfile.Profile()
    profiler.enable()
    
    algorithm(dataset.copy())
    
    profiler.disable()
    s = io.StringIO()
    ps = pstats.Stats(profiler, stream=s).sort_stats('cumulative')
    
    total_calls = ps.total_calls
    total_time = ps.total_tt
    
    return f"{total_calls} function calls in {total_time:.3f} seconds\n"

#En esta funcion nos entragara un formato de salida estandar con el tiempo que demora en ordenar los datos y ademas graficar cada uno de los algoritmos mencionados
#se pueden editar los "sizes", dependiendo de cuantas carpetas se tengan, por ejemplo si se añade la carpeta 300 y quieres leerla, deberas integrarla en el codigo
#de la variable sizes para que la pueda leer, todo lo que tenga dentro de la carpeta 300, es solo un ejemplo burdo pero aplicable si se gusta probar mas ejemplos
def plot_times(order_type, lista):
    sizes = [20, 50, 100, 1000, 4000, 6000]
    times_bubble = []
    times_merge = []
    times_quick = []
    times_python_sort = []

    for size in sizes:
        file_path = f"{size}/dataset_{order_type}.txt"
        dataset = read_dataset(file_path)
    
        lista.append(f"\nProfiling para listas {order_type} desordenadas con tamaño {size}:\n")
        lista.append("Bubble Sort: " + profile_sorting_algorithm(bubble_sort, dataset))
        times_bubble.append(measure_time(bubble_sort, dataset.copy())*1000)  #Convertir a ms
        
        lista.append("Merge Sort: "+ profile_sorting_algorithm(merge_sort, dataset))
        times_merge.append(measure_time(merge_sort, dataset.copy())*1000)   
        
        lista.append("Quick Sort: "+ profile_sorting_algorithm(quick_sort, dataset))
        times_quick.append(measure_time(quick_sort, dataset.copy())*1000)    
        
        lista.append("Python Sort: "+ profile_sorting_algorithm(python_sort, dataset))
        times_python_sort.append(measure_time(python_sort, dataset.copy()) *1000)  
    
    for linea in lista:
        print(linea)
    print("-------------------------------------------")

    plt.plot(sizes, times_bubble, label="Bubble Sort")
    plt.plot(sizes, times_merge, label="Merge Sort")
    plt.plot(sizes, times_quick, label="Quick Sort")
    plt.plot(sizes, times_python_sort, label="Python Sort")

    plt.xlabel('Tamaño de la lista')
    plt.ylabel('Tiempo (ms)')
    plt.title(f'Tiempos de ordenamiento en listas - {order_type}')
    plt.legend()
    plt.show()

lista_completa = []
lista_parcial = []
lista_semi = []
#se llaman las funciones para el análisis de rendimiento con profiling para cada tipo de lista
plot_times('completamente', lista_completa)
plot_times('parcialmente', lista_parcial)
plot_times('semi', lista_semi)



