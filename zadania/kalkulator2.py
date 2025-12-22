import sys

# Opis problemu (programu):
# --------------------------
# Program pobiera parametry od uzytkownika i zamienia na liczbe calkowita.
# 1. Dla operacji "+" wykonuje operacje dodawania
# 2. Dla operacji "-" wykonuje operacje odejmowania
# 3. Dla operacji "*" wykonuje operacje mnozenia
# 4. Dla operacji "//" wykonuje operacje dzielenia
# 5. Dla innych operacji wypisuje komunikat o bledzie.


# Algorytm:
# --------------------------
# 1. PRZYPISZ parametry do zmiennych
# 2. JEZELI parametr = "+" TO wykonaj dodawanie
# 3. JEZELI parametr = "-" TO wykonaj odejmowanie
# 4. JEZELI parametr = "*" TO wykonaj mnozenie
# 5. JEZELI parametr = "//" TO wykonaj dzielenie
# 6. W PRZECIWNYM RAZIE wypisz komunikat o bledzie

# Implementacja:
# --------------------------


# 1. Przypisać parametry do zmiennych (wczytać parametr)
num_1 = int(sys.argv[1])
operation = sys.argv[2]
num_2 = int(sys.argv[3])

# 2. Warunk 1
if operation == "+":
    result = num_1 + num_2
    print("Wynik dodawania wynosi: " ,result)

# 3. Warunk 2
if operation == "-":
    result = num_1 - num_2
    print("Wynik odejmowania wwynosi: " ,result)

# 4. Warunk 3
if  operation == "*":
    result = num_1 * num_2
    print("Wynik mnozenia wynosi: " ,result)

# 5. Warunk 4
if  operation == "/":
    result = num_1 // num_2
    print("Wynik dzielenia wynosi: " ,result)

# 6. Warunk 5
if  num_2 == 0:
    print("Nie mozna dzielic przez 0")




