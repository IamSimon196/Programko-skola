import random

def sude(n: int) -> bool:
    if n%2 == 0:
        return True
    else:
        return False

for _ in range(0,4):
    rand = random.randint(0,100)
    if sude(rand):
        print(f"Cislo {rand} je sude")
    else:
        print(f"Cislo {rand} je liche")