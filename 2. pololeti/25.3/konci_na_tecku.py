import re

string_list = []
pocet = int(input("Zadej kolik je retezcu:\n"))

for i in range(0, pocet):
    string_list.append(input("Zadej vetu:\n"))

for i,string in enumerate(string_list):
    ans = re.findall(r"\.$", string)
    if ans:
        print(f"{i+1}. veta ma na konci tecku")
    else:
        print(f"{i+1}. veta nema na konci tecku")