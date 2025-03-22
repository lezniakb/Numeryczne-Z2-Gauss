import eliminacja_Gaussa as g
import os

def wczytanie_macierzy(nazwa_pliku):
    # Dopisujemy txt do nazwy pliku
    # nazwa_pliku += ".txt"
    # Otwieramy plik tylko do odczytu 'r'
    with open(nazwa_pliku, 'r') as plik:
        # Tworzymy listę 'rownania', która zawiera wszystkie wiersze w pliku
        rownania = plik.readlines()

    n = len(rownania)
    # Sprawdzamy ilość równań
    if n > 10:
        print("BŁĄD: Przekroczono ilość 10 równań\n"
              "Podana ilość równań: " + str(n))

    # Deklarujemy macierz
    macierz = []

    # Przechodzimy przez wszystkie równania, zamieniamy je ze stringa na float i odpowiednio dodajemy do naszej macierzy
    for rownanie in rownania:
        wartosci = list(map(float, rownanie.split()))
        # Współczynniki równań
        macierz.append(wartosci)

    return macierz

# Początek programu
while True:
    plik = input("Podaj plik, w którym znajduje się macierz: ") + ".txt"
    if os.path.exists(plik):
        break
    plik = input("Podano błędną nazwę pliku, spróbuj ponownie: ") + ".txt"

macierz = wczytanie_macierzy(plik)
print("Wybrana macierz: ")
for wiersz in macierz:
    print(wiersz)
print("")

wyniki = g.Gauss(macierz)
if wyniki != -1:
    print("Otrzymane wyniki: ")
    for index, wynik in enumerate(wyniki):
        print("x" + str(index + 1) + ": " + str(wynik))


# o co chodzi z "użytkownik ma mieć możliwość wyboru ilości równań w trakcie pracy programu"
# czy w przypadku wyniku "0.4999999999999999" trzba zaokrąglić