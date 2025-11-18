first = [1, 2, 3, 4, 5 ,6]
second = ["ahoj", "pavle", "jak", "se", "mas"]
final = []

if len(first) > len(second):
    for i in range(len(second)):
        final.append(first[i])
        final.append(second[i])
else:
    for i in range(len(first)):
        final.append(first[i])
        final.append(second[i])

print(final)
