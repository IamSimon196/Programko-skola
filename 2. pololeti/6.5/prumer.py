nb = int(input("Zadej prvni cislo intervalu:\n"))
ne = int(input("Zadej druhe cislo intervalu:\n"))

def prumer(nb: int, ne: int) -> tuple:
    ans1 = 0

    for i in range(nb, ne+1):
        ans1 += i
    ans2 = ans1/(ne+1-nb)
    return ans1, ans2

print(f"Soucet a prumer cisel v intervalu od {nb} do {ne} je {prumer(nb, ne)}")
