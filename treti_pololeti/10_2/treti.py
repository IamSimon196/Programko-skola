def vypocet_mocniny(cislo, exponent):
    try:
        return cislo ** exponent

    except TypeError:
        print("Nezadal jsi platné číslo nebo exponent.")
        return None
    except OverflowError:
        print("Výsledek je příliš velký.")
        return None
    
cislo = input("Zadej číslo: ")
exponent = input("Zadej exponent: ")
print(vypocet_mocniny(cislo, exponent))