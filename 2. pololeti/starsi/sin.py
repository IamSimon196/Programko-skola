import math
import time

start = int(input("Zadej pocatek intervalu: "))
end = int(input("Zadej konec intervalu: "))
step = int(input("Zadej krok: "))
ang = start




while ang <= end:
    print(f"Sinus pro uhel {ang} = {math.sin(math.radians(ang)):.2f}")
    print(f"Cosinus pro uhel {ang} = {math.cos(math.radians(ang)):.2f}")
    ang += step
    
