def zadanie_domowe():
    lista = []

    while True:
        print("\nMenu:")
        print("1 – Dodaj element do listy")
        print("2 – Wypisz listę")
        print("3 – Posortuj listę rosnąco")
        print("4 - Posortuj listę malejąco")
        print("5 – Zakończ")

        wybor = input("Wybierz opcję: ")

        if wybor == '1':
            element = input("Podaj element do dodania: ")
            lista.append(element)
        elif wybor == '2':
            if lista:
                print(f"\nAktualna lista: {lista}")
            else:
                print("Lista jest pusta.")
        elif wybor == '3':
            lista.sort()
            print("Lista w kolejnosci rosnacej.")
        elif wybor == '4':
            lista.reverse()
            print("Lista w kolejnosci malejacej")
        elif wybor == '5':
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

zadanie_domowe()