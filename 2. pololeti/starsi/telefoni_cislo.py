postup = False
while not postup:
    cislo = input("Zadej telefoni cislo\n")
    cislo = cislo.replace(" ", "")
    
    if cislo.isdecimal() and len(cislo) == 9:
        postup = True
    else:
        print("Spatny vstup")