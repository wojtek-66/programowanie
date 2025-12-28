import sys

# Zadanie
# - Maksymalnie 3 liczby
# - Sumuje i wypisuje je na ekranie

# Dane wejściowe:
# > 1 (1) <--------
# > 10 (10) 
# > 1 2 (3)
# > 1 2 3 (6)
# > 0 0 0 (0)
# > 0 -1 -1 (-2)
# > 0 (0)


# Algorytm:
# --------------------------
# 1. Sprawdz ile parametrów uzytkownik podał.
# 2. JEZELI uzytkownik poda TYLKO JEDEN parametr:
    # 2.1 Wypisz ten parametr na ekranie
    # 2.2 Zakończ program
# 3. JEZELI uzytkownik poda DWA parametry to:
    # 3.1 Przekonwertuj obydwa parametry na liczby
    # 3.2 Wypisz sume tych parametrów (dodaj jeden do drugiego)
    # 3.3 Zakoncz program
# 4. JEZELI uzytkownik poda TRZY parametry to:
    # 4.1 Przekonwertuj trzy parametry na liczy
    # 4.2 Wypisz sume tych trzech liczb na ekran
    # 4.3 Zakoncz program



# Implementacja:
# Krok 1.
numberOfParams = len(sys.argv) - 1

# Krok 2.
if (numberOfParams == 1):
    # Wypisuje i koncze program
    print(sys.argv[1])
    sys.exit(1)

if (numberOfParams == 2):
    # 3.1
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    # 3.2.
    print(a + b)
    # 3.3.
    sys.exit(1)

# Krok 4. 
if (numberOfParams == 3):
    # 4.1
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])
    # 4.2.
    print(a + b + c)
    # 4.3.
    sys.exit(1)