start = int(input("Zadej zacatek intervalu: "))
end = int(input("Zadej konec intervalu: "))
radky = int(input("Zadej pocet cisel na radek: "))

def vypys_intervalu(start, end, radky):
    count = 0
    for i in range(start, end + 1):
        print(i, end=' ')
        count += 1
        if count % radky == 0:
            print()
    if count % radky != 0:
        print()

vypys_intervalu(start, end, radky)