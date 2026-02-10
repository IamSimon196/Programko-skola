vstup = input("Zadej číslo: ")

def prevest_na_cislo(vstup):
    try:
        return int(vstup)
    except ValueError:
        print("Nezadal jsi platné číslo.")
        return 0

print(prevest_na_cislo(vstup))