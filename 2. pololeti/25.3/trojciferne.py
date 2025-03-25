import re
string = input("Zadej cislo:\n")

ans = re.findall(r"\s[0-9]{3}\s", string)
print(ans)