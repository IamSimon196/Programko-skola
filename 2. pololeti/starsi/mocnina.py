start = int(input("Zadej pocatek intervalu: "))
end = int(input("Zadej konec intervalu: "))
for i in range(start, end+1):
    print(f"Pro cislo {i} je druha mocnina {i**2}")