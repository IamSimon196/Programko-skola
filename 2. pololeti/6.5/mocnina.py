n = int(input("Zadej cislo pro mocneni:\n"))
exp = input("Zadej exponent:\n")

def mocnina(n: int, e) -> int:
    try:
        e = int(e) 
    except ValueError:
        e = 2  
    return n ** e

print(mocnina(n, exp))
