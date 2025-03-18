import macierz as m
import eliminacja_Gaussa as g

macierz = m.wczytanie_macierzy("2")
for wiersz in macierz:
    print(wiersz)
print("")
g.Gauss(macierz)