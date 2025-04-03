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

def zapisz_macierz():
    iloscRownan = int(input("Podaj ilosc rownan: "))
    rownania = []
    for i in range(1, iloscRownan+1):
        while True:
            wartosci = input(f"Podaj wartosci w {i} wierszu (po przecinku): ").split(",")
            if len(wartosci) == iloscRownan+1:
                break
            print(f"Ilość wartości w wierszu się nie zgadza! Powinno być: {iloscRownan+1}")
        rownania.append(wartosci)
        print("Obecna postać macierzy:")
        for j in rownania:
            print(j)
    # zapisz do pliku
    while True:
        numerPliku = input("Podaj numer zadania: ")
        numerPliku += ".txt"
        sciezka = os.path.join("macierze", numerPliku)
        if os.path.exists(sciezka) == False:
            break
        print("Taki plik już istnieje! Wprowadź inną nazwę.")

    with open(sciezka, "w") as plik:
        for wiersz in rownania:
            payload = " ".join(wiersz) + "\n"
            plik.writelines(payload)

# Początek programu
wybor = "1"
while True:
    print("-----------\n"
          "Menu:\n"
          "1. Wczytaj macierz i rozwiąż\n"
          "2. Zapisz macierz\n"
          "3. Zakończ program")
    wybor = input("Wprowadź opcję: ")
    if wybor == "1":
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
    elif wybor == "2":
        zapisz_macierz()
    elif wybor == "3":
        print("Zakończono działanie programu")
        exit(0)
    else:
        print("Podano niewłaściwą opcję!")
    input("Wciśnij Enter aby kontynuować...")

# czy w przypadku wyniku "0.4999999999999999" trzba zaokrąglić