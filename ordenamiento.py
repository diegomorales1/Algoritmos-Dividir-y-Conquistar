import sys
import cProfile
import pstats
import io
import matplotlib.pyplot as plt

from algoritmos import bubble_sort, python_sort, merge_sort, quick_sort, measure_time


#Aqui se lee la entrada del dataset en una sola linea separados por ","
def read_dataset(file_path):
    with open(file_path, 'r') as f:
        data = f.read().strip() 
        dataset = [int(num) for num in data.split(',') if num.strip()]
    return dataset

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
def plot_times(dataset, lista):
    times_bubble = []
    times_merge = []
    times_quick = []
    times_python_sort = []
    lista.append("\nProfiling para la lista del archivo de entrada:\n")
    
    lista.append("Bubble Sort: " + profile_sorting_algorithm(bubble_sort, dataset))
    times_bubble.append(measure_time(bubble_sort, dataset.copy()))  # Convertir a ms
    
    lista.append("Merge Sort: " + profile_sorting_algorithm(merge_sort, dataset))
    times_merge.append(measure_time(merge_sort, dataset.copy()))    # Convertir a ms
    
    lista.append("Quick Sort: " + profile_sorting_algorithm(quick_sort, dataset))
    times_quick.append(measure_time(quick_sort, dataset.copy()))    # Convertir a ms
    
    lista.append("Python Sort: " + profile_sorting_algorithm(python_sort, dataset))
    times_python_sort.append(measure_time(python_sort, dataset.copy()))  # Convertir a ms
    
    for linea in lista:
        print(linea)
    print("-------------------------------------------")

    #Graficar los resultados
    algorithms = ['Bubble Sort', 'Merge Sort', 'Quick Sort', 'Python Sort']
    times = [times_bubble[0], times_merge[0], times_quick[0], times_python_sort[0]]

    plt.bar(algorithms, times, color=['blue', 'green', 'red', 'purple'])
    plt.xlabel('Algoritmos')
    plt.ylabel('Tiempo (ms)')
    plt.title('Tiempo de ejecución de algoritmos de ordenamiento')
    plt.show()

def main():
    #Verificar que se haya proporcionado el archivo de entrada por la terminal
    if len(sys.argv) < 2:
        print("Uso: python ordenamiento.py <archivo_dataset>")
        sys.exit(1)

    #Leer el archivo de entrada (dataset)
    dataset_file = sys.argv[1]
    dataset = read_dataset(dataset_file)
    lista_resultados = []
    plot_times(dataset, lista_resultados)

if __name__ == "__main__":
    main()
