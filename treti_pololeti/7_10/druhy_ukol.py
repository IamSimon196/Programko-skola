with open("/run/media/simon/FLESKA/souborz python/Lorem.txt", "r", encoding="utf-8") as file:
    obsah = file.readline()
    print(obsah[1])
