import eliminacja_Gaussa as g
import os

def wczytanie_macierzy(nazwa_pliku):
    # Dopisujemy txt do nazwy pliku
    # nazwa_pliku += ".txt"
    # Otwieramy plik tylko do odczytu 'r'
    with open(nazwa_pliku, "r") as plik:
        # Tworzymy listę 'rownania', która zawiera wszystkie wiersze w pliku
        rownania = plik.readlines()

    n = len(rownania)
    # Sprawdzamy ilość równań
    if n > 10:
        print("BŁĄD: Przekroczono ilość 10 równań\n"
              "Podana ilość równań: " + str(n))
        exit(0)

    # Deklarujemy macierz
    macierz = []

    # Przechodzimy przez wszystkie równania, zamieniamy je ze stringa na float i odpowiednio dodajemy do naszej macierzy
    for rownanie in rownania:
        czesci = rownanie.split()  # podzial na czesci
        wartosci_float = map(float, czesci)  # zamiana na typ float
        wartosci = list(wartosci_float)  # zamiana mapy wartosci na liste
        # Współczynniki równań
        macierz.append(wartosci)

    return macierz

# Początek programu
# zabezpieczenie bez uzycia "break" zgodnie z instrukcją
czyIstnieje = False
while czyIstnieje != True:
    plik = input("Podaj numer zadania: ")
    plik += ".txt"
    sciezka = os.path.join("macierze", plik)  # połączenie katalogu zawierajacymi macierze z nazwą pliku

    # jesli plik istnieje to zakoncz petle i idz dalej
    if os.path.exists(sciezka):
        czyIstnieje = True
    else:
        print("Podano błędną nazwę pliku (numer zadania), spróbuj ponownie.")

# wyswietl macierz
macierz = wczytanie_macierzy(sciezka)
print("Wybrana macierz: ")
for wiersz in macierz:
    print(wiersz)

# znajdz rozwiazania przy uzyciu metody gaussa
wyniki = g.Gauss(macierz)
if wyniki != -1:
    print("Otrzymane wyniki: ")
    for index, wynik in enumerate(wyniki):
        print(f"x{(index + 1)}: {wynik:.3f}")


# o co chodzi z "użytkownik ma mieć możliwość wyboru ilości równań w trakcie pracy programu"
# czy w przypadku wyniku "0.4999999999999999" trzba zaokrąglić