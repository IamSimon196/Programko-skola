import random

num = random.randint(0,20)
vyhra = False

def vyhodnot_tip(n, tip):
    if tip > n:
        print("Niz")
        return False
    elif tip < n:
        print("Vys")
        return False
    else:
        return True

for _ in range(0,5):
    tip = int(input("Zade jtip od 0 do 20:\n"))

    vyhra = vyhodnot_tip(num, tip)

    if vyhra:
        print("Vyhral jsi")
        break

if not vyhra:
    print("Prohral jsi")