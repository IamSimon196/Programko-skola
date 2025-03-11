import tkinter
import random

VYSKA = 1000
SIRKA = 1000

okno = tkinter.Tk()
okno.title('Schody')
canvas = tkinter.Canvas(okno, bg='white', width=SIRKA, height=VYSKA)
canvas.pack()

def schody(pocatek, konec, pocet):
    x, y = pocatek
    dx = (konec[0] - pocatek[0]) / pocet
    dy = (konec[1] - pocatek[1]) / pocet

    for _ in range(pocet):
        x_end = x + dx
        canvas.create_line(x, y, x_end, y, width=5, fill="#000000")
        x = x_end

        y_end = y + dy
        canvas.create_line(x, y, x, y_end, width=5)
        y = y_end

schody((2, 2), (SIRKA - 2, VYSKA - 2), 5)
okno.mainloop()
