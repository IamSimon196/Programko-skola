n = int(input("Zadej cele cislo:\n"))

def delitele(n: int):
    ans = []
    for i in range(1,n):
        if n % i == 0:
            ans.append(i)
    return ans

print(f"Delitele cisla {n} jsou: {delitele(n)}")