import sys

# Opis problemu (programu):
# --------------------------
# Program pobiera parametry od uzytkownika i podaje typ tych zmiennych.
# 1. Dla podanego parametru program sprawdza jego typ.
# 2. Program wypisuje typ parametru na ekran.




# Dane wejściowe:
# --------------------------
# > 10 (int)
# > Ala ma kota (str)
# > True (bool)
# > False (bool)



# Algorytm:
# --------------------------
# 1. PRZYPISZ parametr do zmiennej
# 2. Sprawdz typ podanego parametru i zamien go na liczbe calkowita
# 3. jEZELI parametr jest liczba calkowita to wypisz "liczba"
# 4. JEZELI parametr jest "True" LUB "False" to wypisz "bool"
# 5. Jezeli parametr jest stringiem TO wypisz "tekst"


# Implementacja:
# --------------------------



# 1. Przypisać parametr do zmiennej (wczytać parametry)
parametr = sys.argv[1]
# 2. Sprawdz typ podanego parametru i zamien go na liczbe calkowita
try:
    par1 = int(parametr)
    print("liczba")
#Jezeli parametr jest True LUB False to wypisz "bool"
except ValueError:
    if parametr.lower() == "true" or parametr.lower() == "false":
        print("bool")
#Jezeli parametr jest stringiem TO wypisz "tekst"
    else:
        print("tekst")

# -----
value = sys.argv[1]
try:
    print(int(parametr))
finally:
    text = value.lower()

    if (text in ('true', 'false')):
        print("bool")    
    else:
        print("tekst")ś



