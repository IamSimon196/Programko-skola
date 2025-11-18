list = [1,0,5]

def is_sorted(lsit):
    prev = 0
    for n in list:
        if n < prev:
            return False
        prev = n
    return True
print(is_sorted(list))
    