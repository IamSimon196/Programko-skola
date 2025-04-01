string = input("Zadej nekolik vet:\n")
vety = string.split(".")
for veta in vety:
    if len(veta) > 0:
        if veta[0] == " ":
            ans = veta[1:]
        else:
            ans = veta
        print(ans)