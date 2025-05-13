import pygame as pg

screen_width, screen_height = 500, 500
screen = pg.display.set_mode((screen_width, screen_height))

def draw_circle(r, c):
    colour = (0, 0, 0)
    if c > 0:
        colour = (255, 0, 0)
    elif c < 0:
        colour = (0, 0, 255)
    pg.draw.circle(screen, colour, (screen_width//2, screen_height//2), r)

n = int(input("Zadej pocet kruhu:\n"))

r = 50
dr = 50//n
r = 50 + (dr*n)

if n%2 == 0:
    c = -1
else:
    c = 1

for _ in range(0, n):
    draw_circle(r, c)
    r -= dr
    c *= -1

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

    pg.display.update()