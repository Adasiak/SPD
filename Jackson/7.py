# Funkcja obliczająca wartość funkcji Cmax dla danej permutacji zadań
def Cmax(permutation, tasks):
    n = len(permutation)
    m = len(tasks[0])
    C = [[0] * (m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            C[i][j] = max(C[i-1][j], C[i][j-1]) + tasks[permutation[i-1]][j-1]
    return C[n][m]

# Funkcja wyznaczająca optymalną kolejność zadań
def jackson(tasks):
    n = len(tasks)
    # Tworzymy listę zadań do wykonania, posortowaną względem terminów dostępności
    available_tasks = sorted(range(n), key=lambda x: tasks[x][0])
    # Inicjalizujemy permutację wynikową jako pustą listę
    result_permutation = []
    # Dla każdego zadania w kolejności terminów dostępności
    for task_idx in available_tasks:
        # Szukamy pozycji w permutacji wynikowej, w której można umieścić to zadanie,
        # tak, aby minimalizować wartość Cmax
        best_pos = 0
        best_Cmax = float('inf')
        for pos in range(len(result_permutation)+1):
            curr_permutation = result_permutation[:pos] + [task_idx] + result_permutation[pos:]
            curr_Cmax = Cmax(curr_permutation, tasks)
            if curr_Cmax < best_Cmax:
                best_Cmax = curr_Cmax
                best_pos = pos
        # Dodajemy zadanie na najlepszej pozycji
        result_permutation = result_permutation[:best_pos] + [task_idx] + result_permutation[best_pos:]
    return Cmax(result_permutation, tasks)

# Otwieramy plik z danymi
with open("nazwa_pliku_zadan.txt", "r") as input_file:
    n = int(input_file.readline())
    tasks = []
    for i in range(n):
        r, p = map(int, input_file.readline().split())
        tasks.append((r, p))

# Wyliczamy ilość powtórzeń algorytmu w zależności od ilości danych
# repetitions = int(max(10, 10000 // n))
repetitions = max(100, min(10000 // n, 10*n))

# Wywołujemy algorytm Jacksona repetitions razy
results = []
for i in range(repetitions):
    result = jackson(tasks)
    results.append(result)
    # print(f"Wynik {i+1}: {result}")

# Obliczamy średnią wartość funkcji Cmax
avg_result = sum(results) / repetitions
print(f"Średni wynik: {avg_result}")

# Wyświetlamy informację o ilości danych i liczbie powtórzeń algorytmu
print(f"Liczba zadań: {n}")
print(f"Liczba powtórzeń algorytmu: {repetitions}")
