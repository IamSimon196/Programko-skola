nb = int(input("Zadej prvni cislo intervalu:\n"))
ne = int(input("Zadej druhe cislo intervalu:\n"))

def prumer(nb: int, ne: int) -> float:
    ans = 0

    for i in range(nb, ne+1):
        ans += i
    ans = ans/(ne+1-nb)
    return ans

print(f"Prumer cisel v intervalu od {nb} do {ne} je {prumer(nb, ne)}")
