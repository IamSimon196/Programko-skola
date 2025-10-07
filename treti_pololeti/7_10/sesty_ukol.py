with open("/run/media/simon/FLESKA/souborz python/Cisla.txt", "r", encoding="utf-8") as file:
    with open("/run/media/simon/FLESKA/souborz python/Cisla2.txt", "w", encoding="utf-8") as file2:
        for line in file:
            cislo = int(line)
            file2.write(f"{cislo * -1}\n")