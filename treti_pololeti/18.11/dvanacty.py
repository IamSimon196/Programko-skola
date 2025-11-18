n = int(input("Zadej libovolne cislo: "))

def find_divisors(n):
    divisors = []
    for i in range(1, int(n + 1)):
        if n % i == 0:
            divisors.append(i)
    return divisors

print(find_divisors(n))