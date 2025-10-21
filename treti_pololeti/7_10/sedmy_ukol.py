import tkinter as tk

def draw_squares():
    status_label.config(text="", fg="black")
    try:
        x = int(entry_x.get().strip())
        y = int(entry_y.get().strip())
        side = int(entry_side.get().strip())
        count = int(entry_count.get().strip())
    except ValueError:
        status_label.config(text="Chyba: zadejte platná celá čísla.", fg="red")
        return

    if side <= 0 or count <= 0:
        status_label.config(text="Chyba: délka strany a počet musí být kladné.", fg="red")
        return

    spacing = side * 2  # vzdálenost mezi začátky čtverců

    canvas.delete("all")
    for i in range(count):
        x0 = x + i * spacing
        y0 = y
        canvas.create_rectangle(x0, y0, x0 + side, y0 + side, outline="black", fill=entry_color.get().strip())

    try:
        with open("Ctverce.txt", "w", encoding="utf-8") as f:
            f.write(f"start_x={x}\n")
            f.write(f"start_y={y}\n")
            f.write(f"side_length={side}\n")
            f.write(f"count={count}\n")
            f.write(f"spacing={spacing}\n")
        status_label.config(text="Parametry byly uloženy do Ctverce.txt", fg="green")
    except Exception as e:
        status_label.config(text=f"Chyba při ukládání: {e}", fg="red")

root = tk.Tk()
root.title("Čtverce")
root.geometry("900x500")

frm = tk.Frame(root, padx=10, pady=10)
frm.pack(side="top", fill="x")

tk.Label(frm, text="Start X:").grid(row=0, column=0, sticky="e")
entry_x = tk.Entry(frm, width=10)
entry_x.grid(row=0, column=1, padx=5, pady=2)
entry_x.insert(0, "20")

tk.Label(frm, text="Start Y:").grid(row=0, column=2, sticky="e")
entry_y = tk.Entry(frm, width=10)
entry_y.grid(row=0, column=3, padx=5, pady=2)
entry_y.insert(0, "20")

tk.Label(frm, text="Délka strany:").grid(row=1, column=0, sticky="e")
entry_side = tk.Entry(frm, width=10)
entry_side.grid(row=1, column=1, padx=5, pady=2)
entry_side.insert(0, "40")

tk.Label(frm, text="Počet čtverců:").grid(row=1, column=2, sticky="e")
entry_count = tk.Entry(frm, width=10)
entry_count.grid(row=1, column=3, padx=5, pady=2)
entry_count.insert(0, "5")

tk.Label(frm, text="Barva:").grid(row=0, column=4, sticky="e")
entry_color = tk.Entry(frm, width=10)
entry_color.grid(row=0, column=5, padx=5, pady=2)
entry_color.insert(0, "red")

btn_draw = tk.Button(frm, text="Kreslit a uložit", command=draw_squares)
btn_draw.grid(row=2, column=0, columnspan=4, pady=8)

canvas = tk.Canvas(root, width=860, height=360, bg="white")
canvas.pack(fill="both", expand=True, padx=10, pady=(0,10))

status_label = tk.Label(root, text="", anchor="w")
status_label.pack(fill="x", padx=10, pady=(0,10))

root.mainloop()