string = input("Zadej vstup:\n")
ans = ""
for i, s in enumerate(string):
    if i+1 < len(string):
        if not (s == string[i+1]):
            ans += s
    else:
        ans += s

print(f"Opraveny text:\n {ans}")

        