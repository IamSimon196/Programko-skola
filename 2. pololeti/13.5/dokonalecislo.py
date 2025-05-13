n = int(input("Zadej cele cislo:\n"))

def dokonale(n: int):
    ans = 0
    for i in range(1,n):
        if n % i == 0:
            ans += i
    return ans == n

print(f"Cislo je dokonale cislo: {dokonale(n)}")