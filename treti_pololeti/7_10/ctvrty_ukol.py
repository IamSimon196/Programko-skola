with open("/run/media/simon/FLESKA/souborz python/Lorem.txt", "r", encoding="utf-8") as file:
    for line in file:
        i = 0
        for char in line:
            if char == " ":
                i += 1
        if i%2 != 0:
            print(line)