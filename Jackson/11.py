import random
import timeit
def generate_tasks(n:int):
    tasks = []
    for _ in range(n):
        tmp_list = []
        for _ in range(2):
            tmp_list.append(random.randint(1, n/2))
        tasks.append(tmp_list)
    return tasks

def jackson(tasks:list):
    # start zegara
    start_time = timeit.default_timer()
    # Sortowanie zadań według terminu dostępności, 
    # gdy są identyczne następuje odwrotne sortowanie po czasie wykonywania
    # O(n log n), gdzie n oznacza liczbę zadań.
    tasks = sorted(tasks, key=lambda x: (x[0] , -x[1]))
    # Obliczenie Cmax dla posortowanej kolejności zadań
    cmax = 0
    current_time = 0
    # Obliczanie całkowitego czasu wykonywania wszytskich zadań
    for task in tasks:
        current_time = max(current_time, task[0]) + task[1]
        cmax = max(cmax, current_time)
    # zatrzymanie zegara
    end_time = timeit.default_timer()
    # obliczanie czasu wykonywania się algorytmu
    execution_time = end_time - start_time
    # Zwrócenie całkowitego czasu wykonywania wszytskich zadań, 
    # czasu egzekucji, 
    # permutacji zadań
    return cmax, execution_time, tasks

if __name__ == "__main__":

    # # Wczytanie danych z pliku
    # with open("nazwa_pliku_zadan1.txt", 'r') as file:
    #     n = int(file.readline())
    #     tasks = [list(map(int, line.split())) for line in file]

    m = "50"
    for i in range(6):
        n = int(m)
        cmax,ex_time, sorted_tasks = jackson(generate_tasks(n))

        # Zapisanie wyniku do pliku
        with open(f'5iteracja{i}.txt', 'w') as file:
            file.write("Cmax: " +str(cmax) + '\n')
            file.write("Czas egzekucji: " +str(ex_time) + " s" + '\n')
            file.write("Posortowane zadania: " + str(sorted_tasks) + '\n')
        m +="0"