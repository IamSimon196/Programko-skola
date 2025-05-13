begin = int(input("Zadej pocatecni cislo:\n"))
end = int(input("Zadej konecne cislo:\n"))

def dokonale(beg: int, end: int):
    ans_list = []
    for n in range(beg, end):
        ans = 0  
        for i in range(1, n):
            if n % i == 0:
                ans += i
        if ans == n:
            ans_list.append(n) 
    return ans_list

print(f"V intervalu {begin}, {end} je dokonale cislo: {dokonale(begin, end)}")

