start = input("zadej pocatek intervalu:\n")
end = input("zadej konec intervalu:\n")

string = ""
for i in range(int(start), int(end)+1):
    string += str(i)

print(f"Vas retezec je {string}")