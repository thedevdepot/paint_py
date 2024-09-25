import pygame as pg
pg.init()

fps = 60
timer = pg.time.Clock()
WIDTH = 800
HEIGHT = 600

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
    yellow = pg.draw.rect(screen, (0, 0, 255), [WIDTH - 60, 35, 25, 25])
    teal = pg.draw.rect(screen, (0, 255, 255), [WIDTH - 85, 10, 25, 25])
    purple = pg.draw.rect(screen, (255, 0, 255), [WIDTH - 85, 35, 25, 25])
    white = pg.draw.rect(screen, (0, 0, 0), [WIDTH - 110, 10, 25, 25])
    black = pg.draw.rect(screen, (255, 255, 255), [WIDTH - 110, 35, 25, 25])
    color_rect = [blue, red, yellow, teal, purple, white, black]


run = True
while run:
    timer.tick(fps)
    screen.fill("white")

    draw_menu()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    pg.display.flip()
pg.quit()
