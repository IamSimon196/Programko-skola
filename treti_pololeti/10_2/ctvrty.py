with open(r"C:\Users\linti\Desktop\programko\10_2\cisla.txt", "r") as f:
    cisla = []
    data = f.read()
    print(data)
    for n in data.split():
        try:
            cisla.append(float(n))
        except ValueError:
            print(f"Nezadal jsi platné číslo: {n}")
            continue
print(cisla)
