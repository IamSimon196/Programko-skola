dny = ["pondeli", "utery", "streda", "ctvrtek", "patek", "sobota", "nedele"]
days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

for i in range(len(dny)):
    print(dny[i], end=' ')
for i in range(len(days)):
    print(days[i], end=' ')
for i in range(len(dny)):
    print(f"{dny[i]} - {days[i]}")

