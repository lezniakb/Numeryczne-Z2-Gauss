import numpy as np

def wczytanie_macierzy(nazwa_pliku):
    # Dopisujemy txt do nazwy pliku
    nazwa_pliku += ".txt"
    # Otwieramy plik tylko do odczytu 'r'
    with open(nazwa_pliku, 'r') as plik:
        # Tworzymy listę 'rownania', która zawiera wszystkie wiersze w pliku
        rownania = plik.readlines()

    n = len(rownania)
    # Sprawdzamy ilość równań
    if n > 10:
        print("BŁĄD: Przekroczono ilość 10 równań\n"
              "Podana ilość równań: " + str(n))

    # Deklarujemy macierze współczynników 'A' i wyrazów wolnych 'b'
    A = []
    b = []

    # Przechodzimy przez wszystkie równania, zamieniamy je ze stringa na float i odpowiednio dodajemy do naszych macierzy
    for rownanie in rownania:
        wartosci = list(map(float, rownanie.split()))
        # Współczynniki równań
        A.append(wartosci[:-1])
        # Wyrazy wolne
        b.append(wartosci[-1])

            # idk czy możemy korzystać z numpy
    # A = np.array(A, dtype=float)
    # b = np.array(b, dtype=float)

    # Zamieniamy listy na macierze numpy typu float
    return A, b