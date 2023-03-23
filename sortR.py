import random
import timeit
def generate_tasks(n:int):
    tasks = []
    for _ in range(n):
        tmp_list = []
        for _ in range(3):
            tmp_list.append(random.randint(1, n/2))
        tasks.append(tmp_list)
    return tasks


def algorytmS(tasks):
    # start zegara
    start_time = timeit.default_timer()
    # Sortowanie zadań według terminu dostępności, 
    tasks = sorted(tasks, key=lambda x: (x[0]))
    # Obliczenie Cmax dla posortowanej kolejności zadań
    cmax = 0
    current_time = 0
    # Obliczanie całkowitego czasu wykonywania wszytskich zadań
    for task in tasks:
        current_time = max(current_time, task[0]) + task[1]
        tmp_list = [task for task in tasks[tasks.index(task)+1::] if task[0] <= current_time ]
        # gdy pozostałe elementy mają czas przybycia mniejszy niż obceny czas
        # następuje odwrotne sortowanie po czasie dostarczenia
        tmp_list = sorted(tmp_list, key=lambda x: (-x[2]))
        for tmp_list_index in range(len(tmp_list)):
            tasks[tasks.index(task)+1+tmp_list_index] = tmp_list[tmp_list_index]
        
        cmax = max(cmax, current_time)
    
    cmax += tasks[-1][2]
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

    m = 10
    cmaxs = []
    extimes = []
    ll = []
    ll.append(m)
    for i in range(45):
        if i > 35:
            m+=100000
            # ll.append(m)
        elif i > 26:
            m+=10000
            # ll.append(m)
        elif i > 17:
            m+=1000
            # ll.append(m)
        elif i > 8:
            m+=100
            # ll.append(m)
        else:
            m +=10
        
        ll.append(m)

    for i in range(45):
        # print(i)
        # n = int(m)
        print(ll[i])
        
        cmax, ex_time, sorted_tasks = algorytmS(generate_tasks(ll[i]))

        tmp_dict = {cmax :ex_time}
        cmaxs.append(cmax)
        extimes.append(ex_time)
    
    aa = 0
    print(ll)
        
    with open(f'cmaxs.txt', 'w') as file:
            for el in cmaxs:
                file.write(str(el)+"\n")
            
    with open(f'ex_times.txt', 'w') as file:
            for el in extimes:
                file.write(str(el)+"\n")