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
# 2. PRZEKONWERTUJ parametr(number) z ekranu na liczbę
# 3. JEZELI parametr = "+" TO wykonaj dodawanie
# 4. JEZELI parametr = "-" TO wykonaj odejmowanie
# 5. JEZELI parametr = "*" TO wykonaj mnozenie
# 6. JEZELI parametr = "//" TO wykonaj dzielenie
# 7. W PRZECIWNYM RAZIE wypisz komunikat o bledzie

# Implementacja:3
# --------------------------


# 1. Przypisać parametry do zmiennych (wczytać parametr)
num_1 = sys.argv[1]
operation = sys.argv[2]
num_2 = sys.argv[3]

if num_2 == "0":
    print("Drugi parametr nie moze byc zerem")
    sys.exit(1)

# 2. PRZEKONWERTUJ parametr(number) z ekranu na liczbę
try:
    par1 = int(num_1)
    par2 = int(num_2) # "100" => 100
except ValueError:
    print("Błąd: Parametr powinien być liczbą") 
    sys.exit(1) # Zakończenie programu z kodem wyjścia "1"


# 3. Warunk 1
if operation == "+":
    result = par1 + par2
    print("Wynik dodawania wynosi: " ,result)

# 4. Warunk 2
if operation == "-":
    result = par1 - par2
    print("Wynik odejmowania wwynosi: " ,result)

# 5. Warunk 3
if  operation == "*":
    result = par1 * par2
    print("Wynik mnozenia wynosi: " ,result)

# 6. Warunk 4
if  operation == "/":
    try:
        result = par1 // par2
    except ZeroDivisionError:
        print("Nie mozna dzielic przez 0") 
        sys.exit(1) # Zakończenie programu z kodem wyjścia "1"
    
    print("Wynik dzielenia wynosi: " ,result)
       

   





