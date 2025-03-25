import re

string = input("Zadej telefoni cislo:\n")

ans = re.findall(r"^\+420\s?((\d{9})|((\d{3}\s?){2}\d{3}))$", string)
if ans:
    print(f"telefoni cislo ma spravny format")
else:
    print(f"telefoni cislo nema spravny formatu")