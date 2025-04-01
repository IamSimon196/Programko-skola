string = input("Zadej string:\n")
index = input(f"Muzes zadat cislo mezi 1 a {len(string)} pro zmeneny pismena na dane pozici:\n")
index = int(index) - 1

if index >= 0 and index < len(string):
    ans = ""
    for i in range(0, len(string)):
        if i != index:
            ans += string[i]
        else:
            ans += string[i].upper()
    print(f"vysledek je: {ans}")

else:
    print("neplatny index")