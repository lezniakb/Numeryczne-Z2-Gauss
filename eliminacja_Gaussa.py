def Gauss(macierz):
    dokladnosc = 1e-12
    n = len(macierz)
    # Macierz przechowująca wyniki
    X = []

    for niewiadoma in range(n):
        X.append(0)

    # Wiem, że pojebane idk jak to w komentarzu wytłumaczyć :sob:

    # Doprowadzamy macierz do postaci trójkątnej
    # dla kazdego rzedu w macierzy
    for i in range(n - 1):
        # jesli element jest mniejszy niz nasza dokladnosc
        if abs(macierz[i][i]) < dokladnosc:
            # to szukamy w dalszych wierszach wspolczynnika, ktory jest rozny 0
            # jesli taki znajdziemy to zamieniamy je miejscami
            for l in range(i + 1, n):
                if abs(macierz[l][i]) > dokladnosc:
                    for m in range(n + 1):
                        temp = macierz[i][m]
                        macierz[i][m] = macierz[l][m]
                        macierz[l][m] = temp

            # jezeli w zadnym z wierszy nie zostanie znaleziony poszukiwany wspolczynnik to wyswietlany jest blad
            if abs(macierz[i][i]) < dokladnosc:
                print("Błąd: dzielenie przez 0. Macierz nie została rozwiązana.")
                # zwroc -1 jako kod blednego zakonczenia funkcji
                return -1
        # dla wiersza i przetwarzane sa wszystkie wiersze ponizej
        for j in range(i + 1, n):
            m = - macierz[j][i] / macierz[i][i]
            for k in range(n + 1):
                macierz[j][k] = macierz[j][k] + m * macierz[i][k]

    print("\nMacierz po sprowadzeniu do postaci trójkątnej górnej")
    for wiersz in macierz:
        print(wiersz)
    print("")
    # Odwrotne wyznaczanie niewiadomych
    for o in range(n - 1, -1, -1):
        if abs(macierz[o][o]) < dokladnosc:
            if abs(macierz[o][o + 1]) < dokladnosc:
                print("Błąd: Wykryto układ nieoznaczony. Macierz nie została rozwiązana.")
            else:
                print("Błąd: Wykryto układ sprzeczny. Macierz nie została rozwiązana.")
            return -1
        # Przyjmujemy jako s ostatnią wartość z wiersza
        s = macierz[o][n]
        print("DEBUG:", macierz[o][n])
        # print(s)
        for p in range(n - 1, o, -1):
            # Przchodząc po kolei przez elementy w wierszu wyznaczamy wynik po lewej stronie równania
            s = s - macierz[o][p] * X[p]
        # Wyznaczamy ostateczną wartość niewiadomej
        X[o] = s / macierz[o][o]

    # print("Wyniki:")
    # print(X)
    return X
