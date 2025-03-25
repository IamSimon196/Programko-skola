import re
string = input("Zadej znaky:\n")

ans = re.findall(r"^.{0,15}$", string)
if ans:
    print(f"{string} ma do 15 znaku")
else:
    print(f"{string} ma vice jak 15 znaku")