slovo = input("Zadej slovo pro rozklad: ")
for i in range(0, len(slovo) +1):
    slovo2 = ""
    for j in range(0, i):
        slovo2 += slovo[j]
    print(slovo2)