import sys

# Opis problemu (programu):
# --------------------------
# Program pobiera liczbę naturalną od uzytkownika i wypisuje slownie typ tej liczby.
# 1. Dla liczby rownej 100 wypisz ":-|"
# 2. Dla liczby wiekszej niz 100 wypisz ":-)"
# 3. Dla liczby mniejszej niz 100 wypisz ":-("

# Dane testowe:
# --------------------------
# Happy path: 100, 200, 50
# Inne mozliwe wartosci: aaaa

# Algorytm:
# --------------------------
# 1. PRZYPISZ parametr(number) do zmiennej
# 2. PRZEKONWERTUJ parametr(number) z ekranu na liczbę
# 3. JEZELI parametr > 100 TO wypisz ":-)"
# 4. JEZELI parametr = 100 TO wypisz ":-|"
# 5. JEZELI parametr < 100 TO wypisz ":-("

# try - catch

# Implementacja:
# --------------------------


# 1. Przypisać parametr do zmiennej (wczytać parametr)
# KAZDY PARAMETR POBRANY Z TERMINALA JEST TYPU "STRING"
param = sys.argv[1] # W ZMIENNEJ MASZ WARTOSC PARAMETRU: "100", "aaaaa", "899"

# 2. PRZEKONWERTUJ parametr(number) z ekranu na liczbę
try:
    number = int(param) # "100" => 100
except ValueError:
    print("Błąd: parametr powinien być liczbą") 
    sys.exit(1) # Zakończenie programu z kodem wyjścia "1"

# 3. Warunek 1
if number == 100:
    print(":-|")

# 4. Warunek 2 
if number > 100:
    print(":-)")

# 5. Warunek 3
if number < 100:
    print(":-(")
