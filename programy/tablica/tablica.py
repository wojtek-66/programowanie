import sys

# Opis problemu (programu):
# --------------------------
# Program pobiera parametr od uzytkownika i wypisuje slownie typ tej zmiennej.
# 1. Program pobiera parametr z lini komend
# 2. Program wypisuje paramet lub parametry.


# Dane wejściowe:
# --------------------------
# > 1 2 3 4 5
# > a 111 3 
# > 12  
# > 10 12 


# Algorytm:
# --------------------------
# 1. Podaj parametr 
# 2. Wypisz parametr 


# Implementacja:
# --------------------------
# 

# 1. Przypisać parametr do zmiennej (wczytać parametr)
params = sys.argv[1:]

# 2. Wyspisac parametr
print(params[0], params[-1])