def Gauss(macierz):
    dokladnosc = 0.00001
    n = len(macierz)
    for i in range(n - 1):
        if abs(macierz[i][i]) < dokladnosc:
            return False
        for j in range(i + 1, n):
            m = - macierz[j][i] / macierz[i][i]
            for k in range(n + 1):
                macierz[j][k] = macierz[j][k] + m * macierz[i][k]

    for wiersz in macierz:
        print(wiersz)