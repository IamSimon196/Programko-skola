import tkinter
import time

VYSKA = 1000
SIRKA = 1000
pocet = 50

okno = tkinter.Tk()
okno.title(f'Hraci pole {pocet}x{pocet}')
canvas = tkinter.Canvas(okno, bg='white', width=SIRKA, height=VYSKA)
canvas.pack()

def draw(n, odstup):
    x, y = odstup, odstup
    x_end, y_end = SIRKA - odstup, VYSKA - odstup
    dx, dy = (SIRKA - odstup*2) / n, (VYSKA - odstup*2) / n

    for _ in range(0, n+1):
        canvas.create_line(x, odstup, x, y_end, width=5, fill="#000000")
        x += dx

    for _ in range(0, n+1):
        canvas.create_line(odstup, y, x_end, y, width=5, fill="#000000")
        y += dy

start = time.time()
draw(pocet, 20)
end = time.time()
print(f"Cas potrebny pro vykresleni byl {end - start}s")

okno.mainloop()
