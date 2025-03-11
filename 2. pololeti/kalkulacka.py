while True:
    print("Stiskni + pro scitani")
    print("Stiskni - pro odcitani")
    print("Stiskni * pro nasobeni")
    print("Stiskni / pro deleni")
    print("pro ukonceni prokramu zvol libovolny jiny znak")
    

    usri = input()
    print()

    match usri:
        case "+":
            num1 = int(input("Zadej prvni cislo: "))
            num2 = int(input("Zadej druhe cislo: "))
            print(f"Vysledek scitani je {num1 + num2}")
        case "-":
            num1 = int(input("Zadej prvni cislo: "))
            num2 = int(input("Zadej druhe cislo: "))
            print(f"Vysledek odcitani je {num1 - num2}")
        case "*":
            num1 = int(input("Zadej prvni cislo: "))
            num2 = int(input("Zadej druhe cislo: "))
            print(f"Vysledek nasobeni je {num1 * num2}")
        case "/":
            num1 = int(input("Zadej prvni cislo: "))
            num2 = int(input("Zadej druhe cislo: "))
            print(f"Vysledek deleni je {num1 / num2}")
        case _:
            break
    print()
