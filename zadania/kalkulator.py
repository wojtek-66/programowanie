import sys

# Opis problemu (programu):
# --------------------------
# Program pobiera parametry od uzytkownika i zamienia na liczbe calkowita.
# 1. Dla operacji "+" wykonuje operacje dodawania
# 2. Dla operacji "-" wykonuje operacje odejmowania
# 3. Dla operacji "*" wykonuje operacje mnozenia
# --- EXTRA ---
# 4*. Dla innych operacji wypisuje komunikat o bledzie.

# Dane wejściowe:
# --------------------------
# > 10 + 2 (12)
# > 8 - 2 (6)
# > 12 * 3 (24)
# > 0 - 0 (0)
# > 10 - 12 (-2)
# > 10 * 0 (0)

# Algorytm:
# --------------------------
# 1. PRZYPISZ parametry do zmiennych
# 2. PRZEKONWERTUJ parametr(number) z ekranu na liczbę
# 3. JEZELI parametr = "+" TO wykonaj dodawanie
# 4. JEZELI parametr = "-" TO wykonaj odejmowanie
# 5. JEZELI parametr = "*" TO wykonaj mnozenie
# --- extra ---
# 6. W PRZECIWNYM RAZIE wypisz komunikat o bledzie

# Implementacja:
# --------------------------

# 1. Przypisać parametry do zmiennych (wczytać parametr)
# KAZDY PARAMETR POBRANY Z TERMINALA JEST TYPU "STRING"
param1 = sys.argv[1] # W ZMIENNEJ MASZ WARTOSC PARAMETRU: "100", "899"
operation = sys.argv[2] # W ZMIENNEJ MASZ WARTOSC PARAMETRU: "+", "-", "*"
param2 = sys.argv[3] # W ZMIENNEJ MASZ WARTOSC PARAMETRU: "100", "899"


 
# 2. PRZEKONWERTUJ parametr(number) z ekranu na liczbę
try:
    a = int(param1)
    b = int(param2)
except ValueError:
    print("Błąd: parametr powinien być liczbą") 
    sys.exit(1) # Zakończenie programu z kodem wyjścia "1"


# 3. Warunk 1
if operation == "+":
    result = a + b
    print(" Wynik dodawania wynosi: ", result)

# 4. Warunk 2
if operation == "-":
    result = a - b
    print("Wynik odejmowania wwynosi: ", result)

# 5. Warunk 3
if operation == "*":
    result = a * b
    print("Wynik mnozenia wynosi: ", result)




