string = input("Zadej retezec:\n")
char = input("zadej znak pro pocitani:\n")
ans = 0
for i in string:
    if i == char:
        ans += 1
print(f"Znak {char} se v retezci vyskytuje {ans}x")