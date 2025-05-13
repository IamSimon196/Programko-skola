begin = int(input("Zadej pocatecni cislo:\n"))
end = int(input("Zadej konecne cislo:\n"))

def dokonale(n: int):
    ans = 0
    for i in range(1,n):
        if n % i == 0:
            ans += i
    return ans == n

for n in range(begin, end):
    print(f"Cislo {n} je dokonale cislo: {dokonale(n)}")

#6, 28, 496