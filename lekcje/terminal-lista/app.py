import sys

# Opis problemu (programu):
# --------------------------
# Program pobiera liczbę naturalną od uzytkownika i wypisuje slownie typ tej liczby.
# 1. Dla liczby wiekszej niz 0 wypisz "dodatnia"
# 2. Dla zera wypisz zero
# 3. Dla liczby ujemnej wypisz "ujemna"


# Algorytm:
# --------------------------
# 1. PRZYPISZ parametr do zmiennej
# 2. PRZEKONWERTUJ parametr z ekranu na liczbę
# 2. JEZELI parametr > 0 TO wypisz "dodatnia"
# 3. JEZELI parametr = 0 TO wypisz "zero"
# 4. JEZELI parametr < 0 TO wypisz "ujemna"

# Implementacja:
# --------------------------

# 1. Przypisać parametr do zmiennej (wczytać parametr)
parametr = int(sys.argv[1])

# Warunek 1
if parametr > 0:
    print("dodatnia")

# Warunek 2
if parametr == 0:
    print("zero")

# Warunek 3
if parametr < 0:
    print("ujemna")

