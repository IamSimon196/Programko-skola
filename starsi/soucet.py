cislo = input("zadej cislo na reozebrani: ")
vysledek = 0
for i in range(0, len(cislo)):
    print(cislo[i])
    vysledek += int(cislo[i])
print(vysledek)