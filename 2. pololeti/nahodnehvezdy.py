import tkinter
import random
import time

SIRKA, VYSKA = 1000, 1000
okno = tkinter.Tk()
okno.title('hvezdy')
canvas = tkinter.Canvas(okno, bg='blue', width=SIRKA, height=VYSKA)
canvas.pack()

n = 100

def draw():
    canvas.delete("all")
    for _ in range(0, n):
        canvas.create_text(random.randint(0, SIRKA),random.randint(0, VYSKA),text="*", font=("Arial", random.randint(10, 20)),fill='#ffb300')

start = time.time()
draw()
end = time.time()
print(f"Cas potrebny k vykresleni byl {end - start}s")

okno.mainloop() 