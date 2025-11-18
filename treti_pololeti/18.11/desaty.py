def replace(list, a, b):
    for i in range(len(list)):
        if list[i] == a:
            list[i] = b
    return list
my_list = [1, 2, 3, 4, 2, 5, 2]
print(replace(my_list, 2, 99))