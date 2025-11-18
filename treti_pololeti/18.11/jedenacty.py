list_1 = [1, 2, 3, 4, 5 ,6]
list_2 = ["ahoj", "pavle", "jak", "se", "mas"]

def add(a):
    final_list = []
    for i in range(len(a) - 1):
        final_list.append(a[i] + a[i + 1])
    return final_list

print(add(list_1))
print(add(list_2))