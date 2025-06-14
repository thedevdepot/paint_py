import pygame as pg
from pygame import MOUSEBUTTONDOWN

pg.init()

fps = 60
timer = pg.time.Clock()
WIDTH = 800
HEIGHT = 600
active_size = 5
active_color = 'green'
painting = []

screen = pg.display.set_mode([WIDTH, HEIGHT])
pg.display.set_caption('paint_with_python')

def draw_menu():
    pg.draw.rect(screen, 'gray', [0, 0, WIDTH, 70])
    pg.draw.line(screen, 'black', (0,70), (WIDTH, 70), 3)
    xl_brush = pg.draw.rect(screen, 'black', [10, 10, 50, 50])
    pg.draw.circle(screen, 'white', (35, 35), 20)
    l_brush = pg.draw.rect(screen, 'black', [70, 10, 50, 50])
    pg.draw.circle(screen, 'white', (95, 35), 15)
    m_brush = pg.draw.rect(screen, 'black', [130, 10, 50, 50])
    pg.draw.circle(screen, 'white', (155, 35), 10)
    s_brush = pg.draw.rect(screen, 'black', [190, 10, 50, 50])
    pg.draw.circle(screen, 'white', (215, 35), 5)
    brush_list = [xl_brush, l_brush, m_brush, s_brush]

    blue = pg.draw.rect(screen, (0, 0, 255), [WIDTH - 35, 10, 25, 25])
    red = pg.draw.rect(screen, (255, 0, 0), [WIDTH - 35, 35, 25, 25])
    green = pg.draw.rect(screen, (0, 255, 0), [WIDTH - 60, 10, 25, 25])
    yellow = pg.draw.rect(screen, (255, 255, 0), [WIDTH - 60, 35, 25, 25])
    teal = pg.draw.rect(screen, (0, 255, 255), [WIDTH - 85, 10, 25, 25])
    purple = pg.draw.rect(screen, (255, 0, 255), [WIDTH - 85, 35, 25, 25])
    white = pg.draw.rect(screen, (0, 0, 0), [WIDTH - 110, 10, 25, 25])
    black = pg.draw.rect(screen, (255, 255, 255), [WIDTH - 110, 35, 25, 25])
    color_rect = [blue, red, green, yellow, teal, purple, white, black]
    rgb_list = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0), (0, 255, 255),
                (255, 0, 255), (0, 0, 0), (255, 255, 255)]

    return brush_list, color_rect, rgb_list

def draw_painting(paints):
    for i in range(len(paints)):
        pg.draw.circle(screen, paints[i][0] , paints[i][1], paints[i][2])

run = True
while run:
    timer.tick(fps)
    screen.fill("white")
    mouse = pg.mouse.get_pos()
    left_click = pg.mouse.get_pressed()[0]

    if left_click and mouse[1] > 70:
        painting.append((active_color, mouse, active_size))

    draw_painting(painting) # This goes here so preview draws on top of picture.

    if mouse[1] > 70:
        pg.draw.circle(screen, active_color, mouse, active_size)

    brushes, colors, rgbs = draw_menu()


    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

        if event.type == MOUSEBUTTONDOWN:
            for i in range(len(brushes)):
                if brushes[i].collidepoint(event.pos):
                    active_size = 20 - (i * 5)

            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                    active_color = rgbs[i]

    pg.display.flip()
pg.quit()
