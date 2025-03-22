def Gauss(macierz):
    dokladnosc = 1e-12
    n = len(macierz)
    # Macierz przechowująca wyniki
    X = []

    for niewiadoma in range(n):
        X.append(0)

    # Wiem, że pojebane idk jak to w komentarzu wytłumaczyć :sob:

    # Doprowadzamy macierz do postaci trójkątnej
    for i in range(n - 1):
        # Sprawdzamy, czy dzielnik jest różny od zera
        if abs(macierz[i][i]) < dokladnosc:
            # jeżeli tak to szukamy w kolejnych wierszach współczynnika, który jest różny od 0 i zamieniamy kolejnością
            for l in range(i + 1, n):
                if abs(macierz[l][i]) > dokladnosc:
                    for m in range(n + 1):
                        temp = macierz[i][m]
                        macierz[i][m] = macierz[l][m]
                        macierz[l][m] = temp

            # Jeżeli w żadnym z wierszy nie znajdzie odpowiedniego współczynnika, to kończymy program
            if abs(macierz[i][i]) < dokladnosc:
                print("BLAD - dzielenie przez 0")
                return -1
        for j in range(i + 1, n):
            m = - macierz[j][i] / macierz[i][i]
            for k in range(n + 1):
                macierz[j][k] = macierz[j][k] + m * macierz[i][k]

    # for wiersz in macierz:
    #     print(wiersz)

    # Odwrotne wyznaczanie niewiadomych
    for o in range(n - 1, -1, -1):
        if abs(macierz[o][o]) < dokladnosc:
            if abs(macierz[o][o + 1]) < dokladnosc:
                print("BLAD - układ nieoznaczony")
            else:
                print("BLAD - układ sprzeczny")
            return -1
        # Przyjmujemy jako s ostatnią wartość z wiersza
        s = macierz[o][n]
        # print(s)
        for p in range(n - 1, o, -1):
            # Przchodząc po kolei przez elementy w wierszu wyznaczamy wynik po lewej stronie równania
            s = s - macierz[o][p] * X[p]
        # Wyznaczamy ostateczną wartość niewiadomej
        X[o] = s / macierz[o][o]

    # print("Wyniki:")
    # print(X)
    return X
