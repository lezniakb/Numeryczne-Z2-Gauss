# Metody numeryczne Zadanie 2
## Opis
[PL]
Repozytorium zawiera algorytm rozwiązywania "n" równań liniowych o "n" niewiadomych metodą Gaussa w języku Python. Zadanie realizowane jest w ramach przedmiotu "*Metody numeryczne i optymalizacja*" na Politechnice Łódzkiej - 4 semestr na kierunku Informatyka Stosowana

[EN]
The repository contains an algorithm for solving "n" linear equations with "n" unknowns using Gauss method in Python. The task is carried out as part of the "Numerical Methods and Optimization" course at Lodz University of Technology – 4th semester in Computer Science.

## Dodatkowe informacje na temat zadania
Maksymalna ilość równań może być ograniczona z góry (np. 10), ale skonstruowany algorytm ma być uniwersalny, a użytkownik ma mieć możliwość wyboru ilości równań w trakcie pracy programu. Należy zapewnić możliwość wygodnego wprowadzania współczynników układu równań poprzez wczytywanie ich z pliku.
<br />W przypadku metod eliminacji program musi automatycznie wybierać element podstawowy i wykrywać sytuacje, kiedy układ jest sprzeczny albo nieoznaczony.

### Funkcjonalność
- [x] 1. Wczytywanie macierzy z pliku i zaimplementowanie algorytmu Gaussa
- [x] 2. Weryfikacja poprawności macierzy oraz sprawdzenie czy układ jest nieoznaczony lub sprzeczny
- [x] 3. Zapisywanie macierzy wprowadzonej przez użytkownika do pliku 

## Opis rozwiązania
W zadaniu wykorzystano metodę eliminacji Gaussa do rozwiązywania układów równań liniowych. Program jest uniwersalny i umożliwia wczytanie układu o dowolnej ilości równań. Limit maksymalnej ilości równań został ustawiony na 10, ale można go zmodyfikować. Współczynniki układu są ładowane z przygotowanego wcześniej pliku tekstowego. Pliki tekstowe odpowiadają przykładom z platformy Wikamp. Za pomocą funkcji program przekształca macierz rozszerzoną do postaci trójkątnej i realizuje podstawienie wsteczne. Dodano zabezpieczenia, które sprawdzają czy układ jest nieoznaczony lub sprzeczny i zwracają błąd, jeśli tak się wydarzy.

## Działanie algorytmu
### Etap 1: Doprowadzenie macierzy do postaci trójkątnej:
	1. Na początku program wybiera kolejne elementy diagonalne i sprawdza czy są różne od zera. Stosowana jest tutaj tolerancja 10^(-12), czyli maksymalny zakres zmiennej float. 
	2. W przypadku gdy element jest zbyt mały (bliski zera), algorytm bierze następny wiersz i szuka odpowiedniego współczynnika.
	3. Jeśli poszukiwany współczynnik zostanie znaleziony to zostaje on zamieniony miejscami z elementem diagonalnym.  
	4. Gdy pętla dojdzie do końca, a element diagonalny dalej jest bliski zera i nie został zastąpiony, to zostaje wypisana wiadomość że wystąpił błąd i funkcja kończy działanie. Zwracany jest kod błędu „-1” mówiący programowi, że funkcja zakończyła się z błędem.
	5. Jeśli element diagonalny nie jest zero lub bliski zera, to upraszczamy równania poniżej równania pierwszego (od drugiego włącznie w dół). Następuje to przez wyznaczenie mnożnika „m”: m=-(element diagonalny)/(element na tym samym indeksie,z głównego wiersza).
	6. Następnie wyliczane są nowe wartości elementów w wybranym wierszu. „m” to współczynnik, który określa razy ile powinniśmy odjąć element główny od elementu na którym się obecnie znajdujemy. Dzięki temu wyznaczana jest macierz trójkątna górna. 

### Etap 2: Podstawienie wsteczne:
	1. Jeżeli algorytmowi udało się doprowadzić macierz do postaci trójkątnej i nie zwrócił on kodu błędu -1 to wykonywane jest podstawienie wsteczne w celu wyznaczania kolejnych niewiadomych. Zaczyna się to od ostatniego równania w macierzy (najniższego wiersza).
	2. Jeżeli na tym etapie wystąpi błąd nieoznaczony lub sprzeczny, to program kończy działanie funkcji i zwraca odpowieni komunikat z błędem.
	3. W przeciwnym wypadku dla bieżącego wiersza (zaczynając od dołu) zmienna pomocnicza „s” przyjmuje wartość wyrazu wolnego, czyli ostatniego elementu w wierszu.
	4. Dalej kod sprawdza wszystkie współczynniki tego wiersza gdzie indeksy są większe niż ten na którym się znajdujemy (czyli tym, które odpowiadają znanym niewiadomym) i odejmuje od s iloczyny tych współczynników przez wcześniej obliczone wartości niewiadomych.
	5. Po nadpisaniu zmiennej „s” elementem zależnym od niewiadomej w równaniu, kod dzieli s przez element diagonalny i wynik zapisywany jest jako rozwiązanie dla tej niewiadomej.
