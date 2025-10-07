import os

with open("/run/media/simon/FLESKA/souborz python/Pozvanka.txt") as file:
    obsah = file.read()
    jmena = open("/run/media/simon/FLESKA/souborz python/Jmena.txt").read().splitlines()
    for jmeno in jmena:
        text = obsah.replace("JMENO", jmeno)
        pozvanky_dir = "/run/media/simon/FLESKA/souborz python/pozvanky"
        os.makedirs(pozvanky_dir, exist_ok=True)
        with open(f"/run/media/simon/FLESKA/souborz python/pozvanky/Pozvanka_{jmeno}.txt", "w", encoding="utf-8") as file2:
            file2.write(text)