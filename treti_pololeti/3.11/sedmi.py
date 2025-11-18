import tkinter as tk

#kresli text
text = [200, 100, "Jazyk", "Verdana 20"]

def draw_text(canvas, text):
    if len(text) == 4:
        x, y, content, font = text
    else:
        x, y, content = text
        font = "Arial 30"
    canvas.create_text(x, y, text=content, font=font, fill="black")

#nastaveni okna
root = tk.Tk()
root.title("Sedmička")
canvas = tk.Canvas(root, width=400, height=200, bg="white")
canvas.pack()
draw_text(canvas, text)
root.mainloop()