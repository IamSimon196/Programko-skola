n1 = int(input("Zadej prvni cislo:\n"))
n2 = int(input("Zadej druhe cislo:\n"))

def delitel(n1: int, n2: int):
    if n1 > n2:
        higher = n1
    elif n2 > n1:
        higher = n2
    else:
        return n1

    for i in range(higher, 0, -1):
        if n1%i == 0 and n2%i == 0:
            return i

print(f" nejvetsi spolecny delitel cisel {n1} a {n2} je {delitel(n1, n2)}")