seznam = ["Ahoj", "Pavle", "jak", "se", "mas"]

def max_len_index(list):
    max_len = 0
    max_len_index = 0
    for i in range(0, len(list)):
        if len(list[i]) > max_len:
            max_len = len(list[i])
            max_len_index = i
    return max_len, max_len_index

max_len, index = max_len_index(seznam)

print(f"nejdelsi string je: {seznam[index]}; na pozici {index}")
