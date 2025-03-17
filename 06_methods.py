def is_pomidor(tekst: str):
    if "pomidor" in tekst.lower():
        print("tak, to jest pomidor")
    else:
        print("nie, nie jest pomidor")

def is_pomidor_return(tekst):
    return "pomidor" in tekst.lower()

is_pomidor("Pomidor w zupie")


wynik = is_pomidor_return("pomidor w zupie")
print(wynik)