n = int(input("Zadej konec intervalu:\n"))

def soucin(n):
    if n ==1:
        return n
    else:
        return n*soucin(n-1)
        
def iter_soucin(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans


if n > 0:
    if n > 1000:
        print(f"{iter_soucin(n)}")
    else:
        print(f"{soucin(n)}")