"""
Napisz funkcję, która jako parametry przyjmie: nazwę owocu i stan magazynowy owocu.
Funkcja ma operować na liście shop, której elementami są słowniki przyjmującymi wartości z argumentów.
Utwórz drugą funkcję zwracającą listę.
Uruchom pierwszą funkcję 5 razy w pętli, w trakcie której użytkownik będzie odpytywany o owoc i jego stan magazynowy.
Po pętli wypisz w konsoli listę shop. """


shop = []

def add_fruit(name, stock):
    fruit = {
        "name": name,
        "stock": stock
    }
    shop.append(fruit)

def get_shop():
    return shop

for i in range(0, 5):
    name = input("wpisz nazwe owocu\n")
    stock = input("ile na stanie\n")
    add_fruit(name, stock)

print(get_shop())