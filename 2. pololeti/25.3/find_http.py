import re
string = input("Zadej adresu:\n")

ans = re.findall(r"https://", string)
print(ans)