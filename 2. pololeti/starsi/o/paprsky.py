import tkinter
import random

okno = tkinter.Tk()
okno.title('Úvod do grafických aplikací')
canvas = tkinter.Canvas(okno, bg='white', width=1200, height=800)
canvas.pack()

def random_color():
    return '#' + ''.join(random.choices('0123456789abcdef', k=6))

def draw():
    canvas.delete("all")
    for i in range(0, random.randint(10, 50)):
        canvas.create_line(0,0, random.randint(0, 1200),500, width=5, fill=random_color())
    okno.after(1000, draw)

draw()

okno.mainloop() 