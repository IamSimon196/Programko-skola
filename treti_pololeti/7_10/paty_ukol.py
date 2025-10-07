with open("/run/media/simon/FLESKA/souborz python/Cisla.txt", "r", encoding="utf-8") as file:
    obsah = file.read()
    list_cisel = []
    for line in obsah.split("\n"):
        list_cisel.append(int(line))

    print("List cisel je:", list_cisel)
    print(f"Mean cisel je {sum(list_cisel)/len(list_cisel)}")
    print(f"Median cisel je {sorted(list_cisel)[len(list_cisel)//2]}") 

