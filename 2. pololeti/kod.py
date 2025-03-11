string = input("Zadej zpravu pro zakodovani:\n")
key = int(input("Zadej klic:\n"))

ans = ""
for s in string:
    if 33 <= ord(s) <= 122:
        new_char = ord(s) + key

        if 33 <= new_char <= 122:
            ans += chr(new_char)
        elif new_char < 33:
            ans += chr(122 - (33 - new_char) + 1)
        else:
            ans += chr(33 + (new_char % 122) -1)
    else:
        ans += s

print(f"Zakodovana zprava: {ans}")

string = input("Zadej zpravu:\n")
key = int(input("Zadej klic:\n"))


decoded_ans = ""
for s in string:
    if 33 <= ord(s) <= 122:
        new_char = ord(s) - key

        if 33 <= new_char <= 122:
            decoded_ans += chr(new_char)
        elif new_char < 33:
            decoded_ans += chr(122 - (33 - new_char) + 1)
        else:
            decoded_ans += chr(33 + (new_char % 122) -1)
    else:
        decoded_ans += s


print(f"zprava: {decoded_ans}")
