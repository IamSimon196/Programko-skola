n = int(input("zadej n: "))
stri = ""
for i in range(0, n):
    for j in range(0, i+1):
        stri += "*"
    stri += " "
print(stri)