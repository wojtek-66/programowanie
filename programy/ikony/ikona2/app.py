import sys

# Opis problemu (programu):
# --------------------------
# Program pobiera valuer od uzytkownika i wypisuje slownie typ tej zmiennej.
# 1. Program pobiera valuer z lini komend
# 2. Program wypisuje valuery wraz z ikonami.
# 


# Algorytm:
# --------------------------
# 1. Podaj valuer 
# 2. Wypisz valuery z ikonami
# 

# Implementacja:
# --------------------------


def ikonka2(valuer: str):
# 1. Przypisać valuer do zmiennej (wczytać valuery)
    valuer = sys.argv[1]
 
# 2. Wyspisac valuer z ikonami
    valuer = (valuer, ":-)", valuer)

    return valuer