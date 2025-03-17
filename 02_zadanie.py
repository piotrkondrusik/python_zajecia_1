slowo_1 = input("podaj pierwsze slowo:")
slowo_2 = input("podaj drugie slowo:")

dlugosc_1 = str(len(slowo_1))
dlugosc_2 = str(len(slowo_2))

if dlugosc_1 > dlugosc_2:
    print(f"pierwsze slowo jest dluzsze: {slowo_1} sklada sie z {dlugosc_1} liter")
else:
    print(f"drugie slowo jest dluzsze: {slowo_2} sklada sie z {dlugosc_2} liter")

if dlugosc_1 == dlugosc_2:
    print(f"oba slowa maja taka sama dlugosc: {dlugosc_1}")