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
