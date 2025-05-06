n = int(input("Zadej cele cislo:\n"))

def soucet_delitelu(n: int) -> int:

    '''
    input:
        n -> int
    returns:
        int
    '''

    ans = []
    ansint = 0
    for i in range(1,n+1):
        if n % i == 0:
            ans.append(i)
    for cislo in ans:
        ansint += cislo
    return ansint

print(f"Soucet delitelu cisla {n} je: {soucet_delitelu(n)}")