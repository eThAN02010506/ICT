import pygame as py

py.init()

win = py.display.set_mode((500, 500))

py.display.set_caption('Scene Switcher')

center_x = 250 - 130
center_y = 250

black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)


def ct(font, size, text, color):
    mf = py.font.Font(font, size)

    t = mf.render(text, True, color)

    return t


def draw_scene1():
    print("This is Scene 1")
    txt = ct("SB.ttf", 40, "Hello World!", black)
    win.blit(txt, (center_x, center_y))


def draw_scene2():
    print("This is scene 2")
    txt2 = ct("SB.ttf", 40, "scene2 ", black)
    win.blit(txt2, (center_x, center_y))


scene_counter = 0

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

        elif event.type == pg.MOUSEBUTTONDOWN:
            scene_counter += 1

    win.fill(red)
    if scene_counter == 0:
        draw_scene1()
    else:
        draw_scene2()

    py.display.update()

py.quit()
# When this function is called the next scene is drawn.

def draw_next_screen():
    global scene_counter
    scene_counter += 1
    if scene_counter == 1:
        draw_scene1()
    else:
        draw_scene2()


if mouses:
    draw_next_screen()

    py.display.update()

