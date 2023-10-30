import pygame as py
import sys

# Screen Setting
py.init()
screen_dimensions = (1280, 720)
screen = py.display.set_mode(screen_dimensions)
clock = py.time.Clock()

# Misc Setup
py.display.set_caption("ICT project: Info inc.")

# Graphics Setup
bg = py.image.load("Graphics/R-C (3).jpeg")
# insert the needed image

ship_group = py.sprite.GroupSingle()

player = Player(group=ship_group)

# ORIGIN TOP LEFT, Y AXIS FLIPPED, USE TOP LEFT
# GET RECT


# Game Loop
while True:
    # Event Loop
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()

    # Time, Updates, Graphics
    delta_time = clock.tick(120) / 1000

    ship_group.update()

    screen.blit(bg, (0, 0))
    ship_group.draw(screen)

    # Screen Updates
    py.display.update()
