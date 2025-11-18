recept = ["cukr", 100, "g", "vajicka", 5, "ks", "mleko", 2, "dcl"]

def rozloz_seznam(seznam):
    for i in range(0, len(seznam), 3):
        nazev = seznam[i]
        mnozstvi = seznam[i + 1]
        jednotka = seznam[i + 2]
        print(f"{mnozstvi} {jednotka} {nazev}")

rozloz_seznam(recept)