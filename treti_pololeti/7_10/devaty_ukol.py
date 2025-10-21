import os
import shutil

def copy_photos(src_dir, dest_dir, photo_names):
    os.makedirs(dest_dir, exist_ok=True)
    for photo in photo_names:
        src = os.path.join(src_dir, photo)
        dst = os.path.join(dest_dir, photo)
        shutil.copy2(src, dst)
    print(f"Fotky byly zkopírovány do složky: {dest_dir}")

def list_files(dir_path):
    return [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]

def rename_file(dir_path, old_name, new_name):
    old_path = os.path.join(dir_path, old_name)
    new_path = os.path.join(dir_path, new_name)
    os.rename(old_path, new_path)
    print(f"{old_name} byl přejmenován na {new_name}")

def delete_file(dir_path, file_name):
    file_path = os.path.join(dir_path, file_name)
    os.remove(file_path)
    print(f"{file_name} byl smazán.")

def delete_folder(dir_path):
    shutil.rmtree(dir_path)
    print(f"Složka {dir_path} a všechny soubory byly smazány.")

def main():
    src_dir = "/run/media/simon/FLESKA/souborz python"
    photo_names = ["foto1.jpg", "foto2.jpg", "foto3.jpg"]

    dest_dir = input("Zadejte cílovou složku: ").strip()
    copy_photos(src_dir, dest_dir, photo_names)

    while True:
        print("\nCo si přejete udělat?")
        print("1 - Přejmenovat soubor")
        print("2 - Smazat soubor")
        print("3 - Smazat všechny soubory a složku")
        print("4 - Konec")
        volba = input("Zadejte číslo volby: ").strip()

        if volba == "1":
            files = list_files(dest_dir)
            print("Dostupné soubory:", files)
            old_name = input("Zadejte název souboru k přejmenování: ").strip()
            new_name = input("Zadejte nový název souboru: ").strip()
            if old_name in files:
                rename_file(dest_dir, old_name, new_name)
            else:
                print("Soubor nenalezen.")
        elif volba == "2":
            files = list_files(dest_dir)
            print("Dostupné soubory:", files)
            file_name = input("Zadejte název souboru ke smazání: ").strip()
            if file_name in files:
                delete_file(dest_dir, file_name)
            else:
                print("Soubor nenalezen.")
        elif volba == "3":
            delete_folder(dest_dir)
            break
        elif volba == "4":
            break
        else:
            print("Neplatná volba.")

if __name__ == "__main__":
    main()