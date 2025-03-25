import re
string = input("Zadej adresu:\n")

ans = re.split(r"\s", string)
print(ans[-1])