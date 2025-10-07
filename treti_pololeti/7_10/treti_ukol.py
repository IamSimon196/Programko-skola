with open("/run/media/simon/FLESKA/souborz python/Lorem.txt", "r", encoding="utf-8") as file:
    for i, line in enumerate(file):
        print(f"Radek {i} ma {len(line)} znaku")