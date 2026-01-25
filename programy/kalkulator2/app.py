import sys

def kalkulator(wartosc1: int, operation: str, wartosc2: int):


    # 3. Warunk 1
    def dodawanie(a: int, b: int):
        if operation == "+":
            return a + b

    # 4. Warunk 2
    def odejmowanie(a: int, b: int):
        if operation == "-":
            return a - b
        

    # 5. Warunk 3
    def mnozenie(a: int, b: int):
        if operation == "*":
            return a * b
            

    # 6. Warunk 4
    def dzielenie(a: int, b: int):
         return a // b
        
    return dodawanie(wartosc1, wartosc2) or odejmowanie(wartosc1, wartosc2) or mnozenie(wartosc1, wartosc2) or dzielenie(wartosc1, wartosc2)
        

    




