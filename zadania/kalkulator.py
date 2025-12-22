import sys

# Opis problemu (programu):
# --------------------------
# Program pobiera parametry od uzytkownika i zamienia na liczbe calkowita.
# 1. Dla operacji "+" wykonuje operacje dodawania
# 2. Dla operacji "-" wykonuje operacje odejmowania
# 3. Dla operacji "*" wykonuje operacje mnozenia
# 4. Dla innych operacji wypisuje komunikat o bledzie.


# Algorytm:
# --------------------------
# 1. PRZYPISZ parametry do zmiennych
# 2. JEZELI parametr = "+" TO wykonaj dodawanie
# 3. JEZELI parametr = "-" TO wykonaj odejmowanie
# 4. JEZELI parametr = "*" TO wykonaj mnozenie
# 5. W PRZECIWNYM RAZIE wypisz komunikat o bledzie

# Implementacja:
# --------------------------


# 1. Przypisać parametry do zmiennych (wczytać parametr)
num1 = int(sys.argv[1])
operation = sys.argv[2]
num2 = int(sys.argv[3])

# 2. Warunk 1
if operation == "+":
    result = num1 + num2
    print(" Wynik dodawania wynosi: " ,result)

# 3. Warunk 2
if operation == "-":
    result = num1 - num2
    print("Wynik odejmowania wwynosi: " ,result)

# 4. Warunk 3
if operation == "*":
    result = num1 * num2
    print("Wynik mnozenia wynosi: " ,result)



