import random

soucet = 0
hoda, hodb = 0,0
while soucet != 6:
    hoda, hodb = random.randint(0, 6), random.randint(0, 6)
    soucet = hoda + hodb
    if soucet != 6:
        print(f"Bylo hozeno {hoda} a {hodb} a jejich soucet je {soucet}")

print(f"Pro soucet 6 bylo hozeno {hoda} a {hodb}")