import re

# Problem: 
# Aplikacje internetowe, które pobierają lub tworzą nazwę uzytkownika potrzebują funkcji, która "normalizuje" to co uzytkownik podał.
# na przykład: "john doe" - nie jest poprawna bo zawiera spację, musi być przekonwertowana na "john-doe".
# Nickname moze:
# - zawierać tylko małe litery
# - zawierać liczby
# - zawierac "-"

# Dane wejsciowe:
# Parametr jako string, który jest nickname (nazwa uzytkownika)

def sanitise(username: str):
    username = username.lower()
    username = re.sub(r"[^a-z0-9-]", "", username)
    return username

