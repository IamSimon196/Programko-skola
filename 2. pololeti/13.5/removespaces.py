string = input("Zadej retezec pro odstraneni mezer:\n")

def remove_space(n: str) -> str:
    ans = ""
    for char in string:
        if char != " ":
            ans += char
    return ans

print(f"Retezec bez mezer je: {remove_space(string)}")