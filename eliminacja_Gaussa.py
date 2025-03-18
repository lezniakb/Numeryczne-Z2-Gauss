def Gauss(macierz):
    dokladnosc = 1e-12
    n = len(macierz)
    # Wiem, że pojebane idk jak to w komentarzu wytłumaczyć :sob:
    for i in range(n - 1):
        if abs(macierz[i][i]) < dokladnosc:
            for l in range(i + 1, n):
                if abs(macierz[i][l]) >= dokladnosc:
                    for p in range(n + 1):
                        temp = macierz[i][p]
                        macierz[i][p] = macierz[l][p]
                        macierz[l][p] = temp
        for j in range(i + 1, n):
            m = - macierz[j][i] / macierz[i][i]
            for k in range(n + 1):
                macierz[j][k] = macierz[j][k] + m * macierz[i][k]

    for wiersz in macierz:
        print(wiersz)