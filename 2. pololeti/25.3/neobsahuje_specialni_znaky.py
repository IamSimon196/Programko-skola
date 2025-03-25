import re
string = input("Zadej znaky:\n")

ans = re.findall(r"([0-9])|(\.)|(\@)", string)
if ans:
    print(f"{string} obsahuje neplatny znak")
else:
    print(f"{string} je platny")