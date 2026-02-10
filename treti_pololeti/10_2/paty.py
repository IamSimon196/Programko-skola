def secti(seznam):
    #najdi typ prvni hodnoty, pomoci try zkus prevest zbytek a secti, pokud se nepovede, vypis proc a pokracuj
    typ = type(seznam[0])
    vysledek = seznam[0]
    for i in seznam[1:]:
        try:
            vysledek += typ(i)
        except ValueError:
            print(f"lisi se od zbytku: {i}")
    return vysledek

cisla = [1, 2, 3, 4, 5, "Ahoj"]
cisla_a_stringy = [1, 2, "3", 4, 5]
stringy_a_cisla = ["1", "2", 3, "4", 5, "ahoj"]
print(secti(cisla))
print(secti(cisla_a_stringy))
print(secti(stringy_a_cisla))