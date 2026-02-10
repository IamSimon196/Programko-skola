def realne_cislo(vstup):
    #navrat true pokud je vstup desetine cislo, jinak false
    try:
        float(vstup)
        return True
    except ValueError:
        return False
    
cislo = input("Zadej reálné číslo: ")
if realne_cislo(cislo):
    print("Zadal jsi reálné číslo.")
else:
    print("Nezadal jsi reálné číslo.")