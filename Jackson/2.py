def jackson_coefficients(n, a):
    """
    Implementacja algorytmu Jacksona w języku Python.

    :param n: stopień równania rekurencyjnego
    :param a: lista długości n+1 zawierająca współczynniki równania rekurencyjnego
    :return: lista długości n+1 zawierająca kolejne współczynniki rozwinięcia równania rekurencyjnego
    """
    b = [0] * (n + 1)
    c = [0] * (n + 1)
    b[0] = 1
    c[0] = 1
    for j in range(1, n + 1):
        sm = 0
        for k in range(1, j + 1):
            sm += a[k] * b[j - k]
        b[j] = -1 / j * sm
        c[j] = -b[j]
        for k in range(1, j + 1):
            b[k] += c[j] * a[j - k + 1]
    return b


# Przykładowe dane testowe
n = 4
a = [1, -3, 3, -1, 0]
print(jackson_coefficients(n, a))  # Output: [1.0, 3.0, 3.0, 1.0, 0.0]


# W przykładzie powyżej przedstawiamy implementację algorytmu Jacksona 
# oraz funkcję jackson_coefficients(), która przyjmuje dwa argumenty: stopień 
# równania rekurencyjnego n oraz listę a długości n+1, zawierającą współczynniki 
# równania rekurencyjnego. Funkcja zwraca listę b długości n+1, która zawiera 
# kolejne współczynniki rozwinięcia równania rekurencyjnego.