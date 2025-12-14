# Wlasciwe parametry
# 60-300
# 40-400
# 21-100

# Niewlasciwe (aplikacja wyrzuci blad)
# Ala ma kota
#(Ala ma kota)

# Moze pozniej obslugiwane (jak rozbudowac aplikacje)                                                   
# sys.argv[1: ]

import sys # Importujesz wbudowany pakiet "sys". Jezeli importujesz swój plik to nazywasz go "modułem". Pakiet = zewnętrzny, Moduł = plik własny (wewnętrzny)

# sys.argv[0] - komenda
# sys.argv[1] - pierwszy parametr...

def calculator(): # <-- definicja/nagłówek
    return 4+4 # <--- implementacja

calculator() # <--- wywołanie (funkcji)

print(sys.argv[1:]) # <--- wywołanie funkcji print z parameterem o indexie [1], która wyświetla wartość parametru na ekranie