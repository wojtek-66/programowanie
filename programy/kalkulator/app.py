def kalkulator(param1: str, operation: str, param2: str):
    try:
        a = int(param1)
        b = int(param2)
    except ValueError:
        print("Błąd: parametr powinien być liczbą") 
        sys.exit(1) # Zakończenie programu z kodem wyjścia "1"

    # 3. Warunk 1
    if operation == "+":
        return (a + b)

    # 4. Warunk 2
    if operation == "-":
        return (a - b)

    # 5. Warunk 3
    if operation == "*":
        return (a * b)